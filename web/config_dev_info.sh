#!/bin/bash

FULL_NAME=$1
EMAIL=$2

if [ -z "$FULL_NAME" ] || [ -z "$EMAIL" ];then

    if [ -z "$FULL_NAME" ];then
        echo 'Please, Fill in the second parameter with the developers full name'
    fi

    if [ -z "$EMAIL" ];then
        echo 'Please, Fill in the third parameter with the developers email'
    fi
    
else

    git config --global user.name "$FULL_NAME"
    git config --global user.email "$EMAIL"
    
fi

#run "git config --global --list" to check if everthing is set