<?php

class Device {
    
    public $DeviceId = 0;

    function __construct($DeviceId) {
        $this->DeviceId = $DeviceId;
    }

    public function getLastMeasurement() {

        $Db = new Database ();    
        $Sql = "SELECT data_hora AS hora, temperatura, umidade, luminosidade FROM medicoes WHERE id_dispositivo = '$this->DeviceId' AND MINUTE(data_hora) = 0 ORDER BY id_medicao DESC LIMIT 1";
        $Pdo = new PDO($Db->Connection, $Db->User, $Db->Password);
        $Stm = $Pdo->query($Sql);
        $Result = $Stm->fetch();

        if($Result){
            return $Result;
        } else{
            return array();
        }

        
    }

    public function getLastDayMeasurements() {

        $Db = new Database ();    
		$Sql = "SELECT data_hora AS hora, temperatura, umidade, luminosidade FROM medicoes WHERE id_dispositivo = '$this->DeviceId' AND MINUTE(data_hora) = 0 ORDER BY id_medicao DESC  LIMIT 24";
        $Pdo = new PDO($Db->Connection, $Db->User, $Db->Password);
        $Stm = $Pdo->query($Sql);
        $Result = $Stm->fetchAll();

        //var_dump(count($Result));exit;


        return $Result;
    }

}