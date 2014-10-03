#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
        
class RPiServer:

    def __init__(self, ser):
        self.ser = ser

    #This class will handles any incoming request from
    #the browser 
    class myHandler(BaseHTTPRequestHandler):
        
        #Handler for the GET requests
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            # Send the html message
            self.wfile.write("Hello World !")
            print "Yea"
            ser.write('X');
            return
            
    def startServer(self, server_address, server_port):
        #Create a web server and define the handler to manage the
        #incoming request
        server = HTTPServer((server_address, server_port), myHandler)
        print 'Started httpserver on port ' , 1040
        
        #Wait forever for incoming http requests
        server.serve_forever()
        
    def terminateServer(self):
        server.socket.close()
