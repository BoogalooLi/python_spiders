from bs4 import BeautifulSoup
import requests
import pandas as pd

'''
url = https://www.lmoneky.com/t
content: titles, authors, links, times
tool: python, requests, bs4, pandas
'''
# 1.url & headers
url = 'https://www.lmonkey.com/t'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0'
}

# 2.发送请求
res = requests.get(url=url, headers=headers)

# 3.判断请求是否成功，并获取请求的源代码
if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'lxml')
    # 获取文章中所有的文章
    # lists可循环
    # 4.解析数据
    lists = soup.find_all('div', class_="list-group-item list-group-item-action p-06")
    title = []
    url = []
    author = []
    time = []
    for i in lists:
        # 看网页源码再进一步确定这里怎么弄，split要好好使用
        # print(i.text.split('\n')[0])
        j = i.find('div', class_="topic_title")
        if j:
            title.append(j.text.split('\n')[0])
            url.append(i.a['href'])
            author.append(i.strong.a.text)
            time.append(i.span['title'])

    # 5.写入数据
    df = pd.DataFrame({
        '标题': title,
        '作者': author,
        '时间': time,
        '链接': url
    })
    data = pd.HDFStore('data.h5', 'w')
    df.to_hdf('data.h5', key='yq')
    data.close()

    # 读取数据
    store = pd.HDFStore('data.h5', mode='r')
    temp = pd.read_hdf('data.h5')
    print(temp)

    store.close()