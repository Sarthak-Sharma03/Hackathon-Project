
# Import the Modules
from flask import Flask , render_template , request
from sklearn.preprocessing import LabelEncoder
import pickle
import numpy as np

# Define the Preprocessing Functions

def browserName(browser):
    browser_name = ""
    for index in range(0,len(browser)):
        if browser[index].isnumeric():
            break
        browser_name = browser_name + browser[index]
    return browser_name.strip()

# Open the Pickle Files
Model   = pickle.load(open("pickle files/dtModel.pkl" , "rb"))
Encoder = pickle.load(open("pickle files/Encoder.pkl" , "rb"))

# Create the Object of Label Encoder
encoder = LabelEncoder()

# Create the Lambda function for the Class Label
class_label = lambda x: "NOT DETECT" if x == 0 else "DETECT"


# Create the Object of the Flask
app = Flask(__name__)


# Create the First Decorator --> Main Page
@app.route("/")
def home_page():
    return render_template("homePage.html")


# Create the Second Decorator --> Input Data from User
@app.route("/input_data")
def user_input():
    return render_template("requestResult.html")


# Create the Third Decorator --> Find Results
@app.route("/process_request" , methods = ["POST" , "GET"])
def process_request():
    if request.method == "POST":
        login     = request.form["logintime"]
        user      = request.form["User"] 
        ip        = request.form["ip"] 
        country   = request.form["country"] 
        region    = request.form["region"] 
        city      = request.form["city"] 
        browser   = request.form["browser"] 
        device    = request.form["device"]

        # Get the Exect Browser Name
        browser = browserName(browser)

        # Convert the Enoder Form
        country = encoder.fit_transform([country])[0]
        region  = encoder.fit_transform([region])[0]
        city    = encoder.fit_transform([city])[0]
        browser = encoder.fit_transform([browser])[0]
        device = encoder.fit_transform([device])[0]

        # Predict the Result from Model
        vector = np.array([country , region , city , browser , device]).reshape((1,-1))
        prediction = Model.predict(vector)
        label = class_label(prediction[0])
        return  render_template("requestResult.html" , prediction = label)

# Run the Flask App
if "__main__" == __name__:
    app.run(debug=True)








