from flask import Flask, g, request, jsonify
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
import os
import sqlite3

app = Flask(__name__)
load_dotenv()
DATABASE = 'database.db'

#Connection to database
def get_db():
  if 'db' not in g:
    g.db = sqlite3.connect(DATABASE)
    g.db.row_factory = sqlite3.Row
  return g.db

# db = get_db()

@app.route('/')
def hello():
  return "Welcome to my 30 days challenges"

# @app.route('/users')
# def get_users():
#   db = get_db()
#   user = db.execute("SELECT * FROM users").fetchall()
#   user_list = [dict(row) for row in user]  # convert rows to dictionaries
#   return jsonify(user_list)

#Registration route
@app.route('/register', methods=['POST'])
def register():
  if request.method == 'POST':
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    db = get_db()
    
    db.execute("Insert into users(username, passwords) Values (?,?)",(username, generate_password_hash(password) ))
    db.commit()
  return "Registered"
      

if __name__ == '__main__':
  app.run(debug=True)