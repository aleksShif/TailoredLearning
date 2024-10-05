import sqlite3

DB_FILE = "data.db"

db = None

def db_connect():
    global db
    db = sqlite3.connect(DB_FILE)
    return db.cursor()

def db_close():
    db.commit()
    db.close()

def db_table_inits(): 
    # Creates users table if it doesn't exist
    c = db_connect()
    c.execute("CREATE TABLE IF NOT EXISTS users (username text, password text)")
    db_close()

def create_user(username, password):
    c = db_connect()
    c.execute('INSERT INTO users values (?,?)', (username, password))
    db.close()

def check_user_exists(username): 
    c = db_connect()
    c.execute('SELECT username FROM users WHERE username=?', [username])
    user = c.fetchone() 
    db_close()
    return bool(user)