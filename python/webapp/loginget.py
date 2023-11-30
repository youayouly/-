from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def test():
    u = {'name': '张三', 'age': 20}
    return render_template('loginget.html')

@app.route('/loginget', methods=['GET'])
def logintest():
    name=request.args.get['username']
    pwd=request.args.get['password']
    if name == 'admin' and pwd == '123':
        return "登录成功"
    else:
        return render_template('loginget.html')    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8085, debug=True)
