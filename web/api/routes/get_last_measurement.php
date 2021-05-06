<?php

	include '../settings/configuration_file.php';

	if (isset($_GET["id"])) {
		
		$Id = $_GET["id"];
		$Device = new Device($Id);
		echo json_encode($Device->getLastDayMeasurements());
		//to text -> http://localhost/lens_guardian/web/api/routes/get_last_measurement.php?id=1
	}
