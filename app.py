# Import dependencies
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

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new mode
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save preferences to the table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# Flask setup
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

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

# PRECIPITATION PAGE
# Convert the query results to a dictionary using date as the key and prcp as the value. 
# Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation")
def precipitation():
    lastdate = session.query(func.max(measurement.date)).all()[0][0]
    session.close()
    lastdate = dt.datetime.strptime(lastdate, '%Y-%m-%d')
    year_ago_date = lastdate - dt.timedelta(365)
    year_data = session.query(measurement.date, measurement.prcp)\
                    .filter(measurement.date >= year_ago_date)\
                    .order_by(measurement.date.desc()).all()
    session.close()

    precipitationData = []
    for data in year_data:
        prcp_Dict = {"Date": data.date, "Precipitation": data.prcp}
        precipitationData.append(prcp_Dict)

    return jsonify(precipitationData)  

# STATIONS PAGE
# Return a JSON list of the station names.
@app.route("/api/v1.0/stations")
def stations():
    stationsQuery = session.query(station.name).all()
    session.close()
    stationData = []
    for station_ in stationsQuery[:1]:
        stations_Dict = {"Name": stationsQuery}
        stationData.append(stations_Dict)
    
    return jsonify(stationData)

# TEMPERATURE OBSERVATIONS OF THE MOST ACTIVE STATION
# Query the dates and temperature observations of the most active station for the last year of data. 
# Return a JSON list of temperature observations (TOBS) for the previous year.
@app.route("/api/v1.0/tobs")
def tobs():
    lastdate = session.query(func.max(measurement.date)).all()[0][0]
    session.close()
    lastdate = dt.datetime.strptime(lastdate, '%Y-%m-%d')
    year_ago_date = lastdate - dt.timedelta(365)
    most_active_station_data = (session.query(measurement.date, measurement.station, measurement.tobs)\
                                .filter(measurement.date >= year_ago_date)\
                                .order_by(measurement.date.desc()).all())
    session.close()

    tobsList = []
    for data in most_active_station_data:
        tobsDict = {"Station": data.station, data.date: data.tobs}
        tobsList.append(tobsDict)

    return jsonify(tobsList)

# START PAGE
# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start.
@app.route("/api/v1.0/<start>")
def start(start):
    low = (session.query(func.min(measurement.tobs)).filter(measurement.date >= start)).all()[0][0]
    session.close()
    high = (session.query(func.max(measurement.tobs)).filter(measurement.date >= start)).all()[0][0]
    session.close()
    avg = (session.query(func.avg(measurement.tobs)).filter(measurement.date >= start)).all()[0][0]
    session.close()
    avg = round(avg, 2)


    return jsonify(low, high, avg)


# START/END PAGE
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start-end range.
@app.route("/api/v1.0/<start>/<end>")
def startEnd(start, end):
    low = (session.query(func.min(measurement.tobs)).filter(measurement.date >= start).filter(measurement.date <= end)).all()[0][0]
    session.close()
    high = (session.query(func.max(measurement.tobs)).filter(measurement.date >= start).filter(measurement.date <= end)).all()[0][0]
    session.close()
    avg = (session.query(func.avg(measurement.tobs)).filter(measurement.date >= start).filter(measurement.date <= end)).all()[0][0]
    session.close()
    avg = round(avg, 2)

    return jsonify(low, high, avg)



if __name__ == "__main__":
    app.run(debug=True)