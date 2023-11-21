from bs4 import BeautifulSoup

html_str = "<a href='web2_html' class='link'>链接</a> <p><span>你好</span></p>"
soup = BeautifulSoup(html_str, 'html.parser')
print(soup, type(soup))

tag1 = soup.a
print(tag1, type(tag1))
print(tag1.attrs, type(tag1.attrs))

tag2 = soup.a
print(tag2, type(tag2))

d=tag1.attrs
print(d['href'])
print(d['class'][0])#class是多值属性
print(tag1.string,type(tag1.string))#获得节点中中的叶子节点

tag2=soup.p.span
print(tag2.string)