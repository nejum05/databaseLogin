from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# ✅ Use environment variables in production (not hardcoded)
DB_CONFIG = {
    'host': 'sql12.freesqldatabase.com',
    'user': 'sql12780373',
    'password': 'plR7hiKCmt',
    'database': 'sql12780373'
}

@app.route('/', methods=['GET', 'POST'])
def login():
    msg = ''
    username = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM login WHERE username=%s AND password=%s", (username, password))
            result = cursor.fetchone()
            if result:
                return render_template("success.html", username=username)
            else:
                msg = 'Invalid Credentials.'
        except Exception as e:
            msg = f'Error: {e}'
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    return render_template("login.html", msg=msg, username=username)

if __name__ == "__main__":  # ✅ Fix typo from '_main_' to '__main__'
    app.run(debug=True)
