import joblib
import sys
import pandas as pd

def preprocess(): 
    csv = pd.read_csv(sys.argv[1])
    del csv['sublabel']
    csv.to_csv

# open pkl model
def open_model(model_path):
    model = joblib.load(model_path)
    return model

# predict
def predict(model, data):
    prediction = model.predict(data)
    return prediction

def loadRowData(): 
    rawData = pd.read_csv(sys.argv[1])
    return rawData

def loadData(rawData): 
    data = rawData[['sourceTransportPort', 'destinationTransportPort', 'packetTotalCount']]
    return data

def writeSubmitColumn(rawData, prediction):
    rawData['sublabel'] = prediction
    rawData.to_csv(sys.argv[1])

preprocess()
# rawData = loadRowData()
# data = loadData(rawData)
# model = open_model('model.pkl')
# prediction = predict(model, data)
# writeSubmitColumn(rawData, prediction)

# print(pd.read_csv(sys.argv[1]).head(1000))

