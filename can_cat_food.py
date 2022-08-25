import sqlite3
from datetime import datetime

import pytz
from flask import Flask, render_template, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("database.sqlite")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()
    query = "SELECT * FROM meals ORDER BY last_meal DESC"
    if request.method == "GET":
        last_meal = conn.execute(query).fetchone()
        conn.close()

        return render_template("index.html", last_meal=last_meal)

    local_time = datetime.now(pytz.timezone("Europe/Tallinn"))
    now = datetime.strftime(local_time, "%d-%m-%Y %H:%M:%S")
    conn.execute("INSERT INTO meals (last_meal) VALUES (?)", (now,))
    last_meal = conn.execute(query).fetchone()
    conn.close()

    return render_template("index.html", last_meal=last_meal)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
