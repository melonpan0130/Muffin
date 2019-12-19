from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '1234'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:''@localhost/muffin"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
app.debug = True

db = SQLAlchemy(app)

class users(db.Model):
    userid = db.Column("userid", db.String(255), primary_key=True, unique = True)
    pw = db.Column("pw", db.String(255))
    name = db.Column("name", db.String(255))

    def __init__(self, userid, pw, name) :
        self.userid = userid
        self.pw = pw
        self.name = name

@app.route('/')
def home():
    if 'userId' in session :
        return render_template('index.pug', userId = session['userId'])
    return render_template('index.pug')

if __name__ == "__main__":
    # db.create_all()
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


@app.route('/logout')
def logout():
    session.pop('userId', None)
    return redirect('/')

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST' :
        # insert user data into connected DB
        return '<p>Joined</p>'
    else :
        return render_template('join.pug')