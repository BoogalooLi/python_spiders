from lxml import etree

# 读取一个html文件并解析
html = etree.parse('./example.html', etree.HTMLParser())
# print(html)

# 提取数据
r1 = html.xpath('/html/body/ul/li/a/text()')
print(r1)

# 获取页面中所有的li里面的数据
r2 = html.xpath('//li/a/text()')
print(r2)

# 获取制定标签里面的li数据
r3 = html.xpath('//div[@class="teacher"]//li/a/text()')
# 另一种写法，结果是一样的
# r3 = html.xpath('//div[@class="teacher"]/ul/li/a/text()')
print(r3)

r4 = html.xpath('//div[@class="teacher"]//li/a/@*')
print(r4)

print(*zip(r3, r4))
print(list(zip(r3, r4)))
