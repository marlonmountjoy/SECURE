from flask import Flask, request, render_template_string, redirect, url_for
from markupsafe import escape

# Create a Flask application instance
app = Flask(__name__)

# Dummy database of users (In a real application, use a secure database)
USERS = {
    'admin': 'adminpassword',
    'user': 'userpassword'
}

@app.route('/')
def home():
    # Home route that provides instructions for login
    return "Welcome to the secure app! Go to /login to login!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Extracting username and password from form data
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Sanitizing input to prevent injection attacks
        username = escape(username)
        password = escape(password)
        
        # Simulated user authentication
        response = "Login failed!"
        if username in USERS and USERS[username] == password:
            response = f"Successfully logged in as {username}!"
        
        # Rendering the response
        return render_template_string('<h2>' + response + '</h2>')

    # If GET request, render the login form
    return render_template_string('''
        <form method="post" action="/login">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    ''')

if __name__ == '__main__':
    # Running the Flask app on a different port to avoid conflict
    app.run(debug=True, port=5001)
