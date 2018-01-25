<?php

$route = $_POST["route"];
echo 'We gaan naar ';
echo $route;
header("Location: index.php");
exit();
 ?>
