import pandas as pd

df = pd.read_csv("data/Beach_Water_Quality_-_Automated_Sensors.csv")

print(df["Beach Name"].unique())

# goal: display time series graphs of water quality for each of the beaches....incorporate colors