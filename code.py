#!/usr/bin/python

import sys
import time
import Adafruit_DHT
import RPi.GPIO as GPIO
import requests

sensor_type = Adafruit_DHT.DHT22
sensor_pin = 14
btn_reset = 15
interval = 2

time.sleep(10)

#http://razzpisampler.oreilly.com/ch07.html

GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_reset, GPIO.IN, pull_up_down = GPIO.PUD_UP)
reset  = GPIO.input(btn_reset)

if (reset == False):

    startup = open("/etc/rc.local", "w+")
    startup.write('#Startup\nsudo python /home/pi/VinosIOT/inicial.py &\nexit 0')
    startup.close()
    
    os.system("sudo reboot")

else:

    ulr_file = open("ulr.txt", "r")
    ulr = f.read()
    ulr_file.close()

    time.sleep(interval)

    while(1):
        
        humidity, temperature = Adafruit_DHT.read_retry(sensor_type, sensor_pin)
        
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
