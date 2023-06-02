import os

import pandas as pd

base_path = "../data/aqi/"
files = [base_path + f for f in os.listdir(base_path)]
# Collier->Monroe
search_county_list = ["Brewster", "Bexar", "Travis", "Harris", "Collier", "Manatee", "Broward", "Miami-Dade"]
real_county_list = ["Brewster", "Gillespie", "Williamson", "Harris", "Monroe", "DeSoto", "Broward", "Miami-Dade"]


def process(file):
    df = pd.read_csv(file)
    filter_df = df[df["State"].isin(["Texas", "Florida"])]
    filter_df = filter_df[filter_df["County"].isin(search_county_list)]
    filter_df.reset_index(drop=True, inplace=True)
    for ori, real in zip(search_county_list, real_county_list):
        filter_df.loc[filter_df["County"] == ori, "County"] = real

    aqi_levels_name = ['Good Days', 'Moderate Days', 'Unhealthy for Sensitive Groups Days', 'Unhealthy Days',
                       'Very Unhealthy Days', 'Hazardous Days']
    for r in range(0, len(filter_df)):
        AQI = []
        BLO = 500
        BHI = 0
        IHI = [0, 51, 101, 151, 201, 301]
        ILO = [50, 100, 150, 200, 300, 500]
        C = filter_df.loc[r, aqi_levels_name].to_list()  # [100, 75, 105, 165, 205, 305]
        day_year = filter_df.loc[r, 'Days with AQI']
        for i in range(len(C)):
            AQI.append(((IHI[i] - ILO[i]) / (BHI - BLO)) * (C[i] - BLO) + ILO[i])
        summary_aqi = sum(AQI) / len(AQI) + filter_df.loc[r, "Max AQI"]
        filter_df.loc[r, "year_aqi"] = round(summary_aqi, 2)

    filter_df.drop(inplace=True,
                   columns=['Days with AQI', 'Good Days', 'Moderate Days', 'Unhealthy for Sensitive Groups Days',
                            'Unhealthy Days', 'Very Unhealthy Days', 'Hazardous Days', 'Max AQI', '90th Percentile AQI',
                            'Median AQI', 'Days CO', 'Days NO2', 'Days Ozone', 'Days PM2.5', 'Days PM10'])
    return filter_df


if __name__ == '__main__':
    dfs = None  # pd.DataFrame({'State', 'County', 'Year', 'year_aqi'})
    for f in files:
        if dfs is None:
            dfs = process(f)
        else:
            dfs = pd.concat([dfs, process(f)], ignore_index=True)
    dfs.to_csv(base_path + "summary_aqi.csv")
