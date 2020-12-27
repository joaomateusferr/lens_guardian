<?php
    $server = "54.87.126.46";
    $user = "jbgtaiywodkfhkuw";
    $password = "7mP8jw8FzHrHCzpKsiUFtSoqs6PLnKtjqcskusPZjNyMAft2Qhuw7CHn7xPmQvsW";
    $database = "db02c285912b52488bbe87a7c401519240";
    $connection = mysqli_connect($server,$user,$password,$database);
    mysqli_set_charset($connection, "utf8");
    
    if (mysqli_connect_errno()){
        die("Problem when trying to connect to the database: " . mysqli_connect_errno());
    } 
?>