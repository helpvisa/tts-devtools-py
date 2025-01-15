#!/usr/bin/env python
"""
Requests lua scripts from the running TableTop Sim instance
"""

import socket
import json

HOST = "localhost"
PORT = 39999

message = {
    "messageID": 0,
}

data = json.dumps(message)

try:
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect((HOST, PORT))
    tcp_socket.sendall(bytes(data, encoding="utf-8"))
except socket.error as err:
    print("Socket creation failed with error ", err)
finally :
    tcp_socket.close()
