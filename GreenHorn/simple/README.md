# simple
Demo of a simple pluck module

To illustrate how simple a module is:
For a plugin called 'simple':

Create a directory called 'simple'.

File 1 is simple.php - contains the plugin info

```{php}
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
}
```

File 2 is simple.site.php contains the code

```{php}
<?php
defined('IN_PLUCK') or exit('Access denied!');
//{pluginname}_theme_main()
function simple_theme_main() {
    echo getMessage();
}
function getMessage() {
    return 'Hello Friends, this is my simple module';
}
```
