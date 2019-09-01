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
led_red = 20
led_green = 26
interval = 60

time.sleep(10)

#http://razzpisampler.oreilly.com/ch07.html

GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_reset, GPIO.IN, pull_up_down = GPIO.PUD_UP)
reset  = GPIO.input(btn_reset)

GPIO.setup(led_white, GPIO.OUT)
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)

GPIO.output(led_white, False)
GPIO.output(led_red, False)
GPIO.output(led_green, False)

if (reset == False):

    GPIO.output(led_white, True)
    GPIO.output(led_red, True)
    GPIO.output(led_green, True)

    print("Reset ...\n")

    time.sleep(10)
    
    os.system("sudo raspi-config nonint do_boot_behaviour B4")
    os.system("sudo reboot")

else:

    ulr_file = open("ulr.txt", "r")
    ulr = ulr_file.readline()
    ulr_file.close()

    time.sleep(interval)

    while(1):
        
        humidity, temperature = Adafruit_DHT.read_retry(sensor_type, sensor_pin)
        
        if humidity is not None and temperature is not None:

            if (humidity > 60):
                GPIO.output(led_red, True)
                GPIO.output(led_green, False)
            else:
                GPIO.output(led_red, False)
                GPIO.output(led_green, True)

            print('Temp={0:0.1f}  Humidity={1:0.1f}%'.format(temperature, humidity))
            
            payload = "{\n\t\"umidade\": \""+ str(humidity) +"\",\n\"temperatura\": \""+ str(temperature) +"\"\n}"
            headers = {'Content-Type': "application/json",'cache-control': "no-cache"}

            response = requests.request("POST", url, data = payload, headers = headers)        
            
            if (response.status_code == 200):
                print("Data Sent\n")
                GPIO.output(led_white, True)
            else:
                print("Error While Sending Data\n")
                GPIO.output(led_white, False)
            
            time.sleep(interval)
        else:
            print('Failed to get reading')
            GPIO.output(led_white, False)
            time.sleep(interval)
