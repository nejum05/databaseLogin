from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Connect to Cloud SQL MySQL (replace with your DB config)
def get_db_connection():
    return mysql.connector.connect(
        host='sql12.freesqldatabase.com',
        user='sql12776900',
        password='bl1wU4HfJf',
        database='sql12776900'
    )

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_user():
    username = request.form['username']
    password = request.form['password']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if user:
        return render_template('success.html', username=username)
    else:
        return "Login Failed. Invalid credentials."

if __name__ == '__main__':
    app.run(debug=True)
