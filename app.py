from flask import Flask, g, request, jsonify
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from Model.user import db, User

app = Flask(__name__)
load_dotenv()
# DATABASE = 'database.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
  db.create_all()

@app.route('/')
def hello():
  return 'Welcome'

if __name__ == '__main__':
  
  app.run(debug=True)