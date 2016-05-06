//call devicehub from URL
<?php 
$value=shell_exec ("python set_dh_actuator.py ".$_GET['project']." ".$_GET['uuid']. " ".$_GET['actuator']." ".$_GET['state']);
echo $value;
?>
