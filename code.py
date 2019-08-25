#!/usr/bin/python

import sys
import time
import Adafruit_DHT
import requests #on Windows python -m pip install requests

sensor = Adafruit_DHT.DHT22
pin = 14
interval = 2

time.sleep(interval)


#f=open("guru99.txt","a+")
#Open the file back and read the contents
#f=open("guru99.txt", "r")
    #if f.mode == 'r':
    #   contents =f.read()
    #    print (contents)
    #or, readlines reads the individual line into a list
    #fl =f.readlines()
    #for x in fl:
    #print(x)

while(1):
    
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}  Humidity={1:0.1f}%'.format(temperature, humidity))
        
        url = "http://ec2-18-228-191-79.sa-east-1.compute.amazonaws.com:8080/api/medicao"
        payload = "{\n\t\"umidade\": \""+ str(humidity) +"\",\n\"temperatura\": \""+ str(temperature) +"\"\n}"
        headers = {'Content-Type': "application/json",'cache-control': "no-cache"}

        response = requests.request("POST", url, data=payload, headers=headers)        
        
        if (response.status_code == 200):
            print("Data Sent\n")
        else:
            print("Error While Sending Data\n")
        
        time.sleep(interval)
    else:
        print('Failed to get reading')
        time.sleep(interval)
