import requests

# 定义请求的url
url = 'https://fanyi.baidu.com/sug'

# 定义请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0'
}
# 发送的数据
# string = input()
data = {'kw': '你好'}

# 发送请求
res = requests.post(url=url, headers=headers, data=data)

# 接收返回的数据, json格式
code = res.status_code
if code == 200:
    print('请求成功')
    data = res.json()
    if data['errno'] == 0:
        print('响应成功')
        k = data['data'][0]['k']
        v = data['data'][0]['v'].split(';')[-2]
        print(k, '==', v)
