import os
import shutil
import json
import time
import requests
import sys

time.sleep(10)

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

dht_lib = os.path.exists("./Adafruit_Python_DHT")

if(dht_lib):
    shutil.rmtree("Adafruit_Python_DHT")

os.system("git clone https://github.com/adafruit/Adafruit_Python_DHT.git")
os.chdir("/home/pi/Adafruit_Python_DHT")
os.system("sudo python setup.py install")

os.chdir("/home/pi/")

requests_lib = os.path.exists("./requests")

if(requests_lib):
    shutil.rmtree("requests")

os.system("git clone git://github.com/kennethreitz/requests.git")
os.chdir("/home/pi/requests")
os.system("sudo python setup.py install")

os.chdir("/home/pi/")

vinos_lib = os.path.exists("./VinusIOT")

if(vinos_lib):
    shutil.rmtree("VinusIOT")

os.system("git clone https://github.com/joaomateusferr/VinusIOT.git")

os.system("sudo apt-get install python-rpi.gpio python3-rpi.gpio")

os.system("clear")

print("All downloads and updates done!\n")     

print("Fill in the Vinos data!")

email = raw_input('Email: ')
password = raw_input('Password: ')

rep = os.system('ping -i 1 -c 3 ' + api)

if rep == 0:
    print ('API online!')
else:
    print ('API offline!\nTry agan later!')
    sys.exit()

try:
    payload_login = "{\n\t\"email\": \""+ email +"\",\n\t\"password\": \""+ password +"\"\n}"
    headers = {'Content-Type': "application/json",'cache-control': "no-cache"}
    
    response = requests.request("POST", url_login, data = payload_login, headers = headers)
    
    token = response.headers['Authorization']
    os.chdir("/home/pi/VinusIOT/")
    token_file = open("token.txt", "w+")
    token_file.write(token)
    token_file.close()
    
except:
    print("Login Error\n")
    sys.exit()
     
try:
    headers = {'Content-Type': "application/json",'cache-control': "no-cache", 'Authorization': token, 'email': email}
    response = requests.request("GET", ulr_user_data, headers = headers)
    jsonToPython = json.loads(response.text)
    id_user = jsonToPython['listData'][0][0]

except:
    print("Get User Id Error\n")
    sys.exit()

try:
    headers = {'Content-Type': "application/json",'cache-control': "no-cache", 'Authorization': token, 'id': str(id_user)}
    response = requests.request("GET", ulr_device, headers = headers)
    jsonToPython = json.loads(response.text)
except:
    print("Get Devices Error\n")
    sys.exit()

os.system("clear")

isvalid = True

while(isvalid):

    for i, n in enumerate(jsonToPython['listData']):
        print(str(i+1) + ' - ' + str(n[1]) + ' - [ID -> ' + str(n[0]) + ']')

    try:
        device_number = int(input('Select the device: ')) 
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

device_file = open("device.txt", "w+")
device_file.write(str(jsonToPython['listData'][device_number-1][0]))
device_file.close()

os.system("sudo echo '#!/bin/sh -e' | sudo tee /etc/rc.local")
os.system("sudo echo '#Startup' | sudo tee -a /etc/rc.local")
os.system("sudo echo 'sudo python /home/pi/VinusIOT/code.py &' | sudo tee -a /etc/rc.local")
os.system("sudo echo 'exit 0' | sudo tee -a /etc/rc.local")

#os.system("sudo raspi-config nonint do_boot_behaviour B2")
#os.system("sudo reboot")