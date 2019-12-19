from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
app.debug = True

@app.before_first_request
def before_first_request():
    session['userId'] = ''

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
            return '(' + userId + ', ' + pw + ') Please write on your ID or Password.'

        session['userId'] = userId
        return redirect('/')
    else : 
        return 'Somethings wrong.'
app.secret_key = 'sample_secret_key'


@app.route('/logout')
def logout():
    session['userId'] = ''
    return redirect('/')

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST' :
        # insert user data into connected DB
        return '<p>Joined</p>'
    else :
        return render_template('join.pug')
