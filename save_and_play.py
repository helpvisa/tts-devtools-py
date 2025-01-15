#!/usr/bin/env python
"""
Uses a 'definitions' file to send an array containing object + script + ui
information to TTS.

The definitions file is a json file containing an array that is assembled
adhering to the following pattern:

[
    {
        "name": "Global",
        "guid": "-1",
        "script": "path/to/script.lua",
        "ui": "path/to/ui.xml"
    },
    ...
]

...and so forth for each object with an associated script and/or ui file.
The "script" and "ui" fields are optional, but you really should have at least
one or the other.
"""

import socket
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("specfile", type=str,
                    help="Path to the spec.json file defining the objects, "
                         "scripts, and XML files to be sent to TTS.")

args = parser.parse_args()

HOST = "localhost"
PORT = 39999

# gather all the files from the given path
definitions = []
try:
    with open(args.specfile, mode="r", encoding="utf-8") as specfile:
        json_spec = json.load(specfile)
        for entry in json_spec:
            new_definition = {
                "name": entry["name"],
                "guid": entry["guid"],
            }
            if "script" in entry:
                with open(entry["script"], mode="r", encoding="utf-8") as scr:
                    new_definition["script"] = scr.read()
            if "ui" in entry:
                with open(entry["ui"], mode="r", encoding="utf-8") as xml:
                    new_definition["ui"] = xml.read()
            definitions.append(new_definition)
except OSError as error:
    print("Error opening specfile: ", error)

message = {
    "messageID": 1,
    "scriptStates": definitions
}

data = json.dumps(message)

try:
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect((HOST, PORT))
    tcp_socket.sendall(bytes(data, encoding="utf-8"))
    tcp_socket.close()
except socket.error as err:
    print("Socket creation failed with error ", err)
