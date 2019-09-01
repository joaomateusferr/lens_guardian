import os
import time
import requests
import sys
from termios import tcflush, TCIFLUSH

time.sleep(10)

tcflush(sys.stdin, TCIFLUSH)

print("Fill in the  WIFI data!")

ssid = raw_input('SSID: ')
wifi_password = raw_input('Password: ')

#os.system("sudo echo 'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev' | sudo tee /etc/wpa_supplicant/wpa_supplicant.conf")
#os.system("sudo echo 'update_config=1' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf")
#os.system("sudo echo 'country=BR' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf")
os.system("sudo echo '' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf")
os.system("sudo echo 'network = {' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf")
os.system("sudo echo 'ssid = " + str(ssid) + "' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf")
os.system("sudo echo 'psk = " + str(wifi_password) + "' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf")
os.system("sudo echo '}' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf")

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
os.system("sudo echo '#Startup 2' | sudo tee -a /etc/rc.local")
os.system("sudo echo 'sudo python /home/pi/VinosIOT/code.py &' | sudo tee -a /etc/rc.local")
os.system("sudo echo 'exit 0' | sudo tee -a /etc/rc.local")

os.system("sudo reboot")
