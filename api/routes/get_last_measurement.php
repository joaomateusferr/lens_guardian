<?php


	include '../settings/configuration_file.php';

	if (isset($_GET["id"])) {
		
		$Id = $_GET["id"];
		$Sql = "SELECT data_hora AS hora, temperatura, umidade, luminosidade FROM medicoes WHERE id_dispositivo = '$Id' AND MINUTE(data_hora) = 0 ORDER BY id_medicao DESC LIMIT 1";
		$Pdo = new PDO(Database::$Connection, Database::$User, Database::$Password);
		$Stm = $Pdo->query($Sql);
		$Result = $Stm->fetch();

		echo json_encode($Result);
	}
