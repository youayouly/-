# # from bs4 import BeautifulSoup

# # html_str = "<a href='web2_html' class='link'>链接</a> <p><span>你好</span></p>"
# # soup = BeautifulSoup(html_str, 'html.parser')
# # print(soup, type(soup))

# # tag1 = soup.a
# # print(tag1, type(tag1))
# # print(tag1.attrs, type(tag1.attrs))

# # tag2 = soup.a
# # print(tag2, type(tag2))

# # d=tag1.attrs
# # print(d['href'])
# # print(d['class'][0])#class是多值属性
# # print(tag1.string,type(tag1.string))#获得节点中中的叶子节点

# # tag2=soup.p.span
# # print(tag2.string)

# #读取文件的方法
# def readfile(filename):
#     file_object = open(filename, 'r', encoding='UTF-8')
#     try:
#         all_text = file_object.read()
#     finally:
#         file_object.close()
#     return all_text

# from bs4 import BeautifulSoup

# html_str=readfile("test.html")
# print(html_str)
# soup=BeautifulSoup(html_str,'html.parser')
# # A=soup.find_all('a')

# # # print(A,type(A))

# # for a in A:
# #     print(a.string)

# # A=soup.find_all('a',limit=1)
# # for a in A:
# #     print(a.string)

# #通过属性值作为条件过滤
# #正则表达是 找到标签有t的节点
# import re

# #放空不设条件
# A=soup.find_all(hreg=re.compile("web1"))
# for a in A:
#     print(a.name)

# A=soup.find_all(recursive=False)
# for a in A:
#     print(a.name)

# #查找内容包括宁浩的h1标签 

#百度一下：web1.html
#谷歌一下：web2.html


from bs4 import BeautifulSoup
import re

html_str=readfile("test.html")
soup = BeautifulSoup(html_str, 'html.parser')


all_a_tags = soup.find_all('a')

for a_tag in all_a_tags:
    link_text = a_tag.text  # 获取 <a> 标签中的文本内容
    link_href = a_tag.get('href')  # 获取 <a> 标签的 href 属性值
    print(f"#{link_text}: {link_href}")

