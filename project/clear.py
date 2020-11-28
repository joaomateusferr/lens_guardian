import os

Adafruit_Python_DHT = os.path.isdir("/home/pi/Adafruit_Python_DHT")
if(Adafruit_Python_DHT):
    os.system("sudo rm -r Adafruit_Python_DHT")

requests = os.path.isdir("/home/pi/requests")
if(requests):
    os.system("sudo rm -r requests")

VinusIOT = os.path.isdir("/home/pi/VinusIOT")
if(VinusIOT):
    os.system("sudo rm -r VinusIOT")