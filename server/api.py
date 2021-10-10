import pickle
from flask import Flask, request
from flask_cors import CORS, cross_origin
import pandas as pd
import numpy as np
import json
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/predict', methods=['GET', 'POST'])
def welcome():
    data = request.get_json()
    missing_value = ["N/a", "na", np.nan]
    df = pd.read_csv("server/data.csv", na_values=missing_value)
    df = df.replace(r'^\s*$', np.nan, regex=True)
    df.isnull().sum()
    df = df.dropna()
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(df[['Experience']])
    df[['Experience']] = scaled
    df['Awards'] = 60*df['Padma_Vibhushan']+50*df['Padma_Bhushan']+40*df['Padma_Shri'] + \
        30*df['Dhanvantari_Award']+20 * \
        df['BC_Roy_National_Award']+10*df['Other_Awards']
    scaled2 = scaler.fit_transform(df[['Awards']])
    df[['Awards']] = scaled2
    df.drop('Padma_Vibhushan',
            axis='columns', inplace=True)
    df.drop('Padma_Bhushan',
            axis='columns', inplace=True)
    df.drop('Padma_Shri',
            axis='columns', inplace=True)
    df.drop('Dhanvantari_Award',
            axis='columns', inplace=True)
    df.drop('BC_Roy_National_Award',
            axis='columns', inplace=True)
    df.drop('Other_Awards',
            axis='columns', inplace=True)
    km = KMeans(n_clusters=4)
    y_predict = km.fit_predict(df[['Awards', 'Experience']])
    df['cluster'] = y_predict
    Doctor_Name = data["data"]["Name"]
    specialisaton = data["data"]["Specialisation"]
    city = data["data"]["City"]
    doctor_Experience = int(data["data"]["Experience"])
    doctor_Awards_Points = int(
        data["data"]["Award"])
    Experience_Normalised = doctor_Experience/70
    Awards_Point_Normalised = doctor_Awards_Points/100
    predicted_user = km.predict(
        [[Experience_Normalised, Awards_Point_Normalised]])
    final = []
    if(predicted_user < 4):  # for outliers
        for i in range((df.shape[0])):
            if(str(df.iloc[i, 2]).count(city) > 0 and str(df.iloc[i, 1]).count(specialisaton) > 0 and df.iloc[i, 6] <= predicted_user and Experience_Normalised < float(df.iloc[i, 4]) and Awards_Point_Normalised < float(df.iloc[i, 5])):
                final.append(df.iloc[i])
    else:
        return({"final": "Sorry! We cannot match these in data set"})
    if(len(final)):
        hi = []
        for i in final:
            x = {"Name": i["Name"], "Specialisation": i["Specialisation"],
                 "City": i["City"], "Experience": i["Experience"], "Award": i["Awards"]}
            hi.append(x)
        return({"final": hi})
    else:
        return({"final": "Your Doctor is the best in your Area."})
    return({"final": hi})


if __name__ == '__main__':
    app.run()
