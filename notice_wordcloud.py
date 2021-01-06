import xlrd
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
import jieba
import numpy as np
from PIL import Image


#打开xls文件
ad_wb = xlrd.open_workbook("data_2.xls")
#获取第一个目标表单
sheet_0 = ad_wb.sheet_by_index(0)
#生成存有所有通知正文的txt
for i in range(sheet_0.nrows):
    with open("all-notice.txt","a", encoding="utf-8") as f:
        f.write(sheet_0.cell_value(i,3))
        f.write('\n')


#把需要屏蔽的词全部放入stopwords文本文件中
def stop_words(texts):
    words_list = []
    word_generator = jieba.cut(texts, cut_all=False)  # 返回的是一个迭代器
    with open('stopwords.txt',encoding='utf-8') as f:
        unicode_text = f.read()
        f.close() 
    for word in word_generator:
        if word.strip() not in unicode_text:
            words_list.append(word)
    return ' '.join(words_list) 

def create_word_cloud(filename):
    text = open("{}.txt".format(filename), encoding="utf-8").read()

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

    text = stop_words(text)
    myword = wc.generate(text)  # 生成词云
    # 展示词云图
    plt.imshow(myword)
    plt.axis("off")
    plt.show()
    wc.to_file('all-notice.png')  # 把词云保存

if __name__ == '__main__':
    create_word_cloud('all-notice')
