import numpy as np
import plotly.express as px
import csv 

def getDataSource(data_path):
    marks = []
    present = []
            
    with open(data_path) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                marks.append(float(row["Marks In Percentage"]))
                present.append(float(row["Days Present"]))
    return {"x":present,"y":marks}

def findCorelation(dataSource):
    corelation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Corelation between Student marks vs days present :",corelation[0,1])

def setup():
    data_path = "Student.csv"
    dataSource = getDataSource(data_path)
    findCorelation(dataSource)

setup()