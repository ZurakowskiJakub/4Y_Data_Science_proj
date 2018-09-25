import requests
import json

original_data = requests.get("https://data.baltimorecity.gov/api/views/3i3v-ibrt/rows.json?accessType=DOWNLOAD").json()

columns = []
for column in original_data['meta']['view']['columns']:
    columns.append(column['name'])

temp_list = []
for arrest in original_data['data']:
    temp_dict = {}
    for index, arrest_detail in enumerate(arrest):
        temp_dict[columns[index]] = arrest_detail
    temp_list.append(temp_dict)

with open("arrest_data.json", "w") as file:
    json.dump(temp_list, file, indent=4)
