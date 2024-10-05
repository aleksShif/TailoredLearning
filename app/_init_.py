# make sure to pip install flask first
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello(): 
    return "Hello, World!"

