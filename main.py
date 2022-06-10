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
    for index, row in rawData.iterrows():
        if row['sublabel'] == 1:
            rawData.loc[index, 'sublabel'] = "Attempted Information Leak"
        elif row['sublabel'] == 2:
            rawData.loc[index, 'sublabel'] = "Generic Protocol Command Decode"
        elif row['sublabel'] == 3:
            rawData.loc[index, 'sublabel'] = "Misc Attack"
        elif row['sublabel'] == 4:
            rawData.loc[index, 'sublabel'] = "Command Decode"
        elif row['sublabel'] == 5:
            rawData.loc[index, 'sublabel'] = "Potential Corporate Privacy Violation"
        elif row['sublabel'] == 6:
            rawData.loc[index, 'sublabel'] = "Potentially Bad Traffic"
    rawData.to_csv(sys.argv[1], index=False)

# preprocess()
print("Loading data")
rawData = loadRowData()
data = loadData(rawData)
print("Done")
print("Loading model")
model = open_model(sys.argv[2])
print("Done")
print("Predicting")
prediction = predict(model, data)
print("Done")
print("Editing output.csv")
writeSubmitColumn(rawData, prediction)
print("Done")


