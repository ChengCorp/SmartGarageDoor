#!/usr/bin/python

import serial
import json
import requests

STATUS_STRING = "status"
STATUSCODE_STRING = "statuscode"

post_url = "http://192.168.0.37:3639/"

ser = serial.Serial('/dev/ttyACM0', 9600)


prev_state = None
curr_state = None
is_open = None

def read_state(line):
    if "0" in line: # open
        return 0
    elif '1' in line: # close
        return 1
    elif '2' in line: # opening/closing
        return 2
    elif '41' in line: # error occurred at arduino
        return 41
    else:                                             # error occurred at raspberrypi/python
        return 42

def post_json(url, output):
    json_headers = {'content-type': 'application/json'}
    return requests.post(url, data=json.dumps(output), headers=json_headers)

while 1 : 
    prev_state = curr_state
    curr_state = read_state(ser.readline())

    if curr_state == 0:
        is_open = False
    elif curr_state == 1:
        is_open = True

    if curr_state != prev_state:
        print curr_state
        # print("Changing flag")
        post_data = {STATUS_STRING: is_open, STATUSCODE_STRING: curr_state}
        r = post_json(post_url, post_data)
        # print("Flag changed")

