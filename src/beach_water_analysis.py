import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

from fbprophet import Prophet
from fbprophet.plot import add_changepoints_to_plot

def plot_turbidity_by_location(year, df):
    cols_to_keep = ["Measurement Timestamp", "Turbidity"]
    
    fig = plt.figure()
    plot_title = 'Turbidity by Location in ' + str(year)
    plt.title(plot_title)
    ax = fig.add_subplot(111)

    for location in locations:
        location_df = df[df["Beach Name"] == location]
        location_df = location_df[cols_to_keep]
        location_df = location_df[(location_df['Measurement Timestamp'].dt.year == year) \
                                  & (location_df['Measurement Timestamp'] < '09/30/2015')]
        
        if location_df.shape[0] > 0:
            ax.plot(location_df['Measurement Timestamp'], location_df['Turbidity'], label=location)

    plt.xticks(rotation=45)
    plt.xlabel('Measurement Timestamp')
    plt.ylabel('Water Turbidity (NTU)')
    plt.legend(title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left')
    # plt.show()
    plt.savefig('data/' + plot_title + '.png', dpi=200, bbox_inches='tight')
    print(plot_title, ' fig saved!')


def turbidity_stats_by_location(year, df):
    cols_to_keep = ["Measurement Timestamp", "Turbidity"]

    for location in locations:
        location_df = df[df["Beach Name"] == location]
        location_df = location_df[cols_to_keep]
        location_df = location_df[(location_df['Measurement Timestamp'].dt.year == year) \
                                  & (location_df['Measurement Timestamp'] < '09/30/2015')]
        
        print('Water Turbidity Stats by Location\n')
        if location_df.shape[0] > 0:
            # print max Turbidity
            print(location)
            print(location_df['Turbidity'].describe())
            print('\n')


def plot_water_temp_by_location(year, df):
    cols_to_keep = ["Measurement Timestamp", "Water Temperature"]
    
    fig = plt.figure()
    plot_title = 'Water Temperature by Location in ' + str(year)
    plt.title(plot_title)
    ax = fig.add_subplot(111)

    for location in locations:
        location_df = df[df["Beach Name"] == location]
        location_df = location_df[cols_to_keep]
        location_df = location_df[(location_df['Measurement Timestamp'].dt.year == year) \
                                  & (location_df['Measurement Timestamp'] < '09/30/2015')]
        
        if location_df.shape[0] > 0: # data for this location exists during this year
            ax.plot(location_df['Measurement Timestamp'], location_df['Water Temperature'], label=location)

    plt.xticks(rotation=45)
    plt.xlabel('Measurement Timestamp')
    plt.ylabel('Water Temperature (Celcius Degrees)')
    plt.legend(title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left')
    # plt.show()
    plt.savefig('data/' + plot_title + '.png', dpi=200, bbox_inches='tight')
    print(plot_title, ' fig saved!')


def plot_transducer_by_location(year, df):
    cols_to_keep = ["Measurement Timestamp", "Transducer Depth"]
    
    fig = plt.figure()
    plot_title = 'Transducer Depth by Location in ' + str(year)
    plt.title(plot_title)
    ax = fig.add_subplot(111)

    for location in locations:
        location_df = df[df["Beach Name"] == location]
        location_df = location_df[cols_to_keep]
        location_df = location_df[(location_df['Measurement Timestamp'].dt.year == year)]
        
        if location_df.shape[0] > 0:
            ax.plot(location_df['Measurement Timestamp'], location_df['Transducer Depth'], label=location)

    plt.xticks(rotation=45)
    plt.xlabel('Measurement Timestamp')
    plt.ylabel('Transducer Depth (m)')
    plt.legend(title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left')
    # plt.show()
    plt.savefig('data/' + plot_title + '.png', dpi=200, bbox_inches='tight')
    print(plot_title, ' fig saved!')


def water_temp_time_series_pred(df):
    cols_to_keep = ["Water Temperature", "Measurement Timestamp"]

    ohio_street_beach_water_temp_df = df[df["Beach Name"] == "Ohio Street Beach"]
    ohio_street_beach_water_temp_df = ohio_street_beach_water_temp_df[cols_to_keep]
    ohio_street_beach_water_temp_df = ohio_street_beach_water_temp_df[(ohio_street_beach_water_temp_df['Measurement Timestamp'].dt.year == 2015) \
                            & (ohio_street_beach_water_temp_df['Measurement Timestamp'] < '09/30/2015')]
    ohio_street_beach_water_temp_df.rename(columns={'Measurement Timestamp':'ds', 'Water Temperature':'y'}, inplace = True)
    m = Prophet() # seasonality_mode='multiplicative' (additive by default)
    m.fit(ohio_street_beach_water_temp_df)

    # data to hold future predictions
    # period is one row in your data
    future = m.make_future_dataframe(periods=7)
    forecast = m.predict(future)
    fig3 = m.plot(forecast)
    a = add_changepoints_to_plot(fig3.gca(), m, forecast)
    return fig3



if __name__=="__main__":
    df = pd.read_csv("../data/Beach_Water_Quality_-_Automated_Sensors.csv", parse_dates=['Measurement Timestamp'])
    print('read data from csv!')
    # locations = df["Beach Name"].unique()
    # plot_turbidity_by_location(2015, df)
    # turbidity_stats_by_location(2015, df)
    # plot_water_temp_by_location(2015, df)
    # plot_transducer_by_location(2014, df)
    water_temp_time_series_pred(df)
    print('time series plot saved!')












