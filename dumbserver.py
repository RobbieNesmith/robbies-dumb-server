from flask import Flask, request

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
  return "\n".join([" ".join([str(col) for col in result]) for result in results])

@app.route("/create")
def create_item():
  title = request.args.get("title")
  description = request.args.get("description")
  conn = psycopg2.connect(DATABASE_URL, sslmode='require')
  cur = conn.cursor()
  cur.execute("INSERT INTO TEST (title, description) VALUES (%s, %s)", (title, description))
  cur.close()
  conn.close()
  return f"added {title} {description}"
