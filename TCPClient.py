#!/usr/bin/pythong3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = '192.168.2.2'
host = socket.gethostname()

port = 444

clientsocket.connect(('192.168.2.2', port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))