import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)


app = Flask(__name__)

past_year = '2016-08-23'
last_date = '2017-08-23'

@app.route("/")
def LandingPage():
    return "Welcome to my app page.<br/>" 
    return "You can use the following directories to get information on Hawaii's weather:<br/>"
    return "/api/v1.0/precipitation<br/>"
    return "/api/v1.0/stations<br/>"
    return "/api/v1.0/tobs<br/>"
    return "/api/v1.0/yyyy-mm-dd/yyyy-mm-dd<br/>"
    return "/api/v1.0/yyyy-mm-dd<br/>"
       

@app.route("/api/v1.0/precipitation")
def precipitation():
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= int(past_year).all()

    #all_dates = []

    for date in results:
        date_dict = {} 
        date_dict["date"] = Measurement.prcp 
        all_dates.append(date_dict) 
        
    return jsonify(all_dates)

@app.route("/api/v1.0/stations")
def stations():
    return 


@app.route("/api/v1.0/tobs")
def tobs():
    return 

if __name__ == "__main__":
    app.run(debug=True)