import sqlite3
from flask import Flask, request, render_template_string

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn

@app.route('/')
def home():
    return "Welcome to the vulnerable app! Go to /login?username=USERNAME&password=PASSWORD to login!"

@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    conn = get_db_connection()
    cursor = conn.cursor()

    # Vulnerable SQL query
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    try:
        cursor.execute(query)
        result = cursor.fetchone()
        response = "Login failed!"
        if result:
            response = f"Successfully logged in as {username}!"
    except Exception as e:
        response = str(e)
    
    conn.close()
    return render_template_string('<h2>' + response + '</h2><br>Executed query: ' + query)

if __name__ == '__main__':
    app.run(debug=True)
