import re
import requests
import pandas as pd

url = 'https://www.lmonkey.com/ask'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0'
}

res = requests.get(url=url, headers=headers)

if res.status_code == 200:
    # I/O
    # with open('./re.html', 'w') as fp:
    #     fp.write(res.text)

    html = res.text
    title_re = '<div class="topic_title mb-0 lh-180 ml-n2">(.*?)<small'
    author_re = '<strong>(.*?)</strong>'
    date_re = '<span data-toggle="tooltip" data-placement="top" title="(.*?)">'
    # 这里需要使用两个\的原因是escape sequence的问题，和C++一样
    url_re = '<a href="(https://www.lmonkey.com/ask/\\d+)" target="_blank">'

    title = re.findall(title_re, html)
    author = re.findall(author_re, html)
    date = re.findall(date_re, html)
    url = re.findall(url_re, html)

    # print(title)
    # print(len(title))
    # print(author)
    # print(len(author))
    # print(date)
    # print(len(date))
    # print(url)
    # print(len(url))

    df = pd.DataFrame({
        '标题': title,
        '作者': author,
        '时间': date,
        '链接': url
    })
    store = pd.HDFStore('data.h5', mode='w')
    df.to_hdf('data.h5', key='ylrc')
    store.close()

    data = pd.HDFStore('data.h5', mode='r')
    temp = pd.read_hdf('data.h5')
    print(temp)
    data.close()


