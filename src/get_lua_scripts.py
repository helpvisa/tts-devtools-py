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

# prevent name being unbound in 'finally'
tcp_socket = None
try:
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect((HOST, PORT))
    tcp_socket.sendall(bytes(data, encoding="utf-8"))
    tcp_socket.shutdown(socket.SHUT_RDWR)
except socket.error as err:
    print("Socket error ", err)
finally:
    if tcp_socket:
        tcp_socket.close()
