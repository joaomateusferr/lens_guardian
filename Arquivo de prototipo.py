import time
import requests

device = 64
token = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJKb3NlIiwiZXhwIjoxNTc0MTYwMzAzfQ.4hmpCV9M6ZmsZcv7ZLGyRt8ta-BGUrRr2T0mopWLz8Y'

while(1):

    humidity = 
    temperature = 

    payload = '{\"device\": {\"id\": \"'+ str(device) +'\"}, \"humidity\": \"'+ str(humidity) +'\",\"temperature\": \"'+ str(temperature) +'\"}'
    headers = {'Content-Type': 'application/json','cache-control': 'no-cache', 'Authorization': token}

    try:
        response = requests.request("POST", url_measurements, data = payload, headers = headers)
        
        if (response.status_code == 200):
            print("Data Sent")
        else:
            print("Error While Sending Data")
    
    except:
        print("Error")
    
    time.sleep(60)




