<?php
    $server = "";
    $user = "";
    $password = "";
    $database = "";
    $connection = mysqli_connect($server,$user,$password,$database);
    mysqli_set_charset($connection, "utf8");
    
    if (mysqli_connect_errno()){
        die("Problem when trying to connect to the database: " . mysqli_connect_errno());
    } 
?>