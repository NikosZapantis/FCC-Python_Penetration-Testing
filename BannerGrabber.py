#!/usr/bin/python3

import socket

# Defining this function to retrieve a banner from a service running on a given IP and port
def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))

    # Timeout for the socket connection [5 sec]
    s.settimeout(5)
    # Attempting to receive up to 1024 bytes of data from the socket [the received data is in bytes, so I convert it to a string and remove the 'b' prefix]
    print(str(s.recv(1024)).strip('b')) 

def main():
    # Use ipconfig in cmd to access your own IP [user manual]
    ip = input("Please enter the IP: ")
    port = str(input("Please enter the port: "))

    # Caling the banner function with the inputs of the user
    banner(ip, port)

# Calling main to start the script
main()
