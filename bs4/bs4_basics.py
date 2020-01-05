from bs4 import BeautifulSoup
import lxml

text = """
<!DOCTYPE html>
<html lang="zh-CN">
<body>
    <meta charset="UTF-8">
    <title>
        学习猿地 - IT培训|Java培训|Python培训|ui设计培训|web前端培训|GO培训|PHP培训|成就自己的只需一套精品
    </title>
</body>
<body>
    <ul>
        <li><a href="/a/b/c/java/">java engineer</a></li>
        <li><a href="/a/b/c/python/">python engineer</a></li>
        <li><a href="/a/b/c/ai/">AI engineer</a></li>
        <li><a class="class_name">Class engineer</a></li>
        <li><a id="id">ID engineer</a></li>
    </ul>
</body>
</html>
"""

# 创建一个Beautifulsoup对象，建议手动指定解析器
soup = BeautifulSoup(text, 'lxml')

# 通过tag标签获取文档数据
r1 = soup.a
r2 = soup.title
r3 = soup.a['href']
r4 = soup.title.text
r5 = soup.a.parent.name
# print(r1)
# print(r2)
# print(r3)
# print(r4)
# print(r5)

# 通过搜索获取页面中的元素，find/find_all

r6 = soup.find('a')
r7 = soup.find_all('a')
# print(r6)
# print(r6.text)
# print(r6.get_text())
# print(r7)

# CSS选择器

# 通过标签选择元素
tag = soup.select('title')
# print(tag)

# 通过class类名获取元素
class_name = soup.select('.class_name')
# print(class_name)

# 通过ID名获取元素
ID = soup.select('#id')
# print(ID)

# 通过空格层级关系获取元素
family = soup.select('html body')
# print(family)

# 通过逗号，并列关系获取元素
comma = soup.select('a, title')
print(comma)
