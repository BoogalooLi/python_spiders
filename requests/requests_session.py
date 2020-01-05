import requests

# 需要请求的目标地址
# 人人字幕
# url = 'http://www.zmz2019.com/user/user'
url = 'https://www.lmonkey.com/'
# 登录请求的地址
# 人人字幕
# login_url = 'http://www.zmz2019.com/user/login/ajaxlogin'
login_url = 'https://www.lmonkey.com/login'
# 请求头
headers = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

# 如果需要爬虫主动记录cookies
# 那么在使用requests之前先调用session
# 并且使用session返回的对象发送请求即可
req = requests.session()

# 登录请求时的数据
# data需要chrome F12 network勾选preservelog
# 人人字幕data
# data = {
#     'account': '563797067@qq.com',
#     'password': 'lycLYC85302250',
#     'remember': '1',
#     'url_back': 'http://www.zmz2019.com/'
# }

# data = {
#     '_token': 'mHC4eTd5PTr4fNhWP9rtGhYxwBqlRPxiXaCM2SzK',
#     'username': '李彦辰',
#     'password': '123456789'
# }

# 发起登录请求
res = req.post(url=login_url, headers=headers, data=data)

# 判断状态
code = res.status_code
print(code)

if code == 200:
    # 发起新的请求，去获取目标数据
    res = req.get(url=url, headers=headers)
    with open('学习猿地.html', 'w') as fp:
        fp.write(res.text)
