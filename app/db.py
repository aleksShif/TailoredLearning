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
    c.execute("CREATE TABLE IF NOT EXISTS data_questions (questions text, answer1 text, answer2 text, answer3 text, answer4 text, correct text)")
    c.execute("CREATE TABLE IF NOT EXISTS env_questions (questions text, answer1 text, answer2 text, answer3 text, answer4 text, correct text)")
    c.execute("CREATE TABLE IF NOT EXISTS linearalg_questions (questions text, answer1 text, answer2 text, answer3 text, answer4 text, correct text)")
    c.execute("CREATE TABLE IF NOT EXISTS psych_questions (questions text, answer1 text, answer2 text, answer3 text, answer4 text, correct text)")
    db_close()
    
def create_user(username, password):
    c = db_connect()
    c.execute('INSERT INTO users values (?,?)', (username, password))
    db_close()

def check_user_exists(username): 
    c = db_connect()
    c.execute('SELECT username FROM users WHERE username=?', [username])
    user = c.fetchone() 
    db_close()
    return bool(user)

def verify_login(username, password):
    c = db_connect()
    c.execute('SELECT username,password FROM users WHERE username=? AND password=?', (username, password))
    user = c.fetchone()
    db_close()
    if user:
        return True
    return False

def add_data_question(questions, answer1, answer2, answer3, answer4, correct):
    c = db_connect()
    c.execute('INSERT INTO data_questions values (?, ?, ?, ?, ?, ?)',(questions, answer1, answer2, answer3, answer4, correct))
    db_close()

def add_env_question(questions, answer1, answer2, answer3, answer4, correct):
    c = db_connect()
    c.execute('INSERT INTO env_questions values (?, ?, ?, ?, ?, ?)',(questions, answer1, answer2, answer3, answer4, correct))
    db_close()

def add_linearalg_question(questions, answer1, answer2, answer3, answer4, correct):
    c = db_connect()
    c.execute('INSERT INTO linearalg_questions values (?, ?, ?, ?, ?, ?)',(questions, answer1, answer2, answer3, answer4, correct))
    db_close()

def add_psych_question(questions, answer1, answer2, answer3, answer4, correct):
    c = db_connect()
    c.execute('INSERT INTO psych_questions values (?, ?, ?, ?, ?, ?)',(questions, answer1, answer2, answer3, answer4, correct))
    db_close()

def get_data_questions():
    c = db_connect()
    result = c.execute("SELECT * FROM data_questions")
    rows = result.fetchall()
    questions = []
    for r in rows:
        questions.append(r[0])
        print(r[0])


def get_data_questionset(questions):
    c = db_connect()
    result = c.execute('SELECT * FROM data_questions WHERE questions=?', (questions))
    data_question = result.fetchall()
    db_close()
    return data_question

print(get_data_questions())