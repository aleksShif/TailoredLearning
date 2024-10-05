# make sure to pip install flask first
from flask import Flask, request, session, redirect, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home(): 
    # if 'username' not in session: 
    #     return redirect('/login')
    return render_template('homepage.html') 

