import os

import pandas as pd

# List of county
county = ["Brewster", "Fredericksburg", "Round Rock", "Houston", "Everglades", "Arcadia", "Weston", "Miami"]
base_path = "../data/AAAAA/yearly/"

for c in county:
    # List of files to read
    files = [f"{c}-yearly-avg-commute.csv", f"{c}-yearly-bio.csv", f"{c}-yearly-employ-industrial.csv",
             f"{c}-yearly-population.csv", f"{c}-yearly-property-value.csv",
             f"{c}-yearly-rela-industrial.csv"]

    # Create an empty dataframe to store the merged data
    merged_df = pd.DataFrame()

    # Loop through each file and merge it with the existing dataframe
    for file in files:
        file = base_path + file
        print("Processing the ", file.split("/")[-1])
        df = pd.read_csv(file)
        try:
            df = df.drop(columns=["Unnamed: 0"])
        except:
            pass
        if merged_df.empty:
            merged_df = df
        else:
            merged_df = pd.merge(merged_df, df, on=["Year", "County"], how="outer")

    # Print the merged dataframe
    merged_df.to_csv(f"../data/AAAAA/{c}-merged.csv")

files = [base_path + f for f in os.listdir(base_path) if f.endswith("-merged.csv")]

# Create an empty dataframe to store the merged data
merged_df = pd.DataFrame()

for file in files:
    print("Processing the ", file.split("/")[-1])
    df = pd.read_csv(file)
    try:
        df = df.drop(columns=["Unnamed: 0"])
    except:
        pass
    if merged_df.empty:
        merged_df = df
    else:
        merged_df = pd.concat(merged_df, df, ignore_index=True)

    # Print the merged dataframe
    merged_df.to_csv(f"../data/AAAAA/yearly-summary.csv")
