import os
import shutil
import time
#import requests
import sys

server = 'google.com'

rep = os.system('ping -i 1 -c 3  ' + server)

if rep == 0:
    print ('server is up')
else:
    print ('server is down')
    sys.exit()



print("All downloads and updates done!\n")     

url_login = 'http://ec2-18-228-191-79.sa-east-1.compute.amazonaws.com:8080/api/login'

print("Fill in the Vinos data!")

email = raw_input('Email: ')
password = raw_input('Password: ')

payload = "{\n\t\"email\": \""+ email +"\",\n\"senha\": \""+ password +"\"\n}"
headers = {'Content-Type': "application/json",'cache-control': "no-cache"}

try:
    response = requests.request("POST", url_login, data = payload, headers = headers)

except:
    print("Response Error\n")

token = '**************'

#os.chdir("/home/pi/VinusIOT/")
token_file = open("token.txt", "w+")
token_file.write(token)
token_file.close()

#devices = response.text

#selecionar qual dispositivo sera usado para gerar a ulr

url_device = 'aaaaaaaaaaa'

url_file = open("url.txt", "w+")
url_file.write(url_device)
url_file.close()
