import os

os.chdir("/home/pi/")
os.system("sudo apt-get install git")

os.system("git clone https://github.com/adafruit/Adafruit_Python_DHT.git")
os.chdir("/home/pi/Adafruit_Python_DHT")
os.system("sudo python setup.py install") 
os.chdir("/home/pi/")

os.system("clone git://github.com/kennethreitz/requests.git")
os.chdir("/home/pi/requests")
os.system("sudo python setup.py install")
os.chdir("/home/pi/")

os.system("git clone https://github.com/joaomateusferr/VinosIOT.git")

startup = open("/etc/rc.local", "w+")
startup.write('#Startup\nsudo python /home/pi/VinosIOT/inicial.py &\nexit 0')
startup.close()

os.system("sudo raspi-config nonint do_boot_behaviour B2")
os.system("sudo reboot")