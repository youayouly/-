from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def test():
    u = {'name': '张三', 'age': 20}
    return render_template('login.html')

@app.route('/login_post', methods=['POST'])
def logintest():
    name=request.form.get['username']
    pwd=request.form.get['password']
    if name == 'admin' and pwd == '123':
        return "登录成功"
    else:
        return render_template('login.html')    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8085, debug=True)
