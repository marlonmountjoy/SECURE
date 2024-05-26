from flask import Flask, request, render_template_string

app = Flask(__name__)

# Dummy database of users
USERS = {
    'admin': 'adminpassword',
    'user': 'userpassword'
}

@app.route('/')
def home():
    return "Welcome to the vulnerable app! Go to /login?username=USERNAME&password=PASSWORD to login!"

@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    
    # Vulnerable SQL query simulation
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    response = "Login failed!"
    if username in USERS and USERS[username] == password:
        response = f"Successfully logged in as {username}!"
    
    # Simulating the execution of a SQL query and returning the result
    return render_template_string('<h2>' + response + '</h2><br>Executed query: ' + query)

if __name__ == '__main__':
    app.run(debug=True)
