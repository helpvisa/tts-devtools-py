#!/usr/bin/env python
"""
Sends arbitrary code to the running TableTop Sim instance,
to be executed globally or on a given object
"""

import socket
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("guid", type=str,
                    help="The object guid upon which to execute the code. "
                         "-1 is global.")
parser.add_argument("code", type=str,
                    help="The code to be executed.")

args = parser.parse_args()

HOST = "localhost"
PORT = 39999

message = {
    "messageID": 3,
    "guid": args.guid,
    "script": args.code
}

data = json.dumps(message)

try:
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect((HOST, PORT))
    tcp_socket.sendall(bytes(data, encoding="utf-8"))
    tcp_socket.close()
except socket.error as err:
    print("Socket creation failed with error ", err)
