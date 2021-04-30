<?php
	require_once("database_connection.php");

	if (isset($_POST["id"]))
	{	
		$id = $_POST["id"];
		$sql = "SELECT data_hora AS hora, temperatura, umidade, luminosidade
		FROM medicoes
		WHERE id_dispositivo = '$id'
		AND MINUTE(data_hora) = 0
		ORDER BY id_medicao DESC 
		LIMIT 1";

	    $query = mysqli_query($connection,$sql);
	    $result = mysqli_fetch_assoc($query);

	    $query->close();
	    mysqli_close($connection);

		echo json_encode($result);
	}
?>