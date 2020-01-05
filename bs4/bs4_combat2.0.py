import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy as np


class Bs4Yq:
    # 定义属性
    # 1.url & headers
    url = 'https://www.lmonkey.com/t'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0'
    }

    # 存放数据
    html = None
    title = []
    link = []
    author = []
    time = []

    # 初始化方法
    def __init__(self):
        # 2.发送请求
        res = requests.get(url=self.url, headers=self.headers)
        if res.status_code == 200:
            print('请求成功')
            self.html = res.text
            if self.parse_data():
                print('解析数据成功')
                self.store_data()
        else:
            print('请求失败')

    # 解析数据
    def parse_data(self):
        try:
            soup = BeautifulSoup(self.html, 'lxml')
            # 获取文章中所有的文章
            # lists可循环
            # 4.解析数据
            lists = soup.find_all('div', class_="list-group-item list-group-item-action p-06")
            for i in lists:
                # 看网页源码再进一步确定这里怎么弄，split要好好使用
                # print(i.text.split('\n')[0])
                j = i.find('div', class_="topic_title")
                if j:
                    self.title.append(j.text.split('\n')[0])
                    self.link.append(i.a['href'])
                    self.author.append(i.strong.a.text)
                    self.time.append(i.span['title'])
            return True
        except Exception:
            return False

    # 存储数据
    def store_data(self):
        df = pd.DataFrame({
            '标题': self.title,
            '作者': self.author,
            '时间': self.time,
            '链接': self.url
        })
        data = pd.HDFStore('data.h5', 'w')
        df.to_hdf('data.h5', key='yq')
        data.close()
        print('存储数据成功')

    # 读取数据
    @staticmethod
    def read_data():
        store = pd.HDFStore('data.h5', mode='r')
        temp = pd.read_hdf('data.h5')
        print(temp)
        store.close()


obj = Bs4Yq()
obj.read_data()