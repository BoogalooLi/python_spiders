import requests
from fake_useragent import UserAgent

url = 'https://httpbin.org/get'
ua = UserAgent()

headers = {
    'User-Agent': ua.random
}

# 定义代理，可能需要个ip池
proxies = {
    'http': '124.167.232.123:8080',
    'https': '124.167.232.123:8080'
}

try:
    res = requests.get(url=url, headers=headers, proxies=proxies, timeout=5)

    if res.status_code == 200:
        data = res.json()
        print(data)
        print(data['origin'].split(','))
except requests.exceptions.ConnectTimeout:
    print('请求失败')
except requests.exceptions.InvalidURL:
    print('请求失败')
