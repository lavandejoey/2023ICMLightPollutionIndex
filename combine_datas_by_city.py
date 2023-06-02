import glob
import os

import pandas as pd

base_path = "../data/AAAAA/cplt_data/"
cities = ["Brewster", "Fredericksburg", "Round", "Houston", "Everglades", "Arcadia", "Weston", "Miami"]

for city in cities:
    files = glob.glob(os.path.join(base_path, f"{city}*"))
    files = [f.replace("\\", "/") for f in files]
    # dfs = pd.read_csv(files[0])

    # Create an empty list to store the dataframes
    dfs = []

    # Loop through the files and read each CSV file using pandas
    for file in files:
        # Get the file name without the extension
        filename = os.path.splitext(file)[0]
        # Read the CSV file and add a column named "filename"
        df = pd.read_csv(file)
        # df['filename'] = filename
        try:
            df.index = df["year"]
        except:
            df.index = df["Year"]
        else:
            print("ERROR")
        # Add the dataframe to the list
        dfs.append(df)

    # Concatenate the dataframes into a single dataframe
    merged_df = pd.concat(dfs)

    # Reset the index of the merged dataframe
    merged_df.reset_index(drop=True, inplace=True)
    merged_df.to_csv("../data/AAAAA/tmp.csv")
