# make sure to pip install flask first
from flask import Flask, request, session, redirect, render_template
import sys
import db 

app = Flask(__name__)
app.secret_key = "HI"
db.db_table_inits()

@app.route('/', methods=['GET', 'POST'])
def home(): 
    if 'username' in session:
        return render_template('homepage.html', username=session["username"])
    return render_template('homepage.html') 

@app.route('/signup', methods=['GET', 'POST'])
def signup(): 
    if 'username' in session: 
        return redirect('/')
    return render_template('signup.html')

@app.route('/login', methods=['GET'])
def login():
    if 'username' in session: 
        if not db.check_user_exists(session['username']): 
            print('error passed', file=sys.stderr)
            return redirect('/logout')
        return redirect('/')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')

@app.route('/auth/login', methods=['GET', 'POST'])
def authorize_login():
    if request.method != 'POST':
        return redirect('/')
    user = request.form['username']
    password = request.form['password']

    if not db.verify_login(user, password):
        return render_template('login.html', status='error')

    session['username'] = user
    return redirect('/')

@app.route('/auth/signup', methods=['GET', 'POST'])
def authorize_signup():
    if request.method != 'POST':
        return redirect('/')
    
    user = request.form['username']
    password = request.form['password']

    if db.check_user_exists(user):
        return render_template("signup.html", error="user_exists")
    
    if password != request.form['confirmation']:
        return render_template("signup.html", error="unmatched_pass")
    
    db.create_user(user, password)
    session['username'] = user
    return redirect('/')
