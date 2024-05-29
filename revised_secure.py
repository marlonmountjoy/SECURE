from flask import Flask, request, render_template_string, redirect, url_for
from markupsafe import escape

app = Flask(__name__)

# Dummy database of users
USERS = {
    'admin': 'adminpassword',
    'user': 'userpassword'
}

@app.route('/')
def home():
    # Home route that provides instructions for login
    return "Welcome to the vulnerable app! Go to /login?username=USERNAME&password=PASSWORD to login!"

@app.route('/login')
def login():
    # Extracting username and password from URL parameters
    username = request.args.get('username')
    password = request.args.get('password')

    # Sanitizing input to prevent injection attacks
    username = escape(username)
    password = escape(password)
    
    # Vulnerable SQL query simulation (Note: This is not actually running a SQL query, just simulating)
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    response = "Login failed!"
    # Simulated user authentication
    if username in USERS and USERS[username] == password:
        response = f"Successfully logged in as {username}!"
    
    # Rendering the response and the simulated executed query
    return render_template_string('<h2>' + response + '</h2><br>Executed query: ' + query)

if __name__ == '__main__':
    # Running the Flask app in debug mode
    app.run(debug=True)
