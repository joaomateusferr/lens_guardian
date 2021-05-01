<?php

	include '../settings/configuration_file.php';

	if (isset($_GET["id"])) {
		
		$Id = $_GET["id"];
		$Device = new Device($Id);
		echo json_encode($Device->getLastDayMeasurements());
		
	}
