# 半成品
import requests
from lxml import etree
from fake_useragent import UserAgent
import time


def get_links():
    url = 'https://www.kuaidaili.com/free/inha/'
    data = []
    for i in range(1, 3):
        link = f'{url}{i}/'
        data.append(link)
    return data


def get_headers():
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }
    return headers


def parse_html():
    urls = get_links()
    print(urls)
    headers = get_headers()
    proxies = []
    for url in urls:
        res = requests.get(url=url, headers=headers)
        if res.status_code == 200:
            content = res.content.decode('utf-8')
            html = etree.HTML(content)
            ip = html.xpath('//td[1]/text()')
            port = html.xpath('//td[2]/text()')
            proxies.append(list(zip(ip, port)))
        else:
            print('请求错误， 错误代码为', res.status_code)
    time.sleep(2)
    return proxies



