<?php
	require_once("database_connection.php");

	if (isset($_POST["id"]))
	{	
		$id = $_POST["id"];
		$sql = "SELECT temperature, humidity FROM measurements WHERE device_id = '$id' ORDER BY measure_id DESC LIMIT 1";

	    $query = mysqli_query($connection,$sql);
	    $result = mysqli_fetch_assoc($query);

	    $query->close();
	    mysqli_close($connection);

		echo json_encode($result);
	}
?>