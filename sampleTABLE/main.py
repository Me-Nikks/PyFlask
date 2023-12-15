import MySQLdb.cursors
from flask import Flask, request, session, render_template, redirect
from flask_mysqldb import MySQL
import re

app = Flask(__name__)
# username, password, host, DB name
app.secret_key = 'secret_key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'DasV@654321'
app.config['MYSQL_DB'] = 'userprofile'

mysql = MySQL(app)   #initializes the MySQL instance with the Flask app.


@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)    #Establishes a connection to the MySQL database
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['id'] = user['id']
            session['username'] = user['username']
            message = 'login successful'
            return render_template('index.html')
        else:
            message = 'Invalid'
            return render_template('login.html')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['adress']
        city = request.form['city']
        state = request.form['state']
        country = request.form['country']
        postcode = request.form['postcode']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'INSERT INTO USERS(USERNAME,PASSWORD,EMAIL,PHONE,ADRESS,CITY,STATE,COUNTRY,POSTCODE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            (username, password, email, phone, address, city, state, country, postcode))
        mysql.connection.commit()
        return redirect('/login')

    return render_template('Registration.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='61', debug=True)
