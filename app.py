from flask import Flask, render_template, request, session

app = Flask(__name__)

app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
app.debug = True

@app.route('/')
def hello():
    return render_template('login.pug')

if __name__ == "__main__":
    app.run()

@app.route('/info/<number>')
def info(number):
    return 'number is %s' % number

@app.route('/login', methods = ['POST'])
def login():
    if request.method == 'POST':
        userId = request.form['id']
        pw = request.form['pw']

        if len(userId) == 0 or len(pw) == 0 :
            return userId + ', ' + pw + ' 로그인 정보를 제대로 입력하지 않았습니다.'

        session['logFlag'] = true
        session['userId'] = userId
        return session['userId']+'님 환영합니다.'
    else : 
        return '잘못된 접근입니다.'
app.secret_key = 'sample_secret_key'
