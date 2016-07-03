# -*- coding: utf-8 -*-
import socket
from sense_hat import SenseHat

#Declaration
sense = SenseHat()

#UDP Configuration 
UDP_IP = "192.168.1.35"
UDP_PORT = 9930

#PC Configuration
PC_IP = "192.168.1.21"

#Init socket
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

#Connection
sock.bind((UDP_IP, UDP_PORT))

#Main
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    frame=data.split(";",1)

    if frame[0] == "PRINT_TEXT":
      print "PRINT_TEXT received"
      sense.show_message(frame[1])
    elif frame[0] == "PRINT_TEMPERATURE":
      print "PRINT_TEMPERATURE received"
      temperature = sense.get_temperature()
      temperature = round(temperature,2)
      sense.show_message(str(temperature)+ " Degre")
    elif frame[0] == "PRINT_PRESSURE":
      print "PRINT_PRESSURE received"
      pressure = sense.get_pressure()
      pressure = round(pressure,2)
      sense.show_message(str(pressure)+ " HPa")
