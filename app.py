from flask import Flask, request, render_template_string
import pymysql
#cd /Volumes/DriveD/College-Teaching/Conestoga-College/Course_DatabaseAutomation/Scripts/w6/in-class


app = Flask(__name__)

# Database connection
def get_db_connection():
    return pymysql.connect(
        user='root',
        password='jasleen123',
        host='localhost',
        database='newdb'
    )

# Simple login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # For demonstration, assume login is successful and insert into the database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        cursor.close()
        conn.close()
        return "Login Successful"
    return '''
        <form method="post">
            username: <input type="text" name="username"><br>
            password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
