<?php

	if (isset($_GET["id"])) {	
		$id = $_GET["id"];
		$sql = "SELECT data_hora AS hora, temperatura, umidade, luminosidade
		                FROM medicoes
		                WHERE id_dispositivo = '$id'
	                    AND MINUTE(data_hora) = 0
	                    ORDER BY id_medicao DESC 
	                    LIMIT 24";

	    $query = mysqli_query($connection,$sql);
	    $data = array();

	    foreach ($query as $line) {
	    	$data[] = $line;
	    }

	    $query->close();
	    mysqli_close($connection);

		echo json_encode($data);
	}
?>