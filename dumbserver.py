from flask import Flask, request
from flask_cors import CORS

import os
import psycopg2

DATABASE_URL = os.environ["DATABASE_URL"]

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
  return "Index page"

@app.route("/list")
def list_items():
  conn = psycopg2.connect(DATABASE_URL, sslmode='require')
  cur = conn.cursor()
  cur.execute("SELECT * FROM test;")
  results = cur.fetchall()
  cur.close()
  conn.close()
  return "\n".join([" ".join([str(col) for col in result]) for result in results])

@app.route("/create", methods=["POST"])
def create_item():
  title = request.form.get("title")
  description = request.form.get("description")
  conn = psycopg2.connect(DATABASE_URL, sslmode='require')
  cur = conn.cursor()
  cur.execute("INSERT INTO test (title, description) VALUES (%s, %s);", (title, description))
  conn.commit()
  cur.close()
  conn.close()
  return f"added {title} {description}"
