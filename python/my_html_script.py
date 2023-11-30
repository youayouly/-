# Rename your script from html.py to my_html_script.py
from flask import Flask

# 创建一个flask实例
app = Flask(__name__)

# 设置路由
@app.route('/')
def test():
    return "hello flask"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8085, debug=True)
