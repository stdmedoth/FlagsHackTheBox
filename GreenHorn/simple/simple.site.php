<?php
defined('IN_PLUCK') or exit('Access denied!');
//{pluginname}_theme_main()
function simple_theme_main() {
    echo getMessage();
}
function getMessage() {
    return 'Hello Friends, this is my simple module';
}
