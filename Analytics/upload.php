<?php


echo "ok";
$target_dir = "/";
$target_file = $target_dir . basename($_FILES["data"]["name"]);
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
echo var_dump($_FILES);
$check = getimagesize($_FILES["data"]["tmp_name"]);
  if($check !== false) {
    echo "File is an image - " . $check["mime"] . ".";
    $uploadOk = 1;
  } else {
    echo "File is not an image.";
    $uploadOk = 0;
  }
