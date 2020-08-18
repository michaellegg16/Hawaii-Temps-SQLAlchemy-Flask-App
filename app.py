import pandas as pd
import numpy as np 
import datetime as dt
import matplotlib.pyplot as plt

import os
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

measurement = Base.classes.measurement
station = Base.classes.station

session = Session(engine)

app = Flask(__name__)

# HOME PAGE 
@app.route("/")
def home():
    """List all available api routes."""
    return (
        f'Avaiable Routes:<br/>'
        f'/api/v1.0/precipitation<br/>'
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/<start><br/>'
        f'/api/v1.0/<start>/<end><br/>'
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
#    """ Convert the query results to a dictionary using date as the key and prcp as the value. Return the JSON representation of your dictionary."""
    lastdate = session.query(func.max(measurement.date)).all()[0][0]
    lastdate = dt.datetime.strptime(lastdate, '%Y-%m-%d')
    year_ago_date = lastdate - dt.timedelta(365)
    year_data = session.query(measurement.date, measurement.prcp)\
                    .filter(measurement.date >= year_ago_date)\
                    .order_by(measurement.date.desc()).all()

    precipitationData = []
    for data in year_data:
        prcp_Dict = {"Date": data.date, "Precipitation": data.prcp}
        precipitationData.append(prcp_Dict)

    return jsonify(precipitationData)  

@app.route("/api/v1.0/stations")
def stations():
    # Return a JSON list of stations from the dataset.
    stationsQuery = session.query(station.name).all()
    stationData = []
    for station_ in stationsQuery[:1]:
        stations_Dict = {"Name": stationsQuery}
        stationData.append(stations_Dict)
    
    return jsonify(stationData)

@app.route("/api/v1.0/tobs")
def tobs():
    # Query the dates and temperature observations of the most active station for the last year of data. Return a JSON list of temperature observations (TOBS) for the previous year.
    lastdate = session.query(func.max(measurement.date)).all()[0][0]
    lastdate = dt.datetime.strptime(lastdate, '%Y-%m-%d')
    year_ago_date = lastdate - dt.timedelta(365)
    most_active_station_data = (session.query(measurement.date, measurement.station, measurement.tobs)\
                                .filter(measurement.date >= year_ago_date)\
                                .order_by(measurement.date.desc()).all())
    tobsList = []
    for data in most_active_station_data:
        tobsDict = {"Station": data.station, data.date: data.tobs}
        tobsList.append(tobsDict)

    return jsonify(tobsList)
    
@app.route("/api/v1.0/<start>")
def start(start):
    low = (session.query(func.min(measurement.tobs)).filter(measurement.date >= start)).all()[0][0]
    high = (session.query(func.max(measurement.tobs)).filter(measurement.date >= start)).all()[0][0]
    avg = (session.query(func.avg(measurement.tobs)).filter(measurement.date >= start)).all()[0][0]
    avg = round(avg, 2)

    return jsonify(low, high, avg)



@app.route("/api/v1.0/<start>/<end>")
def startEnd(start, end):
    low = (session.query(func.min(measurement.tobs)).filter(measurement.date >= start).filter(measurement.date <= end)).all()[0][0]
    high = (session.query(func.max(measurement.tobs)).filter(measurement.date >= start).filter(measurement.date <= end)).all()[0][0]
    avg = (session.query(func.avg(measurement.tobs)).filter(measurement.date >= start).filter(measurement.date <= end)).all()[0][0]
    avg = round(avg, 2)

    return jsonify(low, high, avg)
if __name__ == "__main__":
    app.run(debug=True)