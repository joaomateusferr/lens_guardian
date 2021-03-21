
#!/bin/bash

if [ $EUID -ne 0 ]; then #this screipt equire root privileges
    echo 'No root privileges detected!'
    echo 'Please, run this script as root'
else
    apt-get update

    echo -ne "y\n" | sudo apt-get install apache2 php libapache2-mod-php
    echo -ne "y\n" | sudo apt-get install php-soap php-xml php-curl php7.3-opcache php-gd php-sqlite3 php-mbstring php-mysql

    a2dismod mpm_event
    a2dismod mpm_worker
    a2enmod  mpm_prefork
    a2enmod  rewrite
    a2enmod  php7.3

    echo "" >> /etc/php/7.2/apache2/php.ini
    echo "error_log = /tmp/php_errors.log" >> /etc/php/7.3/apache2/php.ini
    echo "display_errors = On"             >> /etc/php/7.3/apache2/php.ini
    echo "memory_limit = 256M"             >> /etc/php/7.3/apache2/php.ini
    echo "max_execution_time = 120"        >> /etc/php/7.3/apache2/php.ini
    echo "error_reporting = E_ALL"         >> /etc/php/7.3/apache2/php.ini
    echo "file_uploads = On"               >> /etc/php/7.3/apache2/php.ini
    echo "post_max_size = 100M"            >> /etc/php/7.3/apache2/php.ini
    echo "upload_max_filesize = 100M"      >> /etc/php/7.3/apache2/php.ini
    echo "session.gc_maxlifetime = 14000"  >> /etc/php/7.3/apache2/php.ini

    #echo "display_errors = Off" >> /etc/php/7.3/apache2/php.ini
    #echo "error_reporting = E_ALL & ~E_DEPRECATED & ~E_STRICT & ~E_NOTICE" >> /etc/php/7.3/apache2/php.ini

    sudo service apache2 restart
    sudo apt install git
    sudo chmod -R 777 /var/www/html/
    echo "<?php phpinfo(); ?>" >> /var/www/html/index.php
    rm -rf /var/www/html/index.html
fi