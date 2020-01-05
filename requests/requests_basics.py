import requests

# 定义请求的url
url = 'http://www.baidu.com'

# 发起get请求
res = requests.get(url)
# res = requests.get(url=url)

# 获取相应结果
print(res)  # <Response [200]>返回一个对象,__str__触发
print(res.content)  # b'...' 二进制的文本流

# 下面两个结果一样，所以直接用text就可以了
print(res.text)  # 获取响应的内容
print(res.content.decode('utf-8'))  # 把二进制的文本流转换成utf-8文本

# 响应头信息
# {
# 'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform',
# 'Connection': 'keep-alive',
# 'Content-Encoding': 'gzip',
# 'Content-Type': 'text/html',
# 'Date': 'Sun, 29 Dec 2019 03:05:52 GMT',
# 'Last-Modified': 'Mon, 23 Jan 2017 13:27:52 GMT',
# 'Pragma': 'no-cache',
# 'Server': 'bfe/1.0.8.18',
# 'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/',
# 'Transfer-Encoding': 'chunked'
# }
print(res.headers)

print(res.status_code)  # 状态码 200 404
print(res.url)  # 请求的url

# 请求头信息
# {
# 'User-Agent': 'python-requests/2.22.0',
# 'Accept-Encoding': 'gzip, deflate',
# 'Accept': '*/*',
# 'Connection': 'keep-alive'
# }
print(res.request.headers)
