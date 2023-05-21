# Hackathon-Project
**Project Description:**

The Anomaly Detection System is a web-based application that finds the most suitable model for anomaly detection according to the data and uses a trained state of that model to detect anomalies in further data provided by the user. The data used in current project is of user login activities. It analyzes various attributes such as login timestamp, user ID, IP address, country, region, city, browser name, and device type to determine if a login attempt is normal or potentially suspicious. The system provides real-time predictions and explanations for detected anomalies.

**Key Features:**

1) Anomaly Detection: The system uses a trained Decision Tree Classifier to predict if a login attempt is normal or an anomaly.
2) Attribute Analysis: It analyzes various attributes associated with user login activities to identify patterns and potential anomalies.
3) Real-time Prediction: The system provides instant predictions based on the provided user login information.
4) Anomaly Explanation: In addition to the detection result, the system provides explanations about the detected anomalies, including the specific attributes that contributed to the anomaly.
5) Web-based Interface: The application offers a user-friendly web interface for easy interaction and input of user login information.

**Installation Instructions:**

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

**Usage Example:**

1) Open your web browser and navigate to the application's URL.
2) Fill in the required fields, such as login timestamp, user ID, IP address, country, region, city, browser name, and device type or upload multiple records for simultaneous prediction.
3) Click the "Predict" button.
4) The system will process the input and provide a prediction (either "DETECT" or "NOT DETECTED") based on the anomaly detection result.
5) If an anomaly is detected, the system will also provide an explanation that highlights the specific attributes contributing to the anomaly.

**Technical Documentation**

**Data Preparation:**

The data preparation phase is an important step in building an anomaly detection system. It involves loading the dataset, checking for missing values and duplicates, and gaining an understanding of the dataset's structure.

1) Importing Libraries.
2) Loading the Dataset. (Please note the dataset currently uploaded in the repository is only a sample of the actual raw data.)
3) Dataset Exploration:
   
   a) The first few rows of the dataset are displayed using the head function.
   
   b) The shape of the dataset is printed using the shape attribute, which shows the number of rows and columns.
   
   c) The number of duplicated data instances in the dataset is calculated using the duplicated function.
   
   d) The count of missing values in each column is obtained using the isnull function.
   
   e) The dataset's information, including the number of non-null values and data types of each column, is displayed using the info function.
   
   f) The number of unique values in important columns of dataset are also measured.
   
   g) This initial data exploration and preprocessing step helps in understanding the structure of the dataset, identifying missing values, duplicates, and potential data         issues that need to be addressed before building the anomaly detection model.
 
**Data Preprocessing:**

Handling Missing Values-

1) Missing values in the "Region" column are filled with the most common region, "Oslo County".
2) The sign "-" in the "Region" column is replaced with "Oslo County".
3) Missing values in the "City" column are filled with "Oslo".
4) The sign "-" in the "City" column is replaced with "Oslo".
5) Missing values in the "Device Type" column are filled with "mobile".

Handling Categorical Data-

1) The "Browser Name and Version" column is split into "Browser Name" and "Browser Version" columns.
2) A function is defined to extract the browser name from the "Browser Name and Version" column.
3) The function is applied to create the "Browser Name" column.
4) Label encoding is applied to convert categorical columns ("Country", "Region", "City", "Browser Name", "Device Type") into numerical form.
5) Transformed columns with prefix "Trans_" are created.

Handling Binary Target Variable -
1) The "Login Successful" column is converted into a numerical column using label encoding.

**Feature Engineering:**

1) The dataset is split into independent (X) and dependent (Y) matrices.
2) The independent matrix (X) consists of selected columns (e.g., "Country", "Region", "City", "Browser Name", "Device Type").
3) The dependent matrix (Y) consists of the "Login Successful" column.
4) The data in the independent matrix is normalized using MinMaxScaler to scale the values between 0 and 1.

**Model Selection:**

1) Logistic Regression, Decision Tree Classifier, and Support Vector Classifier models are chosen for anomaly detection.

**Model Evaluation:**

1) The predict_result function is used to train the models, make predictions on the testing set, and evaluate model performance.
2) Accuracy scores, classification reports, and confusion matrices are obtained for each model.
3) The results provide insights into the performance of each model in detecting anomalies and help in selection of best model for the data.

**Model Deployment:**

1) The trained Decision Tree Classifier model is saved using the pickle.dump function.
2) The encoder object used for label encoding is also saved using pickle.dump.
3) These saved models can be loaded and used for future anomaly detection tasks.


