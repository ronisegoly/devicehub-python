import json
import requests
import pdb
import os
import sys
#pdb.set_trace()


def set_sensor_value(sensor,project,uuid,apikey,value):
	message = "https://api.devicehub.net/v2/project/"+project+"/device/"+uuid+"/sensor/"+sensor+"/data"
#	pdb.set_trace()
	res=requests.post(message,data={"value":value,'apiKey':apikey})
	


def get_actuator_state(actuator,project,uuid,apikey):
	url = "https://api.devicehub.net/v2/project/"+project+"/device/"+uuid+"/actuator/"+actuator+"/state"
	payload = { }
	headers = {'X-ApiKey': apikey}
	res = requests.get(url, data=payload, headers=headers)
#	pdb.set_trace()
	return res.json()[0]['state']
	#res.text.split(",")[3].split(":")[1]

def get_sensor_value(sensor,project,uuid,apikey):
        url = "https://api.devicehub.net/v2/project/"+project+"/device/"+uuid+"/sensor/"+sensor+"/data?limit=1"
#        pdb.set_trace()
        payload = { }
        headers = {'X-ApiKey': apikey}
        res = requests.get(url, data=payload, headers=headers)
        return res.json()[0]['value']


def set_actuator_state(actuator,project,uuid,apikey,value):
	if value>100:
		value=100
	message = "https://api.devicehub.net/v2/project/"+project+"/device/"+uuid+"/actuator/"+actuator+"/state"
	res=requests.post(message,data={"state":value,'apiKey':apikey})

actuator="XX"
project='XX'
apikey="XX"
uuid="XX"


