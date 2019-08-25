import os

#os.chdir("/home/pi/")
#os.system("sudo apt-get install git")
#os.system("git clone https://github.com/adafruit/Adafruit_Python_DHT.git")
#os.chdir("/home/pi/Adafruit_Python_DHT")
#os.system("sudo python setup.py install") 
#os.chdir("/home/pi/")
#os.system("clone git://github.com/kennethreitz/requests.git")
#os.chdir("/home/pi/requests")
#os.system("sudo python setup.py install")

print("Preencha os dados da sua rede WIFI")

ssid = raw_input('SSID: ')
senha = raw_input('Senha: ')

network = open("wifi.conf", "w+")
network.write('\nnetwork = {\n\tssid = "%s"\n\tpsk = "%s"\n}' % (ssid,senha))
network.close()

config = open("wifi_config.txt", "w+")
config.write('1')
config.close()

startup = open("/etc/rc.local", "w+")
startup.write('#Startup 2\nsudo python /home/pi/code.py &\n')



#https://askubuntu.com/questions/294257/connect-to-wifi-network-through-ubuntu-terminal
#https://www.cyberciti.biz/faq/unix-howto-read-line-by-line-from-file/

    #f=open("guru99.txt","a+")
    #Open the file back and read the contents
    #f=open("guru99.txt", "r")
    #if f.mode == 'r':
    #   contents =f.read()
    #    print (contents)
    #or, readlines reads the individual line into a list
    #fl =f.readlines()
    #for x in fl:
    #print(x)
