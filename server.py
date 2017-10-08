#!/usr/bin/env python
import socket
import re 
from sense_hat import SenseHat
<<<<<<< Updated upstream
from home import showHouse
=======
import sense_images
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
          sense.show_message('home')
          showHouse()
=======
          sense_images.showHouse()
>>>>>>> Stashed changes

     if re.match(r'disco', data, re.I):
          Rainbow.startTheParty()
          
     if re.match(r'print', data, re.I):
          sense.show_message(data)
<<<<<<< Updated upstream
               
=======
     
>>>>>>> Stashed changes
     print(data)
     conn.send(data)  # echo
conn.close()

#party
#today
#home
     #send sensor data

