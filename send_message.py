#!/usr/bin/env python
"""
Sends a custom message to the running TableTop Sim instance,
in the format of a table containing key=value pairs
"""

import socket
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("values", type=str, nargs="*",
                    help="key = value pairs. Any number is allowed.")

args = parser.parse_args()

keys = []
values = []

for entry in args.values:
    split = entry.split("=")
    if len(split) > 1 and "" != split[1]:
        keys.append(split[0])
        values.append(split[1])

table_to_send = dict(zip(keys, values))

HOST = "localhost"
PORT = 39999

message = {
    "messageID": 2,
    "customMessage": table_to_send
}

data = json.dumps(message)

try:
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect((HOST, PORT))
    tcp_socket.sendall(bytes(data, encoding="utf-8"))
    tcp_socket.close()
except socket.error as err:
    print("Socket creation failed with error ", err)
