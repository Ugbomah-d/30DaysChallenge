from flask import Flask, g, request
from dotenv import load_dotenv
import os
import sqlite3

app = Flask(__name__)
load_dotenv()

@app.route('/')
def hello():
  return "Welcome to my 30 days challenges"

@app.route('/register', method=('POST'))
def register():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']

    db = get_db()
    error = None
    if not username:
      error = "Username is required"
    elif not password:
      error = "Password is required"
    
    if error is None:
      try:
        db.execute("Insert into users(username, password) Values (?,?)",(username,  ))


if __name__ == '__main__':
  app.run(debug=True)