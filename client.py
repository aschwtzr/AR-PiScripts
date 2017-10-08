#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = "172.20.10.8"        # Get local machine name
port = 50001                # Reserve a port for your service.

s.connect((host, port))
print('checkity check')

print(s.recv(1024))
s.close                     # Close the socket when done
