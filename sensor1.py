ports = ['/dev/ttyACM0','/dev/ttyACM1','/dev/ttyUSB0','/dev/ttyUSB1','NULL']
stored={'one':"",'two':"",'three':"",'four':"",'five':"",'six':"",'seven':"",'eight':""}

import time
import pdb
import pyfirmata
import time
import datetime
import sys
from datetime import datetime
import requests
import dh


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


aio = Client('ae9451b613a366a256d1f69ef8ff5b2f4c4a55d3')
#first run, store innitial values
pin1=board.get_pin('d:3:o')
pin2=board.get_pin('d:4:o')
pin3=board.get_pin('d:5:o')
pin4=board.get_pin('d:6:o')
pin5=board.get_pin('d:7:o')
pin6=board.get_pin('d:8:o')
pin7=board.get_pin('d:9:o')
pin8=board.get_pin('d:10:o')
pins={'one':pin1,'two':pin2,'three':pin3,'four':pin4,'five':pin5,'six':pin6,'seven':pin7,'eight':pin8}
ind=0
#loop just to make sure we have network
while True:
	try:
		print "check you connectivity here"
		break
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
#			pdb.set_trace()
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

