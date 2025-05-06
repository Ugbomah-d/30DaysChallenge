from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
  id = db.Column(db.Integer, primary_key= True)
  username = db.Column(db.String(80), unique=True, nullable = False)
  email = db.Column(db.String(80), unique=True, nullable = False)
  firstname =db.Column(db.String(80))
  lastname =db.Column(db.String(80))
  password =db.Column(db.String(80))
  course =db.Column(db.String(80))

  #Converts to dictionary
  def to_dict(self):
    return{"id":self.id,
         "username":self.username,
         "password":self.password,
         "email": self.email
}



def __repr__(self):
  return f'<User {self.username}>'


# CREATE TABLE IF NOT EXISTS users (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   username VARCHAR,
#   firstname VARCHAR,
#   lastname VARCHAR,
#   passwords VARCHAR,
#   email VARCHAR,
#   isVerified BOOLEAN,
#   course VARCHAR,
#   created_at TIMESTAMP,
#   updated_at TIMESTAMP
# );

# CREATE TABLE IF NOT EXISTS posts (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   title VARCHAR,
#   body TEXT,
#   media_link VARCHAR,
#   created_at TIMESTAMP,
#   updated_at TIMESTAMP,
#   user_id INTEGER,
#   FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
# );

# CREATE TABLE IF NOT EXISTS likes (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   user_id INTEGER,
#   post_id INTEGER,
#   FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
#   FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE
# );

# CREATE TABLE IF NOT EXISTS dislikes (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   user_id INTEGER,
#   post_id INTEGER,
#   FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
#   FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE
# );

# CREATE TABLE IF NOT EXISTS otp (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   otp VARCHAR,
#   expiry_time TIMESTAMP,
#   created_at TIMESTAMP,
#   user_id INTEGER,
#   FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
# );

# CREATE TABLE IF NOT EXISTS followers (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   follower_id INTEGER,
#   following_id INTEGER,
#   created_at TIMESTAMP,
#   FOREIGN KEY (follower_id) REFERENCES users(id) ON DELETE CASCADE,
#   FOREIGN KEY (following_id) REFERENCES users(id) ON DELETE CASCADE
# );
