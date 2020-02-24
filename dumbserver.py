from flask import Flask

app = Flask(__name__)

def setup_db():
	pass

@app.route("/")
def index():
  return "Index page"
