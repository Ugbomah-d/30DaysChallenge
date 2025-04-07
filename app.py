from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
  return "Welcome to the 30 days challenge"

if __name__ == '__main__':
  app.run(debug=True)