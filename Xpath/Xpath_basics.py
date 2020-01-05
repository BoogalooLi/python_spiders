from lxml import etree

text = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>
        学习猿地 - IT培训|Java培训|Python培训|ui设计培训|web前端培训|GO培训|PHP培训|成就自己的只需一套精品
    </title>
</head>
<body>
    <ul>
        <li><a href="/a/b/c/java/">java engineer</a></li>
        <li><a href="/a/b/c/python/">python engineer</a></li>
        <li><a href="/a/b/c/ai/">AI engineer</a></li>
    </ul>
</body>
</html>
'''
# 使用etree解析html字符串
html = etree.HTML(text)
# print(html)
# 提取数据
# ['java engineer', 'python engineer', 'AI engineer']
r1 = html.xpath('/html/body/ul/li/a/text()')
print(r1)

# ['java engineer']
r2 = html.xpath('/html/body/ul/li[1]/a/text()')
print(r2)

