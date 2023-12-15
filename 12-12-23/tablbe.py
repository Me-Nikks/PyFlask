from flask import Flask, request, redirect,url_for, session, render_template
from flask_mysql imoprt Mysql
import MySQLdb.cursors
import re

app = Flask(__name__)
#username, password, host, DB name

app.config['MYSQL_HOST'] =  'localhost'

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'DasV@654321'
app.config['MYSQL_DB'] = 'userprofile'

mysql = MySQL(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='81', Debug=True)
