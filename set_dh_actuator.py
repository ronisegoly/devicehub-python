import sys
import dh

import pdb
project = sys.argv[1]
uuid= sys.argv[2]
actuator = sys.argv[3]
state=sys.argv[4]
#pdb.set_trace()
print dh.set_actuator_state(actuator,project,uuid,dh.apikey,int(state))


