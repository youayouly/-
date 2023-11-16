def writefile(file_name,content_str):
    with open(file_name,"w",encoding='utf-8')as f:
        f.write(content_str)
        f.close

def get_html_text(url):
    h={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    'AppleWebKit/537.36 (KHTML, like Gecko)'
    'Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}

    all=""
    for i in range(0,10):
        d={'start':i*25,'filter':""}
        r=requests.request("POST","https://movie.douban.com/top250",headers=h,params=d)
        all+=r.text

    return all




import requests
print("开始爬虫")
url="https://movie.douban.com/top250"
html_text=get_html_text(url)
writefile("a.txt",html_text)




# h={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
#     'AppleWebKit/537.36 (KHTML, like Gecko)'
#     'Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}

# url="https://httpbin.org/post"
# d={'user':"hhh",'pwd'="123"}
# r=requests.request("POST",url,headers=h,params=d)
# print(r.text)



# all=""
# for i in range(0,10):
#     d={'start':i*25,'filter':""}
#     r=requests.request("POST","https://movie.douban.com/top250",headers=h,params=d)
#     all+=r.text
   
# writefile("a.txt",all)
# print(r.status_code)
# print(r.text)

