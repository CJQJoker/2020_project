import xlrd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
import numpy as np
from PIL import Image


#字典用于存储词频
counts = {}
#打开xls文件
ad_wb = xlrd.open_workbook("data_2.xls")
#获取第一个目标表单
sheet_0 = ad_wb.sheet_by_index(0)
#生成存有所有通知正文的txt
for i in range(sheet_0.nrows):
    with open("all-notice.txt","a", encoding="utf-8") as f:
        f.write(sheet_0.cell_value(i,3))
        f.write('\n')

text = open("{}.txt".format('all-notice'), encoding="utf-8").read()
jieba.load_userdict('dict.txt')
# 加载背景图片
cloud_mask = np.array(Image.open("bg.png"))
# 设置词云
wc = WordCloud(
    # 设置背景颜色
    background_color="white",
    # 背景图片
    mask=cloud_mask,
    # 设置最大显示的词云数
    max_words=2000,
    # 这种字体都在电脑字体中，一般路径
    font_path='simsun.ttf',
    height=1200,
    width=1600,
    # 设置字体最大值
    max_font_size=100,
    # 设置随机生成状态
    random_state=40,
)

words_list = []
word_generator = jieba.cut(text, cut_all=False)
with open('stopwords.txt', encoding='utf-8') as f:
    unicode_text = f.read()
    f.close()
for word in word_generator:
    if word.strip() not in unicode_text:
        words_list.append(word)
        counts[word] = counts.get(word, 0) + 1
text = ' '.join(words_list)

myword = wc.generate(text)  # 生成词云
# 展示词云图
plt.imshow(myword)
plt.axis("off")
plt.show()
wc.to_file('all-notice.png')  #保存词云
