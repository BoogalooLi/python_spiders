import requests
import pandas as pd
from lxml import etree

# 请求的地址猿著
url = 'https://www.lmonkey.com/essence'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0'
}

# 发送请求
res = requests.get(url=url, headers=headers)
if res.status_code == 200:
    # 请求的内容写入文件
    with open('./yz.html', 'w') as fp:
        fp.write(res.text)

# 解析数据
html = etree.parse('./yz.html', etree.HTMLParser())

# 提取数据：文章标题，地址url，作者
author = html.xpath('//strong/a/text()')
title = html.xpath('//div[contains(@class, "topic_title mb-0")]/text()')
title_url = html.xpath('//div[contains(@class, "flex-fill  col-12")]/a[@target="_blank"]/@href')

# 整理数据
df = pd.DataFrame({'标题': title, '作者': author, '链接': title_url})

# 写入数据，用pandas的hdf函数
store = pd.HDFStore('data.h5', mode='w')
df.to_hdf('data.h5', key='yz')
store.close()

# 读取数据
store = pd.HDFStore('data.h5', mode='r')
temp = pd.read_hdf('data.h5')
print(temp)

store.close()
