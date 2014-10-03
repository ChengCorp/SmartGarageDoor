#!/usr/bin/python
from arduino_serial_reader import ArduinoSerialReader
from rpi_server import RPiServer

import threading
import serial
import time

if __name__ == "__main__":
    POST_URL = "http://192.168.0.37:3639/"
    RPISERVER_ADDRESS = ('192.168.0.46', 1040)

    SER = serial.Serial('/dev/ttyACM0', 9600)

    arduinoSerialReader = ArduinoSerialReader()
    serialThread = threading.Thread(target = arduinoSerialReader.start, args = (SER, POST_URL))
    serialThread.setDaemon(True) # TODO: using setdaemon=true for now to , should look for alternative methods
    serialThread.start()

    rpiServer = RPiServer(SER)
    serverThread = threading.Thread(target = rpiServer.startServer, args = RPISERVER_ADDRESS)
    serverThread.setDaemon(True)
    serverThread.start()

    while 1:
        time.sleep(.1)