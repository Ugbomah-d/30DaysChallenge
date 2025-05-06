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

@app.route('/register', methods=['POST'])
def registration():
  if request.method != 'POST':
    return jsonify({"error":'Method Not Allowed'}), 405   
  
  data = request.get_json()

  username = data.get('username')
  password = data.get('password')
  email = data.get('email')

  if not username or not password or not email:
    return jsonify({"error":'No username or password'}), 405

  #Hash password
  hashed_password = generate_password_hash(password)

  #User object
  new_user = User(username=username, password=hashed_password, email=email)

  #Store in database
  db.session.add(new_user)
  db.session.commit()

  return 'Successful', 200

@app.route('/login', methods =['POST'])
def login():
  
  if request.method != 'POST':
    return jsonify({"Error":'Method Not Allowed'}), 405   
  
  data = request.get_json()

  username = data.get('username')
  password = data.get('password')

  #Find User
  user = User.query.filter_by(username=username).first()

  if not user:
    return jsonify({"Error": 'User not found'}), 404
  
  #Compare passwords
  if not check_password_hash(user.password, password):
    return jsonify({"Error": 'Invalid Passwordd'}), 401
  
  return jsonify({"message": f"{user.username} logged in sucessfully"})

@app.route('/user/display')
def displayUsers():
  users = User.query.all()
  return jsonify([user.to_dict() for user in users])


if __name__ == '__main__':
  
  app.run(debug=True)