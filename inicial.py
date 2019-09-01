import os
import time
import requests
import sys

time.sleep(10)

os.chdir("/home/pi/")
os.system("sudo apt-get install git")

os.system("git clone https://github.com/adafruit/Adafruit_Python_DHT.git")
os.chdir("/home/pi/Adafruit_Python_DHT")
os.system("sudo python setup.py install") 
os.chdir("/home/pi/")

os.system("git clone git://github.com/kennethreitz/requests.git")
os.chdir("/home/pi/requests")
os.system("sudo python setup.py install")
os.chdir("/home/pi/")

os.system("git clone https://github.com/joaomateusferr/VinosIOT.git")

os.system("sudo apt-get install python-rpi.gpio python3-rpi.gpio")

os.system("clear")

print("Downloads done!\n")

url_login = 'http://ec2-18-228-191-79.sa-east-1.compute.amazonaws.com:8080/api/iot/singup'

print("Fill in the Vinos data!")

email = raw_input('Email: ')
password = raw_input('Password: ')

payload = "{\n\t\"email\": \""+ email +"\",\n\"senha\": \""+ password +"\"\n}"
headers = {'Content-Type': "application/json",'cache-control': "no-cache"}

#response = requests.request("POST", url_login, data = payload, headers = headers)

#devices = response.text

#selecionar qual dispositivo sera usado para gerar a ulr

ulr_file = open("ulr.txt", "w+")
ulr_file.write('http://ec2-18-228-191-79.sa-east-1.compute.amazonaws.com:8080/api/medicao')
ulr_file.close()

os.system("sudo echo '#!/bin/sh -e' | sudo tee /etc/rc.local")
os.system("sudo echo '#Startup' | sudo tee -a /etc/rc.local")
os.system("sudo echo 'sudo python /home/pi/VinosIOT/code.py &' | sudo tee -a /etc/rc.local")
os.system("sudo echo 'exit 0' | sudo tee -a /etc/rc.local")

os.system("sudo raspi-config nonint do_boot_behaviour B2")
os.system("sudo reboot")
