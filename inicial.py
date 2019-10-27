import os
import shutil
import json
import time
import requests
import sys

time.sleep(2)

internet = 'google.com'
api = 'http://ec2-18-228-191-79.sa-east-1.compute.amazonaws.com'
url_login = 'http://ec2-18-228-191-79.sa-east-1.compute.amazonaws.com:8080/api/login'
ulr_user_data = 'http://ec2-18-228-191-79.sa-east-1.compute.amazonaws.com:8080/api/userinfo'
ulr_device = 'http://ec2-18-228-191-79.sa-east-1.compute.amazonaws.com:8080/api/iot/devices'

rep = os.system('ping -i 1 -c 3 ' + internet)

if rep == 0:
    print ('Connected to the internet!')
else:
    print ('No internet connection!')
    sys.exit()

os.chdir("/home/pi/")
os.system("sudo apt-get install git")

Adafruit_Python_DHT = os.path.isdir("/home/pi/Adafruit_Python_DHT")
if(Adafruit_Python_DHT):
    os.system("sudo rm -r Adafruit_Python_DHT")

os.system("git clone https://github.com/adafruit/Adafruit_Python_DHT.git")
os.chdir("/home/pi/Adafruit_Python_DHT")
os.system("sudo python setup.py install")

os.chdir("/home/pi/")

requests = os.path.isdir("/home/pi/requests")
if(requests):
    os.system("sudo rm -r requests")

os.system("git clone git://github.com/kennethreitz/requests.git")
os.chdir("/home/pi/requests")
os.system("sudo python setup.py install")

os.chdir("/home/pi/")

VinusIOT = os.path.isdir("/home/pi/VinusIOT")
if(VinusIOT):
    os.system("sudo rm -r VinusIOT")

os.system("git clone https://github.com/joaomateusferr/VinusIOT.git")

os.system("sudo apt-get install python-rpi.gpio python3-rpi.gpio")

os.chdir("/home/pi/VinusIOT")

os.system("clear")

print("All downloads and updates done!\n")     

print("Fill in the Vinos data!")

email = raw_input('Email: ')
password = raw_input('Password: ')

os.system("clear")

print("we are bringing your data, wait just a little longer ...")

try:
    payload_login = "{\n\t\"email\": \""+ email +"\",\n\t\"password\": \""+ password +"\"\n}"
    headers = {'Content-Type': "application/json",'cache-control': "no-cache"}
    
    response = requests.request("POST", url_login, data = payload_login, headers = headers)
    
    if (response.status_code == 200):
        token = response.headers['Authorization']
    else:
        sys.exit(0)
    
except:
    print("Login Error\n")
    sys.exit(0)
     
try:
    headers = {'Content-Type': "application/json",'cache-control': "no-cache", 'Authorization': token, 'email': email}
    response = requests.request("GET", ulr_user_data, headers = headers)
    
    if (response.status_code == 200):
        jsonToPython = json.loads(response.text)
        id_user = jsonToPython['listData'][0]['id']
    else:
        sys.exit(0)
except:
    print("Get User Id Error\n")
    sys.exit(0)

try:
    headers = {'Content-Type': "application/json",'cache-control': "no-cache", 'Authorization': token, 'id': str(id_user)}
    response = requests.request("GET", ulr_device, headers = headers)
    
    if (response.status_code == 200):
        jsonToPython = json.loads(response.text)
    else:
        sys.exit(0)
    
except:
    print("Get Devices Error\n")
    sys.exit(0)

isvalid = True

while(isvalid):

    for i, n in enumerate(jsonToPython['listData']):
        print(str(i+1) + ' - ' + str(n[1]) + ' - [ID -> ' + str(n[0]) + ']')

    try:
        device_number = int(raw_input('Select the device: ')) 
        isvalid = False
    except:
        os.system("clear")
        print('Enter an integer')
        isvalid = True
        continue
    
    if (device_number <= 0 or device_number > i+1):
        os.system("clear")
        print('Enter an valid number between 1 and ' + str(i+1))
        isvalid = True

device = str(jsonToPython['listData'][device_number-1][0])

condition = 'humidity > 60'

code_file = open("code.py", "w")
code_file.write('#!/usr/bin/python\n\n')
code_file.write('import sys\n')
code_file.write('import os\n')
code_file.write('import time\n')
code_file.write('import Adafruit_DHT\n')
code_file.write('import RPi.GPIO as GPIO\n')
code_file.write('import requests\n')
code_file.write('GPIO.setwarnings(False)\n\n')

code_file.write('sensor_type = Adafruit_DHT.DHT22\n')

code_file.write('device = '+ str(device) +'\n')
code_file.write("token = '"+ str(token) +"'\n")

code_file.write('sensor_pin = 14\n')
code_file.write('btn_reset = 26\n')
code_file.write('led_white = 12\n')
code_file.write('led_green = 16\n')
code_file.write('interval = 30 #seconds\n\n')

code_file.write("internet = 'google.com'\n")
code_file.write("url_measurements = 'http://ec2-18-228-191-79.sa-east-1.compute.amazonaws.com:8080/api/iot/medicoes'\n\n")

code_file.write('time.sleep(2)\n\n')

code_file.write('GPIO.setmode(GPIO.BCM)\n')
code_file.write('GPIO.setup(btn_reset, GPIO.IN, pull_up_down = GPIO.PUD_UP)\n')
code_file.write('reset  = GPIO.input(btn_reset)\n\n')

code_file.write('GPIO.setup(led_white, GPIO.OUT)\n')
code_file.write('GPIO.setup(led_green, GPIO.OUT)\n')

code_file.write('GPIO.output(led_white, False)\n')
code_file.write('GPIO.output(led_green, False)\n\n')

code_file.write('time.sleep(10)\n\n')

code_file.write('if (reset == False):\n')
code_file.write('\tGPIO.output(led_green, True)\n')
code_file.write('\tGPIO.output(led_white, True)\n\n')

code_file.write('\tprint("Reset ...")\n')

code_file.write('\ttime.sleep(5)\n')
    
code_file.write('\tos.system("sudo raspi-config nonint do_boot_behaviour B4")\n')
code_file.write('\tos.system("sudo reboot")\n')

code_file.write('else:\n')

code_file.write('\trep = os.system("ping -i 1 -c 3 " + internet)\n')

code_file.write('\tif rep == 0:\n')
code_file.write('\t\tprint ("Connected to the internet!")\n')
code_file.write('\telse:\n')
code_file.write('\t\tprint ("No internet connection!")\n')
code_file.write('\t\tsys.exit()\n\n')


code_file.write('\ttime.sleep(5)\n\n')
code_file.write('\twhile(1):\n\n')

code_file.write('\t\thumidity, temperature = Adafruit_DHT.read_retry(sensor_type, sensor_pin)\n\n')
code_file.write('\t\tif humidity is not None and temperature is not None:\n\n')

code_file.write('\t\t\tif('+condition+'):\n')
code_file.write('\t\t\t\tGPIO.output(led_green, False)\n')
code_file.write('\t\t\telse:\n')
code_file.write('\t\t\t\tGPIO.output(led_green, True)\n\n')

code_file.write("\t\t\tprint('Temp={0:0.1f}  Humidity={1:0.1f}%'.format(temperature, humidity))\n\n")

code_file.write("\t\t\tpayload = '{\"device\": {\"id\": \"'+ str(device) +'\"}, \"humidity\": \"'+ str(humidity) +'\",\"temperature\": \"'+ str(temperature) +'\"}'\n\n")
code_file.write("\t\t\theaders = {'Content-Type': 'application/json','cache-control': 'no-cache', 'Authorization': token}\n\n")

code_file.write('\t\t\ttry:\n\n')

code_file.write('\t\t\t\tresponse = requests.request("POST", url_measurements, data = payload, headers = headers)\n\n')

code_file.write('\t\t\t\tif (response.status_code == 200):\n')
code_file.write('\t\t\t\t\tprint("Data Sent")\n')
code_file.write('\t\t\t\t\tGPIO.output(led_white, True)\n\n')

code_file.write('\t\t\t\telse:\n')
code_file.write('\t\t\t\t\tprint("Error While Sending Data")\n')
code_file.write('\t\t\t\t\tGPIO.output(led_green, False)\n')
code_file.write('\t\t\t\t\tGPIO.output(led_white, False)\n\n')

code_file.write('\t\t\texcept:\n')
code_file.write('\t\t\t\tprint("Error While Sending Data")\n\n')
code_file.write('\t\t\t\tGPIO.output(led_white, False)\n')
code_file.write('\t\t\t\tGPIO.output(led_green, False)\n\n')

code_file.write('\t\telse:\n')
code_file.write('\t\t\tprint("Failed to get reading")\n')
code_file.write('\t\t\tGPIO.output(led_white, False)\n')
code_file.write('\t\t\tGPIO.output(led_green, False)\n\n')
code_file.write('\t\ttime.sleep(interval)\n')

code_file.close()

os.system("sudo echo '#!/bin/sh -e' | sudo tee /etc/rc.local")
os.system("sudo echo '#Startup' | sudo tee -a /etc/rc.local")
os.system("sudo echo 'sudo python /home/pi/VinusIOT/code.py &' | sudo tee -a /etc/rc.local")
os.system("sudo echo 'exit 0' | sudo tee -a /etc/rc.local")

os.system("sudo raspi-config nonint do_boot_behaviour B2")
os.system("sudo reboot")