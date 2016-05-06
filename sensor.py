#list of possible devcices
ports = ['/dev/ttyACM0','/dev/ttyACM1','/dev/ttyUSB0','/dev/ttyUSB1','NULL']
#same as on device hub names
stored={'LampA':"",'LampB':""}
def myip():

	try:
		return(commands.getoutput("/sbin/ifconfig").split("\n")[1].split()[1][5:])
	except:
		return "unkown"

import time
import pdb
import mymodule
import pyfirmata
import time
import datetime
import sys
from datetime import datetime
import requests
import dh
import commands

# Create a new board, specifying serial port
for p in ports:
        try:
                print "trying port: "+p
                if (p=='NULL'):
                        print "getting off"
                        sys.exit()
		print 'trying board with %s' %p
		board = pyfirmata.Arduino(p)
                print  'opened'
		break
        except:
                print "error connecting...aborting" + p
                #sys.exit()board = pyfirmata.Arduino('/dev/ttyACM0')


#first run, store innitial values
pin1=board.get_pin('d:8:o')
pin2=board.get_pin('d:9:o')
pins={'LampA':pin1,'LampB':pin2}
#loop just to make sure we have network, as scipt is triggered from cron
while True:
	try:
 	        print "am I connected?"
 	        #add code here
		break
# 	        if myip()=='unkown':
#			print "still not connected"
#		else:
#			break
		
	except Exception,e:
		print 'no network yet'

try:
	for keys in stored:
    		print keys
    		#read status from devicehub
		if (dh.get_actuator_state (keys, dh.project,dh.uuid, dh.apikey)) == 1:
			mydh='ON'
		else:
			mydh = 'OFF'
                print "state from devicehub %s " % mydh
		#stre locally
		stored[keys]=mydh
#		pdb.set_trace()
		#send to Arduino and relay
		if mydh=='ON':
                	pins[keys].write(1)
                else:
               		pins[keys].write(0)
	        board.pass_time(2)                  # pause 1 second
		time.sleep(2)

	print stored
	#loop forever
	while True:
	        logtime =str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
		
		for keys in stored:
			#read from devicehub
			if (dh.get_actuator_state (keys, dh.project,dh.uuid, dh.apikey)) == 1:
                        	mydh='ON'
                	else:
                        	mydh = 'OFF'
                	data = mydh
                	#do we have a change?
                	if data != stored[keys]:
				print ('%s Value changed on %s, updated to %s' %(keys,logtime,data))
		                stored[keys]=data
                                print stored
				print "sending %s to Arduino %s" %(data,pins[keys])
				if data=='ON':
					pins[keys].write(1)
				else:
					pins[keys].write(0)				
			        board.pass_time(2)                  # pause 1 second
				time.sleep(2)
		print 'new loop ' + logtime
		time.sleep(5) # delays for 5 second		
except Exception,e:
                print "error "+str(e)

