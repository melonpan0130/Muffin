from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
app.debug = True

@app.route('/')
def home():
    return render_template('index.pug', userId = session['userId'])

if __name__ == "__main__":
    app.run()

@app.route('/info/<number>')
def info(number):
    return 'number is %s' % number

@app.route('/login', methods = ['GET'])
def login():
    return render_template('login.pug')

@app.route('/login', methods = ['POST'])
def loginProc():
    if request.method == 'POST':
        userId = request.form['id']
        pw = request.form['pw']

        if len(userId) == 0 or len(pw) == 0 :
            return userId + ', ' + pw + ' 로그인 정보를 제대로 입력하지 않았습니다.'

        session['logFlag'] = 'true'
        session['userId'] = userId
        return redirect('/')
    else : 
        return '잘못된 접근입니다.'
app.secret_key = 'sample_secret_key'


@app.route('/logout')
def logout():
    session['logFlag'] = 'false'
    session['userId'] = ''
    return redirect('/')