import requests
import json
import csv
import os

original_data = requests.get("https://data.baltimorecity.gov/api/views/wsfq-mvij/rows.csv?accessType=DOWNLOAD")

with open("temp.csv", "w+") as f:
    f.write(original_data.text)

new_data = []
data_scope = ["2018", "2017", "2016"]

with open("temp.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['CrimeDate'][-4:] in data_scope:
            new_data.append(row)

with open("incident_data.json", "w+") as f:
    json.dump(new_data, f, indent=4)

os.remove("temp.csv")
print("temp.csv deleted!")
print("incident_data.json updated!")
