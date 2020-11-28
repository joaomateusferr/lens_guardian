#!/bin/bash

#Developer notes
#for this script to work correctly it must be run as root

BOOT_BEHAVIOUR=$1

#BOOT_BEHAVIOUR possible values
#B1 CLI 
#B2 CLI authenticated to pi user (PI OS Lite default)
#B3 GUI
#B4 GUI authenticated to pi user (PI OS Full default)

if [ $EUID -ne 0 ]; then #change the boot behaviour equire root privileges
    echo 'No root privileges detected!'
    echo 'Please, run this script as root'
else
    raspi-config nonint do_boot_behaviour $BOOT_BEHAVIOUR 

    if [ $? -eq 0 ] ; then
        echo "Boot behavior changed to $BOOT_BEHAVIOUR"
        echo 'Restarting raspberry pi to apply boot behaviour'
        reboot
    else 
        echo "Error while trying to change boot behavior to $BOOT_BEHAVIOUR"    
    fi
fi