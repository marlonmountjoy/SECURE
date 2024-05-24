import sqlite3

# Create a database connection
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create a table and insert data
cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
cursor.execute('INSERT INTO users (username, password) VALUES ("admin", "adminpassword")')
cursor.execute('INSERT INTO users (username, password) VALUES ("user", "userpassword")')
conn.commit()
conn.close()