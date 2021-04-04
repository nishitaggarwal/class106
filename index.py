import numpy as np
import plotly.express as px
import csv 

def getDataSource(data_path):
    Coffee_in_ml = []
    sleep_in_hours = []
            
    with open(data_path) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                Coffee_in_ml.append(float(row["sleep in hours"]))
                sleep_in_hours.append(float(row["sleep in hours"]))
    return {"x":sleep_in_hours,"y":Coffee_in_ml}

def findCorelation(dataSource):
    corelation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Corelation between cups of cofee vs hours of sleep:",corelation[0,1])

def setup():
    data_path = "coffee.csv"
    dataSource = getDataSource(data_path)
    findCorelation(dataSource)

setup()