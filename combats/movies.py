import requests
from fake_useragent import UserAgent
import time
from bs4 import BeautifulSoup
import re
import pandas as pd


def get_headers():
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }
    return headers


# 请求页面数据
def get_page(url):
    headers = get_headers()
    # noinspection PyBroadException
    try:
        res = requests.get(url=url, headers=headers)
        if res.status_code == 200:
            # print(res.text)
            return res.text
        else:
            return None
    except Exception:
        return None


def to_list(content):
    contents = []
    for c in content:
        contents.append(c.text)
    return contents


# 解析页面数据
def parse_page(text):
    # 实际上这里完全可以用正则表达式去弄，因为很直接，就像洗澡直接脱光
    # 用Xpath和BeautifulSoup也可以，只不过需要多脱一次才能脱光

    # 代码可以复用
    soup = BeautifulSoup(text, "lxml")
    # 排名
    # 用BeautifulSoup比较简单
    rank = soup.find_all("em")
    ranks = to_list(rank)
    # print(len(ranks)) == 25

    # 电影名字
    # 用正则表达式可以匹配到想要的标题
    name_re = '<span class="title">(\\w*?)</span>'
    names = re.findall(name_re, text)
    # print(len(names)) == 25

    # 链接
    link_re = '<a href="(.*?)" class="">'
    links = re.findall(link_re, text)
    # print(len(links)) == 25

    # 名言
    # 正则表达式和BeautifulSoup都可以
    # 正则表达式
    # lyric_re = '<span class="inq">(.*?)</span>'
    # lyrics = re.findall(lyric_re, text)
    # BeautifulSoup
    lyric = soup.find_all("span", class_="inq")
    lyrics = to_list(lyric)
    # print(len(lyrics)) == 25

    data = {
        'Rank': ranks,
        'Name': names,
        'Lyric': lyrics,
        'Link': links
    }
    return data


# 将数据写入文件
def to_file(data):
    if data is not None:
        df = pd.DataFrame(data=data, index=data['Rank'])
        df.to_csv('Douban_movies.csv')
        print('成功将数据写入csv文件')
    else:
        print('传入数据为空，没有写入csv文件')


# main函数，负责调度爬虫程序
def main(offset):
    url = f'https://movie.douban.com/top250?start={offset}'
    # 调用函数进行页面的爬取
    html = get_page(url)
    if html:
        # 解析页面数据
        data = parse_page(html)

        # 写入数据
        to_file(data)


if __name__ == '__main__':
    for i in range(1):
        main(offset=i * 25)
        time.sleep(2)
