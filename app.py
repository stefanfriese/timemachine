#!/usr/bin/env python
# encoding: utf-8

from flasgger import Swagger
from flask import Flask, jsonify, redirect, render_template

from datetime import datetime, timezone
from dateutil import parser
import pytz


app = Flask(__name__)
Swagger(app)


@app.route("/")
def home():
    """/ Route will redirect to API Docs: /apidocs"""

    return redirect("/apidocs")

@app.route('/showhelp', methods = ['GET'])
def showhelp():
    """/ Show help: /showhelp"""
    return render_template("index.html")


@app.route("/now", methods = ['GET'])
def now():
    """Returns for some cities local time


        GET /api/now
        ---
        responses:
            200:
                description: Returns for some cities the local time.


    """

    # note that timezone requires python3
    tz_utc = pytz.utc.localize(datetime.utcnow())
    tz_nyc = tz_utc.astimezone(pytz.timezone("America/New_York"))
    tz_chicago = tz_utc.astimezone(pytz.timezone("America/Chicago"))
    tz_berlin = tz_utc.astimezone(pytz.timezone("Europe/Berlin"))
    tz_Sydney = tz_utc.astimezone(pytz.timezone("Australia/Sydney"))

    return jsonify(UTC=tz_utc.isoformat(), Berlin=tz_berlin.isoformat(), New_York=tz_nyc.isoformat(), Chicago=tz_chicago.isoformat(), Sydney=tz_Sydney.isoformat())


@app.route("/normalize/<input_date>", methods = ['GET'])
def normalize(input_date):
    """Returns dates in different formats


        GET /api/normalize
        ---
        parameters:
            -   in:    path
                name:  input_date
                type:  string
                required: true
                description:  Date that shall get normalized
        responses:
            200:
                description: Returns dates in different formats.


    """

    if input_date.isdigit():
        ts = input_date
        dt = datetime.fromtimestamp(float(input_date)).strftime("%Y-%m-%d") 
        
        return jsonify(timestamp=input_date, day=dt)

    else:
        d = parser.parse(input_date)
        dt = d.strftime("%Y-%m-%d")
        # timezone requires python3
        ts = parser.parse(input_date).replace(tzinfo=timezone.utc).timestamp()
        return jsonify(input=input_date, day=dt, timestamp=ts)


# Runs server
if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 80)
