#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Timeout for socket connection [5 sec]
s.settimeout(5)

# Allows user to input the IP and port he want to scan
host = input("Please enter the IP you want to scan: ")
port = int(input("Please enter the port you want to scan: "))

# This function just checks if the provided port is open or closed
def portScanner(port):
    # The connect_ex() method tries to connect to the given host and port [if connection fails ---> returns non-zero value / if succeeds ---> returns 0]
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

# Calling the portScanner function, passing the provided port number from the user's input
portScanner(port)