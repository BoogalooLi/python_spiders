import requests

# 定义请求的url
# url = 'https://www.lmonkey.com'
url = 'https://www.xicidaili.com/nn'

# 定义请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0'
}

# 发起get请求
res = requests.get(url=url, headers=headers)


# 获取响应状态码
code = res.status_code

print(code)  # 503 服务器内部拒绝请求

# 响应成功后把响应的内容写入文件中
if code == 200:
    with open('./test.html', 'w') as fp:
        fp.write(res.text)
