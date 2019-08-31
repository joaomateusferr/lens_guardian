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

os.system("sudo apt-get install python-rpi.gpio python3-rpi.gpio")

os.system("sudo echo '#Startup' | sudo tee /etc/rc.local")
os.system("sudo echo 'sudo python /home/pi/VinosIOT/inicial.py &' | sudo tee -a /etc/rc.local")
os.system("sudo echo 'exit 0' | sudo tee -a /etc/rc.local")

os.system("sudo raspi-config nonint do_boot_behaviour B2")
os.system("sudo reboot")