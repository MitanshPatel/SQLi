from flask import Flask, request, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)


@app.route("/get")
def get():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("select * from data")
    data = c.fetchall()
    return "<br>".join([i[0] for i in data])


@app.route("/register")  #to register and add new person
def register():
    code = request.args.get('code')
    conn = sqlite3.connect("data.db") #connect to db
    c = conn.cursor()
    try:
        c.execute("INSERT INTO data VALUES (?)", (code,))  #insert the name in db
        conn.commit()
        return f"Successfully added {code}"  #return the response
    except sqlite3.Error as e: #error
        return str(e)


@app.route("/search")
def search():
    code = request.args.get('code')  #params fetch from URL
    conn = sqlite3.connect("data.db")  #connect to db
    c = conn.cursor()   #for sql
    try:
        statement = "select * from data where data='" + code + "'"   #sql stmt
        c.execute(statement)  #execute the sql stmt
        found = c.fetchall() #fetch the data
        if found == []: #if not found
            return f"Invalid Code<br>{statement}" #send response
        else:
            return f" Connection Established<br>{found}" #else send the response if data found in db
    except sqlite3.Error as e: #error handle
        return str(e) + f"<br>{statement}"


@app.route("/login")
def login():
    return open("login.html").read()


@app.route("/")
def main():
    return open("403.html").read()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
