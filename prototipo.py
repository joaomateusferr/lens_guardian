import time
import requests
import random

url_measurements = 'http://ec2-18-228-191-79.sa-east-1.compute.amazonaws.com:8080/api/iot/medicoes'
device = 64
token = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJKb3NlIiwiZXhwIjoxNTc0MTYwMzAzfQ.4hmpCV9M6ZmsZcv7ZLGyRt8ta-BGUrRr2T0mopWLz8Y'

while(1):

    humidity = round(random.uniform(40.5,41.5),2)
    temperature = round(random.uniform(14.2,13.5),2)

    payload = '{\"device\": {\"id\": \"'+ str(device) +'\"}, \"humidity\": \"'+ str(humidity) +'\",\"temperature\": \"'+ str(temperature) +'\"}'
    headers = {'Content-Type': 'application/json','cache-control': 'no-cache', 'Authorization': token}

    try:
        response = requests.request("POST", url_measurements, data = payload, headers = headers)
        
        if (response.status_code == 200):
            print("Data Sent")
            print("H: "+str(humidity)+" | T: "+str(temperature)+"")
        else:
            print("Error While Sending Data")
    
    except:
        print("Error")
    
    time.sleep(60)




