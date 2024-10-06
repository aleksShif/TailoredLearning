#testing file for azure sql db
import pyodbc #pip install pyodbc
from passwords import az_server, az_database, az_username, az_password

azdb = None

# Azure SQL Database connection details
server = az_server
database = az_database
username = az_username
password = az_password
driver = '{ODBC Driver 18 for SQL Server}' # please install x64 from #https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16

def azdb_connect():
    global azdb
    azdb = pyodbc.connect(
        f'DRIVER={driver};'
        f'SERVER={server};'
        f'PORT=1433;'
        f'DATABASE={database};'
        f'UID={username};'
        f'PWD={password};'
        'Encrypt=yes;'
        'TrustServerCertificate=no;'
        'Connection Timeout=30;'
        )
    return azdb.cursor()

def create_table():
    conn = azdb_connect()
    cursor = conn.cursor()
    # Create table query
    create_table_query = """
    CREATE TABLE users (
        id INT PRIMARY KEY IDENTITY(1,1),
        username NVARCHAR(50),
        password NVARCHAR(50)
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()

def insert_dummy_data():
    conn = azdb_connect()
    cursor = conn.cursor()
    # Insert dummy data
    dummy_data = [
        ('user1', 'password1'),
        ('user2', 'password2'),
        ('user3', 'password3'),
        ('user4', 'password4'),
        ('user5', 'password5')
    ]
    cursor.executemany("INSERT INTO users (username, password) VALUES (?, ?)", dummy_data)
    conn.commit()
    conn.close()

def all_users_query():
    conn = azdb_connect()
    cursor = conn.cursor()
    # Query to get all users
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

def azdb_table_inits(): 
    # Creates users table if it doesn't exist
    cursor = azdb_connect()
    cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'users')
    BEGIN
        CREATE TABLE users (
            username NVARCHAR(50),
            password NVARCHAR(50)
        )
    END
    """)
    cursor.commit()
    cursor.close()
    azdb_close()

def check_user_exists(username): 
    cursor = azdb_connect()
    cursor.execute('SELECT username FROM users WHERE username=?', [username])
    user = cursor.fetchone() 
    azdb_close()
    return bool(user)

def verify_login(username, password):
    cursor = azdb_connect()
    cursor.execute('SELECT username,password FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()
    azdb_close()
    if user:
        return True
    return False

def create_user(username, password):
    cursor = azdb_connect()
    cursor.execute('INSERT INTO users values (?,?)', (username, password))
    azdb_close()

def azdb_close():
    azdb.commit()
    azdb.close()

# Run the create table function
if __name__ == "__main__":
    insert_dummy_data()
    users = all_users_query()
    for user in users:
        print(user)