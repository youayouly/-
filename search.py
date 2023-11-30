import requests
from bs4 import BeautifulSoup
import os
import urllib.request

def read_html(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        html_content = file.read()
    return html_content

def write_to_file(file_name, content):
    with open(file_name, "w", encoding='utf-8') as file:
        file.write(content)

if __name__ == "__main__":
    url = "https://www.shanghairanking.cn/rankings/bcur/2023"
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/68.0.3440.106 Safari/537.36'}
    
    response = requests.get(url, headers=headers)
    html_code = response.content.decode("utf-8")
    
    write_to_file("web_content.html", html_code)
    html_str = read_html("web_content.html")
    
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_str, 'html.parser')
    
    # 查找大学排名数据
    university_names = [name.text.strip() for name in soup.find_all('a', class_="name-cn")]
    tags = [tag.text.strip() for tag in soup.find_all('p', class_="tags")]
    table_cells = [cell.text.strip() for cell in soup.find_all('td')]
    
    # 新的循环部分
    ranks, regions, types, total_scores, cengci = [], [], [], [], []
    for i in range(0, len(table_cells), 6):
        ranks.append(table_cells[i])
        regions.append(table_cells[i + 2])
        types.append(table_cells[i + 3])
        total_scores.append(table_cells[i + 4])
        cengci.append(table_cells[i + 5])
    
    # 在桌面上创建 'images' 目录（如果不存在）
    output_directory = os.path.join(os.path.expanduser("~"), 'Desktop', 'images')
    os.makedirs(output_directory, exist_ok=True)
    
    with open("output.txt", "w", encoding='utf-8') as output_file:
        output_lines = [f"排名：{rank}，名字：{name}，标签：{tag}，地区：{region}，类型：{university_type}，总分：{total_score}，办学层次：{level}\n" 
                        for rank, name, tag, region, university_type, total_score, level in zip(ranks, university_names, tags, regions, types, total_scores, cengci)]
        output_file.writelines(output_lines)

    
    icon_images = soup.find_all('img', class_='univ-logo')
    for icon in icon_images:
        # 将图标保存到 'C:\Users\71091\Desktop\images' 目录
        output_path = os.path.join(output_directory, f"{icon['alt']}.jpg")
        urllib.request.urlretrieve(icon['src'], output_path)
    
    print("结束")
