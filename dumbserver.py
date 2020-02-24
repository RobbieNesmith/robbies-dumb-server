from flask import Flask

import os
import psycopg2

DATABASE_URL = os.environ["DATABASE_URL"]

app = Flask(__name__)

@app.route("/")
def index():
  return "Index page"

@app.route("/list")
def list_items():
  conn = psycopg2.connect(DATABASE_URL, sslmode='require')
  cur = conn.cursor()
  cur.execute("SELECT * FROM test")
  results = cur.fetchall()
  cur.close()
  conn.close()
  out = ""
  for res in results:
    out += " ".join(res)
    out += "\n"
  return out
