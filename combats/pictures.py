import requests
import os


# 进行数据爬取
def get_pages(kw, num):
    # 请求的url
    url = 'https://image.baidu.com/search/acjson'
    # 循环页码和请求参数
    params = []
    for i in range(30, 30 * (num + 1), 30):
        params.append(
            {
                'tn': 'resultjson_com',
                'ipn': 'rj',
                'ct': '201326592',
                'is': ' ',
                'fp': 'result',
                'queryWord': kw,
                'cl': '2',
                'lm': '-1',
                'ie': 'utf-8',
                'oe': 'utf-8',
                'adpicid': ' ',
                'st': ' 1',
                'z': ' ',
                'ic': ' ',
                'hd': ' ',
                'latest': ' ',
                'copyright': ' ',
                'word': kw,
                's': ' ',
                'se': ' ',
                'tab': ' ',
                'width': ' ',
                'height': ' ',
                'face': ' ',
                'istype': '2',
                'qc': ' ',
                'nc': ' 1',
                'fr': ' ',
                'expermode': ' ',
                'force': ' ',
                'cg': 'girl',
                'pn': i,
                'rn': '30',
                'gsm': ' ',
                '1578205514975': ' ',
            }
        )
    # 循环请求
    urls = []
    for i in params:
        # 向每一个url发起请求
        res = requests.get(url=url, params=i)
        data = res.json()['data']
        # 获取请求的数据，加入urls里面
        urls.append(data)
    return urls


def download_pic(data, pos):
    # 检测文件夹是否存在
    if not os.path.exists(pos):
        os.mkdir(pos)

    # 循环下载图片数据
    name = 1
    for d in data:
        for i in d:
            if i.get('thumbURL') is not None:
                print(f'下载图片{i.get("thumbURL")}')
                # 向图片地址发起请求
                img_res = requests.get(i.get('thumbURL'))
                open(f'{pos}/{name}.jpg', 'wb').write(img_res.content)
                name += 1


# 获取用户输入信息
keyword = input('请输入搜索图片的关键字：')
# 指定关键字和页数
data_list = get_pages(keyword, 1)
# 保存数据，指定图片路径
download_pic(data_list, './baidu_pics')
