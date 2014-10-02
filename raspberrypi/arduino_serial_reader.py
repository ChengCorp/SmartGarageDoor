#!/usr/bin/python

import serial
import json
import requests

class ArduinoSerialReader:
    _STATUS_STRING = "status"
    _STATUSCODE_STRING = "statuscode"
    
    #_post_url = "http://192.168.0.37:3639/"
    
    #def __init__(self, url):
    #    self._post_url = url

    def read_state(self, line):
        if "0" in line:    # open
            return 0
        elif '1' in line:  # close
            return 1
        elif '2' in line:  # opening/closing
            return 2
        elif '41' in line: # error occurred at arduino
            return 41
        else:              # error occurred at raspberrypi/python
            return 42

    def post_json(self, url, output):
        json_headers = {'content-type': 'application/json'}
        return requests.post(url, data=json.dumps(output), headers=json_headers)

    def start(self, ser, url):
        prev_state = None
        curr_state = None
        is_open = None
            
        while 1 : 
            prev_state = curr_state
            curr_state = self.read_state(ser.readline())
        
            if curr_state == 0:
                is_open = False
            elif curr_state == 1:
                is_open = True
        
            if curr_state != prev_state:
                print curr_state
                # print("Changing flag")
                post_data = {self._STATUS_STRING: is_open, self._STATUSCODE_STRING: curr_state}
                r = self.post_json(url, post_data)
                # print("Flag changed")

ser = serial.Serial('/dev/ttyACM0', 9600)
arduino_serial_reader = ArduinoSerialReader()
arduino_serial_reader.start(ser, "http://192.168.0.37:3639/")
