import os

import numpy as np
import pandas as pd

base_path = "../data/AAAAA/cplt_data/"
cities = ["Brewster", "Fredericksburg", "Round", "Houston", "Everglades", "Arcadia", "Weston", "Miami"]
pv_files = [base_path + f for f in os.listdir(base_path) if f.endswith("property_value.csv")]
mid_prices = [round((0 + 10000) / 2), round((10000 + 14999) / 2), round((15000 + 19999) / 2),
              round((20000 + 24999) / 2), round((25000 + 29999) / 2), round((30000 + 34999) / 2),
              round((35000 + 39999) / 2), round((40000 + 49999) / 2), round((50000 + 59999) / 2),
              round((60000 + 69999) / 2), round((70000 + 79999) / 2), round((80000 + 89999) / 2),
              round((90000 + 99999) / 2), round((100000 + 124999) / 2), round((125000 + 149999) / 2),
              round((150000 + 174999) / 2), round((175000 + 199999) / 2), round((200000 + 249999) / 2),
              round((250000 + 299999) / 2), round((300000 + 399999) / 2), round((400000 + 499999) / 2),
              round((500000 + 749999) / 2), round((750000 + 999999) / 2), round((1000000 + 1499999) / 2),
              round((1500000 + 1999999) / 2), round((2000000 + 2000000) / 2)]
mid_prices = np.array(mid_prices)
for f in pv_files:
    # f = pv_files[0]
    years = range(2013, 2021)
    df = pd.read_csv(f)
    df = round(df.groupby('Year').apply(lambda x: (mid_prices[x["ID Value Bucket"].values] * x["share"]).sum()), 4)
    df = df.to_frame(name="Property Value")
    df["County"] = f.split("/")[-1].split("-")[0]
    df.to_csv("../data/AAAAA/yearly/" + f.split("/")[-1].split("-")[0] + "-yearly-property-value.csv")

# industy dev
base_path = "../data/AAAAA/cplt_data/"
cities = ["Brewster", "Fredericksburg", "Round", "Houston", "Everglades", "Arcadia", "Weston", "Miami"]
pv_files = [base_path + f for f in os.listdir(base_path) if f.endswith("occupation.csv")]
for f in pv_files:
    # f = pv_files[0]
    df = pd.read_csv(f)
    df = df[~df["Occupation"].isin(
        ["Building & Grounds Cleaning & Maintenance Occupations", "Management Occupations",
         "Business & Financial Operations Occupations", "Community & Social Service Occupations",
         "Education Instruction, & Library Occupations",
         "Health Diagnosing & Treating Practitioners & Other Technical Occupations",
         "Personal Care & Service Occupations",
         "Law Enforcement Workers Including Supervisors", "Office & Administrative Support Occupations",
         "Farming, Fishing, & Forestry Occupations",
         "Construction & Extraction Occupations", "Installation, Maintenance, & Repair Occupations",
         "Production Occupations", "Healthcare Support Occupations", ])].drop(columns=["Unnamed: 0"])
    df.reset_index(drop=True, inplace=True)
    df = df.groupby(["Year"]).apply(lambda x: ((x["Median Earnings"] * x["Workforce by Occupation and Gender"]).sum()))
    df = df.to_frame(name="Industry Dev")
    df["County"] = f.split("/")[-1].split("-")[0]
    df.to_csv("../data/AAAAA/yearly/" + f.split("/")[-1].split("-")[0] + "-yearly-rela-industrial.csv")


#population
import os

import pandas as pd

base_path = "../data/AAAAA/cplt_data/"
cities = ["Brewster", "Fredericksburg", "Round", "Houston", "Everglades", "Arcadia", "Weston", "Miami"]
pv_files = [base_path + f for f in os.listdir(base_path) if f.endswith("population.csv")]
for f in pv_files:
    # f = pv_files[0]
    df = pd.read_csv(f).drop(columns=["Unnamed: 0","Geography"])
    df["County"] = f.split("/")[-1].split("-")[0]
    df.to_csv("../data/AAAAA/yearly/" + f.split("/")[-1].split("-")[0] + "-yearly-population.csv")

#
import os

import pandas as pd

base_path = "../data/AAAAA/cplt_data/"
cities = ["Brewster", "Fredericksburg", "Round", "Houston", "Everglades", "Arcadia", "Weston", "Miami"]
pv_files = [base_path + f for f in os.listdir(base_path) if f.endswith("-occupation.csv")]
for f in pv_files:
    # f = pv_files[0]
    df = pd.read_csv(f)
    df = df[~df["Occupation"].isin(
        ["Building & Grounds Cleaning & Maintenance Occupations", "Management Occupations",
         "Business & Financial Operations Occupations", "Community & Social Service Occupations",
         "Education Instruction, & Library Occupations",
         "Health Diagnosing & Treating Practitioners & Other Technical Occupations",
         "Personal Care & Service Occupations",
         "Law Enforcement Workers Including Supervisors", "Office & Administrative Support Occupations",
         "Farming, Fishing, & Forestry Occupations",
         "Construction & Extraction Occupations", "Installation, Maintenance, & Repair Occupations",
         "Production Occupations", "Healthcare Support Occupations", ])].drop(columns=["Unnamed: 0"])
    df.reset_index(drop=True, inplace=True)
    df = df[["Year", "Workforce by Occupation and Gender"]]
    df = df.groupby(["Year"]).apply(lambda x: ((x["Workforce by Occupation and Gender"]).sum()))
    df = df.to_frame(name="Industry Employ")
    df["County"] = f.split("/")[-1].split("-")[0]
    df.to_csv("../data/AAAAA/yearly/" + f.split("/")[-1].split("-")[0] + "-yearly-employ-industrial.csv")
