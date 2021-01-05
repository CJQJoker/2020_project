import requests, bs4
import xlwt
import time as t

xt = xlwt.Workbook()
xs = xt.add_sheet('data')

page=['bkstz.htm','/bkstz/8.htm','/bkstz/7.htm','/bkstz/6.htm','/bkstz/5.htm','/bkstz/4.htm','/bkstz/3.htm','/bkstz/2.htm','/bkstz/1.htm']
list_pages=[]
list_title=[]
s = 'http://ssdut.dlut.edu.cn'
url = "http://ssdut.dlut.edu.cn/index/"
for p in page:
    urlt = url+p
    res = requests.get(urlt)
    res.encoding = res.apparent_encoding
    doc = bs4.BeautifulSoup(res.text, 'html.parser')
    listp = doc.find_all('a',attrs={'class':"c56628"})
    for i in listp:
        list_title.append(i['title'])
        if '/' in p:
            list_pages.append(s+i['href'][5:])
        else:
            list_pages.append(s+i['href'][2:])

n = 0
for lp in list_pages:
    res = requests.get(lp)
    res.encoding = res.apparent_encoding
    doc = bs4.BeautifulSoup(res.text, 'html.parser')

    # 通知标题
    notice_title = list_title[n]

    getChicks = str(doc.select('.mt_10.mb_10.f13.lh_15per script')[0]).replace(' ', '').split(')')[0].split(',')
    resulturl = 'http://ssdut.dlut.edu.cn/system/resource/code/news/click/dynclicks.jsp?clickid={}&owner={}&clicktype=wbnews'.format(getChicks[2], getChicks[1])
    count = bs4.BeautifulSoup(requests.get(resulturl).text, 'html.parser')

    # 通知发布时间 及 点击量
    time_c = "".join(doc.find_all('div', attrs={'class': "mt_10 mb_10 f13 lh_15per", 'align': "center"})[0].text.split()).replace(
        '[]', count.text).split('点击：')

    time = time_c[0]
    chicks_num = time_c[1]

    # 通知正文
    notice_context = ''
    for i in doc.select('.v_news_content p'):
        notice_context = notice_context + i.text
    notice_context = "".join(notice_context.split())


    xs.write(n, 0, notice_title)
    xs.write(n, 1, time)
    xs.write(n, 2, chicks_num)
    xs.write(n, 3, notice_context)

    n += 1
    print('正在获取第'+str(n)+'页')
    t.sleep(5)


xt.save('G:/data_2.xls')


