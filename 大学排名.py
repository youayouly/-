import urllib.request

import requests
from bs4 import BeautifulSoup


def readfile(filename):
    file_object = open(filename, 'r', encoding='UTF-8')
    try:
        all_text = file_object.read()
    finally:
        file_object.close()
    return all_text


# 将字符串写进文件中，参数分别是文件名和内容
def writefile(file_name, content_str):
    with open(file_name, "w", encoding='utf-8', ) as f:
        f.write(content_str)
        f.close


if __name__ == "__main__":
    url = "https://www.shanghairanking.cn/rankings/bcur/2023"
    h = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/68.0.3440.106 Safari/537.36'
         }
    response = requests.get(url, headers=h)
    html_code = response.content.decode("utf-8")
    writefile("a.txt", html_code)
    html_str = readfile("a.txt")
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_str, 'html.parser')
    # 查找大学排名数据
    names = soup.find_all('a', class_="name-cn")
    Names = []
    for name in names:
        Names.append(name.text.strip())
    tags = names = soup.find_all('p', class_="tags")
    Tags = []
    for tag in tags:
        Tags.append(tag.text.strip())
    tags = names = soup.find_all('td')
    text = []
    Rank = []
    Region = []
    Type = []
    Totcal_score = []
    Cengci = []
    for str in tags:
        text.append(str.text.strip())
    i = 0
    for i in range(0, len(text)):
        if i % 6 == 1:
            continue
        else:
            if i % 6 == 0:
                Rank.append(text[i])
            elif i % 6 == 2:
                Region.append(text[i])
            elif i % 6 == 3:
                Type.append(text[i])
            elif i % 6 == 4:
                Totcal_score.append(text[i])
            else:
                Cengci.append(text[i])
    i = 0
    for i in range(0, len(Names)):
        print("排名：{0}，名字：{1}，标签：{2}，地区：{3}，类型：{4}，总分：{5}，办学层次：{6}".format(Rank[i], Names[i], Tags[i],
                                                                                          Region[i], Type[i],
                                                                                          Totcal_score[i], Cengci[i]))
    icon_img = soup.find_all('img', class_='univ-logo')
    for icon in icon_img:
        urllib.request.urlretrieve(icon['src'], 'university/%s.jpg' % icon['alt'])
    print("End")
