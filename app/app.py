from flask import Flask, Response, request
import psycopg
import os
import datetime

app = Flask(__name__)

API_KEY = os.environ["API_KEY"]

def is_authorized(headers):
    return headers.get("X-Api-Key") == API_KEY

def create_conn():
    return psycopg.connect("postgresql://jerry:password123@db/vikeandsell")

with create_conn() as conn:
    print("creating db schema")
    conn.execute(open("schema.sql", "r").read())

print("db schema created")

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/dump_users")
def dump_users():
    if not is_authorized(request.headers):
        return Response(status=401)

    with create_conn() as conn:
        cursor = conn.execute("SELECT * FROM Users")
        return Response(str(cursor.fetchall()), status=200)

@app.route("/make_user", methods=["POST"])
def make_user():
    if not is_authorized(request.headers):
        return Response(status=401)

    with create_conn() as conn:
        data = request.get_json()
        username = data["username"]
        email = data["email"]
        password = data["password"]
        location = f"ST_GeographyFromText('SRID=4326;POINT({data["location"]})')"
        print(f"creating user {username}")
        conn.execute(f"INSERT INTO Users (username, email, password, location, join_date, items_sold, items_purchased) \
                              VALUES ('{username}', '{email}', '{password}', {location}, NOW(), array[]::integer[], array[]::integer[])")
        return Response(status=200)


if __name__ == '__main__':
    app.run(debug=True)
