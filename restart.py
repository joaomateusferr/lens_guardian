import os

os.system("sudo raspi-config nonint do_boot_behaviour B2")
os.system("sudo reboot")