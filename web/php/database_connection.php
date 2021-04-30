<?php
    $server = "02c28591-2b52-488b-be87-a7c401519240.mysql.sequelizer.com";
    $user = "jbgtaiywodkfhkuw";
    $password = "Dz8eBEeDfUYUFCXc7LupKvUATxXv7QQmjZb8aarrZcDKxBmPX5tVYUahMEseQREw";
    $database = "db02c285912b52488bbe87a7c401519240";
    $connection = mysqli_connect($server,$user,$password,$database);
    mysqli_set_charset($connection, "utf8");
    
    if (mysqli_connect_errno()){
        die("Problem when trying to connect to the database: " . mysqli_connect_errno());
    } 
?>