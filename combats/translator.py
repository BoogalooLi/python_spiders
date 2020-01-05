import requests

'''
url = http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule
method: post
'''


def translate(kw):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {
        'i': kw,
        'doctype': 'json'
    }

    res = requests.post(url=url, data=data)

    code = res.status_code

    if code == 200:
        # 这个时候用json解析比较合适，因为返回的是json数据类型
        # print(res.json())
        res_data = res.json()
        if res_data['errorCode'] == 0:
            print('请求成功')
            print(res_data['translateResult'][0][0]['tgt'])
        else:
            print('请求失败')


message = """
欢迎使用BoogalooLi写的翻译小程序
输入q退出
希望你能喜欢
"""
print(message)

while True:
    word = input('请输入要翻译的内容：')
    if word == 'q':
        print('欢迎您下次使用')
        break
    translate(word)
