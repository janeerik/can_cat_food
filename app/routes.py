from datetime import datetime

import pytz
from flask import render_template, redirect, url_for

from app import app, db
from app.models import Meal


@app.get("/")
def index():
    last_meal = Meal.query.order_by(Meal.timestamp.desc()).first()
    formatted_time = "Never"
    if last_meal:
        local_time = last_meal.timestamp.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Europe/Tallinn"))
        formatted_time = datetime.strftime(local_time, "%d-%m-%Y %H:%M:%S")

    return render_template("index.html", last_meal=formatted_time)


@app.post("/")
def store():
    db.session.add(Meal())
    db.session.commit()

    return redirect(url_for("index"))
