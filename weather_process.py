import os

import pandas as pd

base_path = "../data/weather/"
files = [base_path + f for f in os.listdir(base_path)]

for f in files:
    df = pd.read_csv(f)
    df.columns = df.loc[1]
    df = df.loc[2:]
    df.reset_index(drop=True, inplace=True)
    df['temperature_2m_mean (°C)'] = df['temperature_2m_mean (°C)'].astype(float)
    df['shortwave_radiation_sum (MJ/m²)'] = df['shortwave_radiation_sum (MJ/m²)'].astype(float)
    df['precipitation_sum (mm)'] = df['precipitation_sum (mm)'].astype(float)
    df['et0_fao_evapotranspiration (mm)'] = df['et0_fao_evapotranspiration (mm)'].astype(float)

    # Convert the "time" column to a datetime object
    df["time"] = pd.to_datetime(df["time"])

    # Extract the year from the "time" column
    df["year"] = df["time"].dt.year

    # Group the data by year and calculate summary statistics
    summary_df = df.groupby("year").agg({
        "temperature_2m_mean (°C)": "mean",
        "shortwave_radiation_sum (MJ/m²)": "mean",
        "precipitation_sum (mm)": "mean",
        "et0_fao_evapotranspiration (mm)": "mean"
    })

    summary_df.columns = ['temperature(°C)', 'shortwave_radiation(MJ/m²)', 'precipitation(mm)',
                          'evapotranspiration(mm)']
    summary_df.to_csv(f.split(".csv")[0] + "-summary.csv")
