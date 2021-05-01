<?php

class Database {
    //Database Info
    public $Server = "";
    public $Database = "";
    public $Connection = "";
    public $User = "";
    public $Password = "";

    //File Exception
    public static $ExceptionDatabaseInfoFileNotFound = "Unable to find database info file";
    public static $ExceptionUnableToGetDatabaseInfoFile = "Unable to get Database file info";

    function __construct() {
        
        $DatabaseInfoFilePath = "../settings/database_info.json";

        if(file_exists($DatabaseInfoFilePath)){

            try {

                $DatabaseInfoFile = fopen($DatabaseInfoFilePath, "r");
                $DatabaseInfo = json_decode(fread($DatabaseInfoFile,filesize($DatabaseInfoFilePath)),true);

                $this->Server = $DatabaseInfo['Server'];
                $this->Database = $DatabaseInfo['Database'];
                $this->Connection = "mysql:host=".$DatabaseInfo['Server'].";dbname=".$DatabaseInfo['Database'];
                $this->User = $DatabaseInfo['User'];
                $this->Password = $DatabaseInfo['Password'];

                fclose($DatabaseInfoFile);

            } catch(Exception $e) {
                throw new Exception(Database::$ExceptionUnableToGetDatabaseInfoFile);
            }

        } else {
            throw new Exception(Database::$ExceptionDatabaseInfoFileNotFound);
        }
    }
}