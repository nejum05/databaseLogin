from flask import Flask, request, render_template_string
import mysql.connector

app = Flask(__name__)

DB_CONFIG = {
    'host': 'sql12.freesqldatabase.com',
    'user': 'sql12776900',
    'password': 'bl1wU4HfJf',
    'database': 'sql12776900',
    'port': 3306
}

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        uname = request.form["username"]
        pwd = request.form["password"]

        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (uname, pwd))
            result = cursor.fetchone()
            if result:
                message = "Login Successful!"
            else:
                message = "Invalid Credentials"
        except Exception as e:
            message = "Error: " + str(e)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    return render_template_string("""
    <h2>User Login</h2>
    <form method="POST">
        Username: <input name="username"><br>
        Password: <input name="password" type="password"><br>
        <input type="submit" value="Login">
    </form>
    <p>{{ message }}</p>
    """, message=message)

if _name_ == "_main_":
    app.run(debug=True)