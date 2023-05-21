# Hackathon-Project
Project Description:

The Anomaly Detection System is a web-based application that finds the most suitable model for anomaly detection according to the data and uses a trained state of that model to detect anomalies in further data provided by the user. The data used in current project is of user login activities. It analyzes various attributes such as login timestamp, user ID, IP address, country, region, city, browser name, and device type to determine if a login attempt is normal or potentially suspicious. The system provides real-time predictions and explanations for detected anomalies.

Key Features:

1) Anomaly Detection: The system uses a trained Decision Tree Classifier to predict if a login attempt is normal or an anomaly.
2) Attribute Analysis: It analyzes various attributes associated with user login activities to identify patterns and potential anomalies.
3) Real-time Prediction: The system provides instant predictions based on the provided user login information.
4) Anomaly Explanation: In addition to the detection result, the system provides explanations about the detected anomalies, including the specific attributes that contributed to the anomaly.
5) Web-based Interface: The application offers a user-friendly web interface for easy interaction and input of user login information.

Installation Instructions:

1) Clone the repository from GitHub: git clone https://github.com/Sarthak-Sharma03/Hackathon-Project
2) Navigate to the project directory: cd Hackathon-Project
3) Create a virtual environment (optional): python -m venv venv
4) Activate the virtual environment:
   a) For Windows: venv\Scripts\activate
   b) For Linux/Mac: source venv/bin/activate
5) Install the required dependencies: pip install numpy pandas seaborn matplotlib scikit-learn Flask
6) Run the application: python app.py
7) Access the application through your web browser at the active URL.

Please note that the above steps assume you have Python and Git installed on your system.

Usage Example:

1) Open your web browser and navigate to the application's URL.
2) Fill in the required fields, such as login timestamp, user ID, IP address, country, region, city, browser name, and device type or upload multiple records for simultaneous prediction.
3) Click the "Predict" button.
4) The system will process the input and provide a prediction (either "DETECT" or "NOT DETECTED") based on the anomaly detection result.
5) If an anomaly is detected, the system will also provide an explanation that highlights the specific attributes contributing to the anomaly.

Technical Documentation:

Data Preparation

The data preparation phase is an important step in building an anomaly detection system. It involves loading the dataset, handling missing values, checking for duplicates, and gaining an understanding of the dataset's structure.

1) Importing Libraries.
2) Loading the Dataset. (Please note the dataset currently uploaded in the repository is only a sample of the actual raw data.)
3) Dataset Exploration:
   
   a) The first few rows of the dataset are displayed using the head function.
   
   b) The shape of the dataset is printed using the shape attribute, which shows the number of rows and columns.
   c) The number of duplicated data instances in the dataset is calculated using the duplicated function.
   d) The count of missing values in each column is obtained using the isnull function.
   e) The dataset's information, including the number of non-null values and data types of each column, is displayed using the info function.
   f) The number of unique values in important columns of dataset are also measured.
   g) This initial data exploration and preprocessing step helps in understanding the structure of the dataset, identifying missing values, duplicates, and potential data      issues that need to be addressed before building the anomaly detection model.
 
Next, we will proceed with the data preprocessing and feature engineering steps.

