from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def test():
    u = {'name': '张三', 'age': 20}
    return render_template('index.html', title='我的标题', user="张三", info=u)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8085, debug=True)
