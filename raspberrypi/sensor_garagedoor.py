import serial
import json
import requests

prevState = None
currState = None
isOpen = None

url = "http://192.168.0.37:3639/"

ser = serial.Serial('/dev/ttyACM0', 9600)

while 1 : 
  prevState = isOpen

  if "0" in ser.readline(): # open
    isOpen = False
    currState = 0
  elif '1' in ser.readline(): # close
    isOpen = True
    currState = 1
  elif '2' in ser.readline(): # opening/closing
    currState = 2
  elif '41' in ser.readline(): # error occurred at arduino
    currState = 41
  else:                       # error occurred at raspberrypi/python
    currState = 42

  if isOpen != prevState:
    print("Changing flag")
    statusStr = "status"
    headers = {'content-type': 'application/json'}
    output = {statusStr: isOpen}
    r = requests.post(url, data=json.dumps(output), headers=headers)
    print("Flag changed")

