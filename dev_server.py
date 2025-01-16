#!/usr/bin/env python
"""
Spins up a server which listens on localhost:39998 for messages from TTS and
responds to them accordingly, pulling down scripts into a directory of the
user's choice or displaying console messages.
"""

import sys
import atexit
import socket
import selectors
import argparse
# custom
import modules.listen as Listen

parser = argparse.ArgumentParser()
parser.add_argument("folder", type=str,
                    help="Path to the folder where scripts should be stored.")
parser.add_argument("-e", "--editor",
                    help="Specify what command should be run when attempting "
                    "to load a script in an editor. If left blank, no editor "
                    "will be opened.")

args = parser.parse_args()

HOST = "localhost"
PORT = 39998

selector = selectors.DefaultSelector()

try:
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind((HOST, PORT))
    tcp_socket.listen()
    print("TTS DevServer listening on port", PORT)
    tcp_socket.setblocking(False)

    atexit.register(Listen.terminate_socket, tcp_socket, selector)

    selector.register(tcp_socket, selectors.EVENT_READ, data=None)

    while True:
        events = selector.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                Listen.accept_wrapper(key.fileobj, selector)
            else:
                toprint = Listen.service_connection(
                    key, mask,
                    args.folder, args.editor,
                    selector
                )
                if len(toprint) > 0:
                    for entry in toprint:
                        print(entry, end="")
except socket.error as err:
    print("Socket error ", err)
except KeyboardInterrupt:
    # avoid ugly errors in term when SIGINT received and gracefully exit
    sys.exit(0)
