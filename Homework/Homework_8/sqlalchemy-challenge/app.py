import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import datetime as dt

engine=create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station




from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return (
        f"Home Page:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/(start date)<br/>"
        f"/api/v1.0/(start date)/(end date)")

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    results = session.query(Measurement.date,Measurement.prcp)
    precipitation = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        precipitation.append(prcp_dict)

    return jsonify(precipitation)


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(Station.station)
    Stations = []
    for station in results:
        station_dict = {}
        station_dict["Station"] = station
        Stations.append(station_dict)
    return jsonify(Stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    Last_Date = session.query(Measurement.date).filter(Measurement.station=='USC00519281').order_by(Measurement.date.desc()).first()[0]
    Last_Date = dt.datetime.strptime(Last_Date, '%Y-%m-%d')
    Last_12_Months = Last_Date - dt.timedelta(days =366)
    Last_12_Months

    results =session.query(Measurement.date, Measurement.tobs).filter(Measurement.date>Last_12_Months)

    TOBS = []
    for date, tobs in results:
        tobs_dict={}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        TOBS.append(tobs_dict)
    return jsonify(TOBS)


@app.route("/api/v1.0/<start_date>")
def start_date(start_date):
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date>start_date).all()
    return (f"Tmin: {results[0][0]}<br/>"
    f"Tmax: {results[0][1]} <br/>"
    f"Tavg: {results[0][2]}")


@app.route("/api/v1.0/<start_date>/<end_date>")
def end_date(start_date , end_date):
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date > start_date).filter(Measurement.date < end_date).all()
    return (f"Tmin: {results[0][0]}<br/>"
    f"Tmax: {results[0][1]} <br/>"
    f"Tavg: {results[0][2]}")


if __name__ == '__main__':
    app.run(debug=True)
