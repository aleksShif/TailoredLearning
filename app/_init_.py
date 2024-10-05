# make sure to pip install flask first
from flask import Flask, request, session, redirect, render_template
import db

app = Flask(__name__)
db.db_table_inits()

@app.route('/', methods=['GET', 'POST'])
def home(): 
    # if 'username' not in session: 
    #     return redirect('/login')
    return render_template('homepage.html') 

@app.route('/login', methods=['GET'])
def login():
    # if 'username' in session: 
    #     if not db.check_user_exists(session['username']): 
    #         return redirect('/logout')
    #     return redirect('/')
    return render_template("login.html")
    