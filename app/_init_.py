# make sure to pip install flask first
from flask import Flask, request, session, redirect, render_template, url_for
from flask_socketio import SocketIO, send, join_room, leave_room
import uuid
import sys
import db 

app = Flask(__name__)
socketio = SocketIO(app)
app.secret_key = "HI"
db.db_table_inits()

rooms = {}
1
@app.route('/create_room', methods=['POST'])
def create_room():
    room_id = str(uuid.uuid4())
    rooms[room_id] = []
    return redirect(url_for('join_room_view', room_id=room_id))

@app.route('/room/<room_id>')
def join_room_view(room_id):
    if room_id not in rooms:
        return "Room not found", 404
    return render_template('room.html', room_id=room_id)

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(f'{username} has entered the room.', to=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(f'{username} has left the room.', to=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)

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
            return redirect('/logout')
        return redirect('/')
    return render_template('login.html')

@app.route('/quiz', methods=['GET'])
def quizroom():
    if 'username' in session:
        return render_template('quizroom.html', username=session["username"])
    return render_template('quizroom.html')  


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
        return render_template('login.html')

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
