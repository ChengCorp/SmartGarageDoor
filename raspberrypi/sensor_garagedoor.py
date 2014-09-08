import serial
import json
import requests

prevFlag = None;
isOpen = None

url = "http://192.168.0.37:3639/"

ser = serial.Serial('/dev/ttyACM0', 9600)

while 1 : 
  prevFlag = isOpen
  #output = ""
  if "0" in ser.readline():
    isOpen = False
    #output = "{'status':'close'}"
  elif '1' in ser.readline():
    isOpen = True
    #output = "{'status':'open'}"
	
  if isOpen != prevFlag:
    print("Changing flag")
    statusStr = "status"
    headers = {'content-type': 'application/json'}
    output = {statusStr: isOpen}
    r = requests.post(url, data=json.dumps(output), headers=headers)
    print("Flag changed")

