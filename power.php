<?php

session_start();
$start = $_POST["start"] . "\r\n";


// laten we eens een comment schrijven
// Ik wil de gewenste keuze opslaan in een bestand, start.txt
$file = "start.txt";
// Write the contents back to the file
file_put_contents($file, $start);

header("Location: omw.php");

 ?>
