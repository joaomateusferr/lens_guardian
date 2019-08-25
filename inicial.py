import os

print("Preencha os dados da sua rede WIFI")

ssid = raw_input('SSID: ')
senha = raw_input('Senha: ')

#network = open("/etc/wpa_supplicant/wpa_supplicant.conf, "w+") raspberypi
network = open("wpa_supplicant.conf", "w+")
network.write('ctrl_interface=DIR=/var/run/wpa_supplicant GROUP = netdev\nupdate_config = 1\n\nnetwork = {\n\tssid = "%s"\n\tpsk = "%s"\n}' % (ssid,senha))
network.close()

#login no vinos aqui

#selecionar qual dispositivo sera usado

ulr_file = open("ulr.txt", "w+")
ulr_file.write('http://ec2-18-228-191-79.sa-east-1.compute.amazonaws.com:8080/api/medicao')
ulr_file.close()

#startup = open("/etc/rc.local", "w+")
#startup.write('#Startup 2\nsudo python /home/pi/VinosIOT/code.py &\n')
#startup.close()

#os.system("sudo reboot")
