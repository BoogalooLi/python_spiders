import requests
from lxml import etree


# 封装类，进行学习猿地的登录和订单的获取
class LMonkey:
    login_url = 'https://www.lmonkey.com/login'
    order_url = 'https://www.lmonkey.com/my/order'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0'
    }
    # 请求对象
    req = None
    # _token口令
    _token = ''
    # 订单号
    order_number = 0

    # 初始化方法
    def __init__(self):
        # 请求对象的初始化
        self.req = requests.session()
        if self.get_login():
            if self.post_login():
                self.get_order()

    # get 登录页面，获取_token
    def get_login(self):
        # 1 get请求 login页面，设置cookie，获取_token
        res = self.req.get(url=self.login_url, headers=self.headers)
        if res.status_code == 200:
            print('get登录页面请求成功')
            html = etree.HTML(res.text)
            self._token = html.xpath('//input[@name="_token"]/@value')[0]
            print('token获取成功')
            return True
        else:
            print('请求错误')

    # post 请求登录
    def post_login(self):
        name = input('用户名：')
        pwd = input('密码: ')

        data = {
            '_token': self._token,
            'username': name,
            'password': pwd
        }

        # 发起post请求，设置cookie
        res = self.req.post(url=self.login_url, headers=self.headers, data=data)

        if res.status_code == 200:
            print('登录成功')
            return True
            # 请求订单数据

    # get 请求账户数据 获取默认订单号
    def get_order(self):
        # 3 get请求 账户中心，获取默认订单号
        pass

        res = self.req.get(url=self.order_url, headers=self.headers)
        if res.status_code == 200:
            print('账户中心请求成功，正在解析数据')
            html = etree.HTML(res.text)
            r = html.xpath('//div[@class="avatar-content"]//small/text()')[0][5:]
            self.order_number = r
            print(self.order_number)


obj = LMonkey()