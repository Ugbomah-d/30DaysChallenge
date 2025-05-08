from flask import Flask, g, request, jsonify
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from Model.user import db, User
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

app = Flask(__name__)
load_dotenv()
# DATABASE = 'database.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key ='ELDIN RING'

db.init_app(app)

# Initialize LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Load user from session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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
  
  user = User.query.filter_by(username=username).first()

  if user:
    return jsonify({"Message": 'User exists'}), 400

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
  
  login_user(user)
  return jsonify({"message": f"{user.username} logged in sucessfully"})

@app.route('/dashboard')
@login_required
def display():
  return jsonify({"message": f'welcome {current_user.username}'})

@app.route('/logout')
@login_required
def logout():
  logout_user()
  return jsonify({"message": "Logged out successfully"}), 200


@app.route('/user/display')
def displayUsers():
  users = User.query.all()
  return jsonify([user.to_dict() for user in users])


if __name__ == '__main__':
  
  app.run(debug=True)