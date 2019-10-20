#!/usr/bin/python

import sys
import os
import time
import Adafruit_DHT
import RPi.GPIO as GPIO
import requests

GPIO.setwarnings(False)

sensor_type = Adafruit_DHT.DHT22
sensor_pin = 14
btn_reset = 21
led_white = 16
led_green = 26
interval = 5

internet = 'google.com'
url_measurements = 'http://ec2-18-228-191-79.sa-east-1.compute.amazonaws.com:8080/api/iot/medicoes'

time.sleep(10)

GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_reset, GPIO.IN, pull_up_down = GPIO.PUD_UP)
reset  = GPIO.input(btn_reset)

GPIO.setup(led_white, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)

GPIO.output(led_white, False)
GPIO.output(led_green, False)

time.sleep(10)

if (reset == False):
    GPIO.output(led_green, True)
    GPIO.output(led_white, True)

    print("Reset ...\n")

    time.sleep(10)
    
    #os.system("sudo raspi-config nonint do_boot_behaviour B4")
    #os.system("sudo reboot")

else:

    rep = os.system('ping -i 1 -c 3 ' + internet)

    if rep == 0:
        print ('Connected to the internet!')
    else:
        print ('No internet connection!')
        sys.exit()

    device_file = open("device.txt", "r")
    device = device_file.readline()
    device_file.close()

    token_file = open("token.txt", "r")
    token = token_file.readline()
    token_file.close()

    time.sleep(10)

    while(1):
        
        humidity, temperature = Adafruit_DHT.read_retry(sensor_type, sensor_pin)
        
        if humidity is not None and temperature is not None:

            if (humidity > 60):
                GPIO.output(led_green, False)
            else:
                GPIO.output(led_green, True)

            print('Temp={0:0.1f}  Humidity={1:0.1f}%'.format(temperature, humidity))

            payload = "{\"device\": {\"id\": \""+ str(device) +"\"}, \"humidity\": \""+ str(humidity) +"\",\"temperature\": \""+ str(temperature) +"\"}"
            headers = {'Content-Type': "application/json",'cache-control': "no-cache", 'Authorization': token}

            try:
                response = requests.request("POST", url_measurements, data = payload, headers = headers)

                if (response.status_code == 200):
                    print("Data Sent\n")
                    GPIO.output(led_white, True)
                else:
                    print("Error While Sending Data\n")
                    GPIO.output(led_white, False)
                    
            except:
                print("Error While Sending Data\n")
                
        else:
            print('Failed to get reading')
            GPIO.output(led_white, False)
        
        time.sleep(interval)