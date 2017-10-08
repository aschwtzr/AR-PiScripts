#!/usr/bin/env python
 
import socket
from sense_hat import SenseHat

sense = SenseHat()
 
TCP_IP = '172.20.10.8'
TCP_PORT = 50001
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
 
conn, addr = s.accept()
print('Connection address:', addr)
while 1:
     data = conn.recv(BUFFER_SIZE)
     if not data: break
     sense.show_message(data)
     
     print(data)
     conn.send(data)  # echo
conn.close()
