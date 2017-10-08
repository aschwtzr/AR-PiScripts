#!/usr/bin/env python
import socket
import re 
from sense_hat import SenseHat
import sense_images
import Rainbow

sense = SenseHat()
 
TCP_IP = '172.20.10.8'
TCP_PORT = 50001
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(5)
 
conn, addr = s.accept()
print('Connection address:', addr)

while True:
     data = conn.recv(BUFFER_SIZE)
     if not data: break

     if re.match(r'home', data,re.I):
          sense_images.showHouse()
          
     if re.match(r'heart',data,re.I):
          sense_images.showHeart()

     if re.match(r'disco', data, re.I):
          Rainbow.startTheParty()
          
     if re.match(r'alert', data, re.I):
          sense.set_rotation(180)
          sense.show_message(data, scroll_speed=.02)

     conn.send(data)  # echo
conn.close()

#party
#today
#home
     #send sensor data


