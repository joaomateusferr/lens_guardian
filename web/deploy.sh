
#!/bin/bash

PRODUCTION_ENVIRONMENT=$1
PHP_DIR='/etc/php/'

if [ $(id -u) -ne 0 ]; then #this screipt equire root privileges (root id is 0)
    echo 'No root privileges detected!'
    echo 'Please, run this script as root'
else

    if [ -z "$PRODUCTION_ENVIRONMENT" ];then
        PRODUCTION_ENVIRONMENT=0
    fi

    apt-get update

    sudo apt-get install apache2 php libapache2-mod-php
    sudo apt-get install php-soap php-xml php-curl php-opcache php-gd php-sqlite3 php-mbstring php-mysql
    sudo apt install git

    git config --global core.fileMode false

    if [ ! -e $PHP_DIR ];then
        echo 'PHP not installed'
    else
        NEWER_VERSION_INSTALLED=$(ls -1r $PHP_DIR | head -1)

        if [ -z "$NEWER_VERSION_INSTALLED" ];then
            echo 'No version found!'
        else
            echo "Changing the settings for the version $NEWER_VERSION_INSTALLED"

            a2dismod mpm_event
            a2dismod mpm_worker
            a2enmod  mpm_prefork
            a2enmod  rewrite
            a2enmod  $NEWER_VERSION_INSTALLED

            PHP_INI_PATH="$PHP_DIR$NEWER_VERSION_INSTALLED/apache2/php.ini"

            echo "" >> $PHP_INI_PATH
            echo "error_log = /tmp/php_errors.log" >> $PHP_INI_PATH
            echo "display_errors = On"             >> $PHP_INI_PATH
            echo "memory_limit = 256M"             >> $PHP_INI_PATH
            echo "max_execution_time = 120"        >> $PHP_INI_PATH
            echo "error_reporting = E_ALL"         >> $PHP_INI_PATH
            echo "file_uploads = On"               >> $PHP_INI_PATH
            echo "post_max_size = 100M"            >> $PHP_INI_PATH
            echo "upload_max_filesize = 100M"      >> $PHP_INI_PATH
            echo "session.gc_maxlifetime = 14000"  >> $PHP_INI_PATH

            if [ $PRODUCTION_ENVIRONMENT -eq 1 ];then
                echo "display_errors = Off" >> $PHP_INI_PATH
                echo "error_reporting = E_ALL & ~E_DEPRECATED & ~E_STRICT & ~E_NOTICE" >> $PHP_INI_PATH
            fi

            sudo service apache2 restart
            sudo apt install git
            sudo chmod -R 777 /var/www/html/
            echo "<?php phpinfo(); ?>" >> /var/www/html/index.php
            rm -rf /var/www/html/index.html
        fi
    fi
fi

# After cloning the git repository don't forget to run the command "" in the repository folder to avoid problems with file permissions