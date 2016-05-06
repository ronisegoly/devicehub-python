import sys
import dh

import pdb
#$value=shell_exec ("python push_dh_sensor.py ".$_GET['project']." ".$_GET['uuid']. " ".$_GET['sensor']." ".$_GET['d_value']);

#def set_actuator_state(actuator,project,uuid,apikey,value):

project = sys.argv[1]
uuid= sys.argv[2]
actuator = sys.argv[3]
state=sys.argv[4]
#pdb.set_trace()
print dh.set_actuator_state(actuator,project,uuid,dh.apikey,int(state))


