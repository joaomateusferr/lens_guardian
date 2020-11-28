#!/bin/bash

#Developer notes
#for this script to work correctly it must be run as root

BOOT_BEHAVIOUR=$1

#BOOT_BEHAVIOUR possible values
#B1 CLI 
#B2 CLI authenticated to pi user (PI OS Lite default)
#B3 GUI
#B4 GUI authenticated to pi user (PI OS Full default)


if [ $EUID -ne 0 ]; then #delete users and user's folder equire root privileges
    echo 'No root privileges detected!'
    echo 'Please, run this script as root'
else
    raspi-config nonint do_boot_behaviour $BOOT_BEHAVIOUR 
    reboot
fi