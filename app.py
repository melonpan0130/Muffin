from flask import Flask, render_template, request, session, pypugjs
app = Flask(__name__)

@app.route('/')
def index():
    return pypugjs.register_filter("login.pug")
    # return render_template('login.html')

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
