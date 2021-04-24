import flask
import pandas as pd
from flask import Flask, render_template, url_for
from src import water_temp_time_series_pred

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/watertemp', methods=['GET'])
def watertemp():
    return render_template("watertemp.html")


# @app.route('/getwatertempdata', methods=['GET'])
# def get_water_temp_data():
#     df = pd.read_csv("data/Beach_Water_Quality_-_Automated_Sensors.csv", parse_dates=['Measurement Timestamp'])
#     cols_to_keep = ["Water Temperature", "Measurement Timestamp"]

#     ohio_street_beach_water_temp_df = df[df["Beach Name"] == "Ohio Street Beach"]
#     ohio_street_beach_water_temp_df = ohio_street_beach_water_temp_df[cols_to_keep]
#     ohio_street_beach_water_temp_df = ohio_street_beach_water_temp_df[(ohio_street_beach_water_temp_df['Measurement Timestamp'].dt.year == 2015) \
#                             & (ohio_street_beach_water_temp_df['Measurement Timestamp'] < '09/30/2015')]

#     return ohio_street_beach_water_temp_df

if __name__=="__main__":
    app.run()
