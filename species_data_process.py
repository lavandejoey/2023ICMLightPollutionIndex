import os

import pandas as pd

base_path = "../data/species_by_county/"
files = [base_path + f for f in os.listdir(base_path)]

to_drop = ["gbifID", "datasetKey", "occurrenceID", "kingdom", "phylum", "class", "order", "family", "species",
           "taxonRank", "infraspecificEpithet", "verbatimScientificName", "verbatimScientificNameAuthorship",
           "countryCode", "locality", "stateProvince", "occurrenceStatus", "publishingOrgKey", "decimalLatitude",
           "decimalLongitude", "coordinateUncertaintyInMeters", "coordinatePrecision", "elevation", "elevationAccuracy",
           "depth", "depthAccuracy", "eventDate", "day", "month", "taxonKey", "speciesKey", "basisOfRecord",
           "institutionCode", "collectionCode", "catalogNumber", "recordNumber", "identifiedBy", "dateIdentified",
           "license", "rightsHolder", "recordedBy", "typeStatus", "establishmentMeans", "lastInterpreted", "mediaType",
           "issue"]
res_columns = ["genus", "scientificName", "individualCount", "year", ]
columns = ["gbifID", "datasetKey", "occurrenceID", "kingdom", "phylum", "class", "order", "family", "genus", "species",
           "infraspecificEpithet", "taxonRank", "scientificName", "verbatimScientificName",
           "verbatimScientificNameAuthorship", "countryCode", "locality", "stateProvince", "occurrenceStatus",
           "individualCount", "publishingOrgKey", "decimalLatitude", "decimalLongitude",
           "coordinateUncertaintyInMeters", "coordinatePrecision", "elevation", "elevationAccuracy", "depth",
           "depthAccuracy", "eventDate", "day", "month", "year", "taxonKey", "speciesKey", "basisOfRecord",
           "institutionCode", "collectionCode", "catalogNumber", "recordNumber", "identifiedBy", "dateIdentified",
           "license", "rightsHolder", "recordedBy", "typeStatus", "establishmentMeans", "lastInterpreted", "mediaType",
           "issue"]

if __name__ == '__main__':
    for d in files:
        if not d.endswith(".csv"):
            ori_file = d + "/" + os.listdir(d)[0]
            new_file = d + ".csv"
            os.rename(ori_file, new_file)
    for f in files:
        df = pd.read_csv(f, sep="\t", low_memory=False)
        df = df.drop(columns=to_drop)
        # Group the data by year and aggregate the genus and individualCount columns
        genus_counts = df.groupby('year')['genus'].count()
        indiv_counts = df.groupby('year')['individualCount'].sum()
        cnt_by_year = pd.merge(genus_counts, indiv_counts, on='year')

        cnt_by_year.to_csv(f.split("-")[0] + "-boiDiv.csv")
        print(f.split("-")[0].split("/")[-1], "saved.")
