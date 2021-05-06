<?php
    require_once("database_connection.php");

    if (isset($_GET["email"])) 
    {
        $email = $_GET["email"];
        $senha = $_GET["senha"];

        $query_login = "SELECT * 
                       FROM usuarios
                       WHERE email = '$email' 
                       AND senha = '$senha'";
        
        $login = mysqli_query($connection,$query_login);
        $info = mysqli_fetch_assoc($login);
            
        if (!empty($info))
        {
            if (!isset($_SESSION))
            {
                session_start();    
                $_SESSION["id_usuario"] = $info["id_usuario"];
                $_SESSION["email"] = $info["email"];
                echo "sucesso";
            }
        }
        else
        {
            echo "erro";
        }
    }
    $login->close();
    mysqli_close($connection);
?>