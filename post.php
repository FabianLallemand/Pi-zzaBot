<?php

session_start();
$route = $_POST["route"] . "\r\n";
echo 'We gaan naar ' . $route;

// laten we eens een comment schrijven
// Ik wil de gewenste keuze opslaan in een bestand, route.txt
$file = "direction.txt";
// Write the contents back to the file
file_put_contents($file, $route);

<<<<<<< HEAD
header("Location: run.php");

 ?>
=======
?>
>>>>>>> 6c51994f8bbd385ec3ea213c09479207069650f4
