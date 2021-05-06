#!/bin/bash

#Developer notes
#for this script to work correctly it must be run as root

if [ $(id -u) -ne 0 ]; then #delete folders equire root privileges (root id is 0)
    echo 'No root privileges detected!'
    echo 'Please, run this script as root'
else

    if [ -e "/home/pi/Adafruit_Python_DHT" ]; then 
        rm -r /home/pi/Adafruit_Python_DHT

        if [ $? -eq 0 ] ; then
            echo 'Adafruit_Python_DHT - deleted'
        else 
            echo 'Error while deleting Adafruit_Python_DHT'    
        fi
    fi

    if [ -e "/home/pi/requests" ]; then 
        rm -r /home/pi/requests

        if [ $? -eq 0 ] ; then
            echo 'requests - deleted'
        else 
            echo 'Error while deleting requests'    
        fi
    fi

    if [ -e "/home/pi/lens_guardian" ]; then 
        rm -r /home/pi/lens_guardian

        if [ $? -eq 0 ] ; then
            echo 'lens_guardian - deleted'
        else 
            echo 'Error while deleting lens_guardian'    
        fi
    fi

fi
