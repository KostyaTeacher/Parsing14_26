from flask import render_template
from app import app, Session
from flask_login import login_required, logout_user
from flask import redirect, url_for
from datetime import timedelta, date
import requests
import random as r

from app.models import Event


@app.get("/")
@login_required
def main():
    mock = {}
    for item in range(1, 6):
        event_date = date.today() + timedelta(days=item)
        date_str = event_date.strftime("%d %B")
        info = requests.get(f"https://rickandmortyapi.com/api/character/{item}")
        info_text = info.json()
        print(f"{info_text.get("name")} {info_text.get("gender")} {info_text.get("status")}")
        events = [requests.get(f"https://rickandmortyapi.com/api/character/{item}")]
        mock[date_str] = [event.json().get("name") for event in events]

        session = Session()
        event1 = Event()
        event1.date = event_date
        event1.header = events[0].json().get("name")
        event1.describe = events[0].json().get("name")
        session.add(event1)
        session.commit()


    print(mock)
    return render_template('main.html', iterable=mock)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))