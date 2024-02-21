<?php

// String para a qual você deseja gerar o hash
$senhaOriginal = 'senha123';

// Gerar um salt aleatório
$salt = '12345678';

// Concatenar o salt à senha original
$senhaComSalt = $senhaOriginal . $salt;

// Gerar o hash usando bcrypt e o salt concatenado
$hash = password_hash($senhaComSalt, PASSWORD_BCRYPT);

// Exibir o hash gerado
echo "Senha Original: " . $senhaOriginal . "<br>";
echo "Salt: " . $salt . "<br>";
echo "Hash Gerado: " . $hash;

?>

