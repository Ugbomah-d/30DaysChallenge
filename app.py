from flask import Flask
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

@app.route('/')
def hello():
  return "Welcome to my 30 days challenge"

if __name__ == '__main__':
  app.run(debug=True)