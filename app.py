import numpy as np
import pandas as pd
import hashlib
import joblib
import dill
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
app = Flask(__name__)

encoding = joblib.load('encoder.joblib')
scaler = joblib.load('scaler.pkl')
AutoE = joblib.load('AutoE.pkl')
ensemble = joblib.load('ensemble.pkl')

with open('pre_pro1.pkl', 'rb') as file:
    pre_pro1 = dill.load(file)

with open('pre_pro2.pkl', 'rb') as file:
    pre_pro2 = dill.load(file)
    
with open('pipe.pkl', 'rb') as file:
    pipe = dill.load(file)

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", methods = ["POST"])
def predict():
    # Multiple upto 4 entries
    Login_Timestamp1 = request.form['Login_Timestamp1']
    User_ID1 = request.form['User_ID1']
    IP_Address1 = request.form['IP_Address1']
    Country1 = request.form['Country1']
    Region1 = request.form['Region1']
    City1 = request.form['City1']
    Browser_Name_and_Version1 = request.form['Browser_Name_and_Version1']
    Device_Type1 = request.form['Device_Type1']
    Login_Successful1 = request.form['Login_Successful1']

    Login_Timestamp2 = request.form['Login_Timestamp2']
    User_ID2 = request.form['User_ID2']
    IP_Address2 = request.form['IP_Address2']
    Country2 = request.form['Country2']
    Region2 = request.form['Region2']
    City2 = request.form['City2']
    Browser_Name_and_Version2 = request.form['Browser_Name_and_Version2']
    Device_Type2 = request.form['Device_Type2']
    Login_Successful2 = request.form['Login_Successful2']

    Login_Timestamp3 = request.form['Login_Timestamp3']
    User_ID3 = request.form['User_ID3']
    IP_Address3 = request.form['IP_Address3']
    Country3 = request.form['Country3']
    Region3 = request.form['Region3']
    City3 = request.form['City3']
    Browser_Name_and_Version3 = request.form['Browser_Name_and_Version3']
    Device_Type3 = request.form['Device_Type3']
    Login_Successful3 = request.form['Login_Successful3']

    Login_Timestamp4 = request.form['Login_Timestamp4']
    User_ID4 = request.form['User_ID4']
    IP_Address4 = request.form['IP_Address4']
    Country4 = request.form['Country4']
    Region4 = request.form['Region4']
    City4 = request.form['City4']
    Browser_Name_and_Version4 = request.form['Browser_Name_and_Version4']
    Device_Type4 = request.form['Device_Type4']
    Login_Successful4 = request.form['Login_Successful4']


    dic1 = { 'Login Timestamp': Login_Timestamp1, 
            'User ID': int(User_ID1), 
            'IP Address': IP_Address1, 
            'Country': Country1, 
            'Region': Region1, 
            'City': City1, 
            'Browser Name and Version': Browser_Name_and_Version1, 
            'Device Type': Device_Type1, 
            'Login Successful': int(Login_Successful1)}

    dic2 = {
        'Login Timestamp': Login_Timestamp2,
        'User ID': int(User_ID2),
        'IP Address': IP_Address2,
        'Country': Country2,
        'Region': Region2,
        'City': City2,
        'Browser Name and Version': Browser_Name_and_Version2,
        'Device Type': Device_Type2,
        'Login Successful': int(Login_Successful2)
    }


    dic3 = {
    'Login Timestamp': Login_Timestamp3,
    'User ID': int(User_ID3),
    'IP Address': IP_Address3,
    'Country': Country3,
    'Region': Region3,
    'City': City3,
    'Browser Name and Version': Browser_Name_and_Version3,
    'Device Type': Device_Type3,
    'Login Successful': int(Login_Successful3)}

    dic4 = {
        'Login Timestamp': Login_Timestamp4,
        'User ID': int(User_ID4),
        'IP Address': IP_Address4,
        'Country': Country4,
        'Region': Region4,
        'City': City4,
        'Browser Name and Version': Browser_Name_and_Version4,
        'Device Type': Device_Type4,
        'Login Successful': int(Login_Successful4)
    }
    
    prediction1 = pipe(dic1)
    prediction2 = pipe(dic2)
    prediction3 = pipe(dic3)
    prediction4 = pipe(dic4)
    
    return render_template("index.html", prediction_text = "The predictions are {} \n, {} \n, {} \n, {} \n".format(prediction1, prediction2, prediction3, prediction4))

if __name__ == "__main__":
    app.run()
