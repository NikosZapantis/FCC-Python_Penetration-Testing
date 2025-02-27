#!/usr/bin/python3

import socket
 
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Getting the hostname of the current machine so I can use it as the host address for the server [replace with yours static IP found with ipconfig at cmd]
host = socket.gethostname()
port = 444

# Binding the server socket to the specified host and port
serversocket.bind((host, port))

# The server will listen for incoming clien connections for up to 3 clients waiting in the queue [max]
serversocket.listen(3)

# Infinite loop to keep the server running_accepting connections
while True:
    # Accepting an incoming connection [The clientsocket will be used to communicate with client]
    clientsocket, address = serversocket.accept()

    print("received connection from %s " % str(address))

    # Preparing the message to send [client] and encoding it using ASCII
    message = 'Thank you for connecting to the server. [It runs correctly]' + "\r\n"
    clientsocket.send(message.encode('ascii'))

    # Closing the connection with the client after sending the msg
    clientsocket.close()
