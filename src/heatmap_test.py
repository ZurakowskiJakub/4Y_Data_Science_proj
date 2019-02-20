from flask import Flask
from flask import render_template
import json

app = Flask(__name__)
app.debug = True
app.template_folder = "heatmap_templates"


@app.route('/')
def index():
    # with open("arrest_data.json", "r") as f:
    with open("../data/heatmapdata.json", "r") as f:
        list_of_arrests = json.load(f)
    
    data = []
    for arrest in list_of_arrests:
        point = {}
        if arrest['Latitude'] is not None and arrest['Felony'] is not "False":
            point['Lat'] = arrest['Latitude']
            point['Lng'] = arrest['Longitude']
            data.append(point)

    print(len(data))

    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run()