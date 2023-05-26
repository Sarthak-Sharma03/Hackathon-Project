url = "https://chitkara-hackathon.s3.ap-south-1.amazonaws.com/Chitkara_Anomaly_Detection.zip"
wget.download(url)

from zipfile import ZipFile

with ZipFile("C:\Users\lenovo\Downloads\Send", 'r') as zObject:
    zObject.extractall(path="C:\Users\lenovo\Downloads\Send\data")