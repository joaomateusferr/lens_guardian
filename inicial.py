import os

print("Fill in the  WIFI data!")

ssid = raw_input('SSID: ')
wifi_password = raw_input('Password: ')

network = open("/etc/wpa_supplicant/wpa_supplicant.conf, "w+") raspberypi
network.write('ctrl_interface=DIR=/var/run/wpa_supplicant GROUP = netdev\nupdate_config = 1\n\nnetwork = {\n\tssid = "%s"\n\tpsk = "%s"\n}' % (ssid,wifi_password))
network.close()

url_login = 'http://ec2-18-228-191-79.sa-east-1.compute.amazonaws.com:8080/api/iot/singup'

print("Fill in the Vinos data!")

email = raw_input('Email: ')
password = raw_input('Password: ')

payload = "{\n\t\"email\": \""+ email +"\",\n\"senha\": \""+ password +"\"\n}"
headers = {'Content-Type': "application/json",'cache-control': "no-cache"}

response = requests.request("POST", url_login, data = payload, headers = headers)

devices = response.text

#selecionar qual dispositivo sera usado para gerar a ulr

ulr_file = open("ulr.txt", "w+")
ulr_file.write('http://ec2-18-228-191-79.sa-east-1.compute.amazonaws.com:8080/api/medicao')
ulr_file.close()

startup = open("/etc/rc.local", "w+")
startup.write('#Startup 2\nsudo python /home/pi/VinosIOT/code.py &\n')
startup.close()

os.system("sudo reboot")
