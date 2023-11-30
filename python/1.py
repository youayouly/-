# 1#读取文件的方法
# def readfile(filename):
#     file_object = open(filename, 'r', encoding='UTF-8')
#     try:
#         all_text = file_object.read()
#     finally:
#         file_object.close()
#     return all_text

# from bs4 import BeautifulSoup

# html_str = readfile("test.html")
# soup = BeautifulSoup(html_str, 'html.parser')
# # print(html_str)
# # A=soup.body.div
# A=soup.head.contents
# for a in A:
#     #转义字符repr
#     print(repr(a))

# B=soup.head.children
# for b in B:
#     print(repr(b))
# print("*"*10)

# print(soup.title.string)
# E=soup.body.strings
# for e in E:
#     print(e)


# F=soup.body.stripped_strings
# for f in F:
#     print(f)

# G=soup.h1
# print(G.parents)
# for g in G:
#     print(g)

# #获取前后兄弟
# #previous_sibling
# #previous_siblings

# H=soup.h1.previous_siblings
# print(H)
# for h in H:
#     print(repr(h))

#读取文件的方法
def readfile(filename):
    file_object = open(filename, 'r', encoding='UTF-8')
    try:
        all_text = file_object.read()
    finally:
        file_object.close()
    return all_text
 # 将字符串写进文件中，参数分别是文件名和内容
def writefile(file_name,content_str):
    with open(file_name, "w",encoding='utf-8', ) as f:
        f.write(content_str)
        f.close

import requests
from bs4 import BeautifulSoup

h = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/68.0.3440.106 Safari/537.36'
     }
alltext=""
for i in range(0,10):
    d = {"start":25*i,"filter":""}
    # r = requests.get("https://movie.douban.com/top250",headers=h,params=d)
    r = requests.request("POST","https://movie.douban.com/top250", headers=h, data=d)
    alltext+=r.text
print("URL:",r.request.url)
writefile("a.txt",alltext)

html_str=readfile("a.txt")
soup = BeautifulSoup(html_str, 'html.parser')

namelist=[]
scorelist=[]

nameNode=soup.find_all("span",class_="title")
for n in nameNode:
    name=n.string.strip()#移除前后空格
    print(name)
    if(name[0]=="/"):
        continue
    namelist.append(name)
print(namelist)

scoreNode=soup.find_all("span",class_="rating_num")
for n in scoreNode:
    scorelist.append(n.string)
print(scorelist)

import urllib.request
imgNode=soup.find_all("img")
for n in imgNode:
    print(n)
    print(n["alt"])
    urllib.request.urlretrieve(n["src"],'imgs/%s.jpg' % n["alt"])
