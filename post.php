<?php

session_start();
$route = $_POST["route"] . "\r\n";
echo 'We gaan naar ' . $route;

// laten we eens een comment schrijven
// Ik wil de gewenste keuze opslaan in een bestand, direction.txt
$file = "direction.txt";
// Write the contents back to the file
file_put_contents($file, $route);
<<<<<<< HEAD

=======
>>>>>>> 8911974683dc3a0dd3f919ed3a56bf72eefd7a33
header("Location: index.php");

 ?>
