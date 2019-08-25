#!/usr/bin/python

import sys
import time
import Adafruit_DHT
import requests

sensor = Adafruit_DHT.DHT22
pin = 14
btn_reset = 15
interval = 2

time.sleep(10)

reset = GPIO.input(btn_reset)

if (reset == 1):

    startup = open("/etc/rc.local", "w+")
    startup.write('#Startup 2\nsudo python /home/pi/VinosIOT/code.py &\n')
    startup.close()
    
    os.system("sudo reboot")

else:

    ulr_file = open("ulr.txt", "r")
    ulr = f.read()
    ulr_file.close()

    time.sleep(interval)

    while(1):
        
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        
        if humidity is not None and temperature is not None:

            print('Temp={0:0.1f}  Humidity={1:0.1f}%'.format(temperature, humidity))
            
            payload = "{\n\t\"umidade\": \""+ str(humidity) +"\",\n\"temperatura\": \""+ str(temperature) +"\"\n}"
            headers = {'Content-Type': "application/json",'cache-control': "no-cache"}

            response = requests.request("POST", url, data = payload, headers = headers)        
            
            if (response.status_code == 200):
                print("Data Sent\n")
            else:
                print("Error While Sending Data\n")
            
            time.sleep(interval)
        else:
            print('Failed to get reading')
            time.sleep(interval)
