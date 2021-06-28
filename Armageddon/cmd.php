<?php
// mysqli
$mysqli = new mysqli("localhost", "drupaluser", "CQHEy@9M*m23gBVj", "drupal");
$result = $mysqli->query("select * from users");

//$result = $mysqli->query("show columns from users");
while($row = $result->fetch_assoc()){
	echo "<p>" .  $row['name']. "</p>" . "\n";
	echo "<p>" .  $row['pass']. "</p>" . "\n";
}

