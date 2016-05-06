ports = ['/dev/ttyACM0','/dev/ttyACM1','/dev/ttyUSB0','/dev/ttyUSB1','NULL']
stored={'LampA':"",'LampB':""}
def myip():

	try:
		return(commands.getoutput("/sbin/ifconfig").split("\n")[1].split()[1][5:])
	except:
		return "unkown"

def email_alert(first, second, third):
    report = {}
    report["value1"] = first
    report["value2"] = second
    report["value3"] = third
    requests.post("https://maker.ifttt.com/trigger/relay001/with/key/ctoyvcrdl2NWmXeLL87aT2", data=report)
                  #https://maker.ifttt.com/trigger/relay001/with/key/ctoyvcrdl2NWmXeLL87aT2

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
#loop just to make sure we have network
while True:
	try:
 	        rd= mymodule.r.hgetall('relay')
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
		if (dh.get_actuator_state (keys, dh.project,dh.uuid, dh.apikey)) == 1:
			mydh='ON'
		else:
			mydh = 'OFF'
                print "state from devicehub %s " % mydh

		stored[keys]=mydh
#		pdb.set_trace()
		if mydh=='ON':
                	pins[keys].write(1)
                else:
               		pins[keys].write(0)
	        board.pass_time(2)                  # pause 1 second
		time.sleep(2)

	print stored
	while True:
	        logtime =str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
		
		for keys in stored:
			if (dh.get_actuator_state (keys, dh.project,dh.uuid, dh.apikey)) == 1:
                        	mydh='ON'
                	else:
                        	mydh = 'OFF'
                	data = mydh
                	if data != stored[keys]:
				print ('%s Value changed on %s, updated to %s' %(keys,logtime,data))
		                stored[keys]=data
                                print stored
				print "sending %s to Arduino %s" %(data,pins[keys])
#				email_alert("Sending to Arduino", data, pins[keys])

#				pdb.set_trace()
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

