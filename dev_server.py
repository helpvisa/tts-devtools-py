#!/usr/bin/env python
"""
Spins up a server which listens on localhost:39998 for messages from TTS and
responds to them accordingly, pulling down scripts into a directory of the
user's choice or displaying console messages.
"""

import os
import subprocess
import sys
import atexit
import socket
import selectors
import json
import argparse

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


def save_received_files(files, folder):
    """
    save a table of files/scripts/xml to the specified folder
    """
    for entry in files:
        if "script" in entry:
            script = entry["name"]
            script = script.replace(" ", "_").lower() + ".lua"
            abs_path = os.path.abspath(folder)
            final_path = os.path.join(abs_path, script)
            print("\tWriting script to:", final_path)
            try:
                with open(final_path, mode="w", encoding="utf-8") as new_file:
                    new_file.write(entry["script"])
            except OSError as err:
                print("Error saving / opening: ", err,
                      "| with file", script, "at", folder)

        if "ui" in entry:
            xml = entry["name"]
            xml = xml.replace(" ", "_").lower() + ".xml"
            abs_path = os.path.abspath(folder)
            final_path = os.path.join(abs_path, xml)
            print("\tWriting script to:", final_path)
            try:
                with open(final_path, mode="w", encoding="utf-8") as new_file:
                    new_file.write(entry["ui"])
            except OSError as err:
                print("Error saving / opening: ", err,
                      "| with file", xml, "at", folder)


def save_and_open_received_file(file, folder, script, editor_cmd):
    """
    save the given script with name "file" to the specified folder and open it
    in an editor using the provided editor_cmd
    """
    # process a new filename
    file = file.replace(" ", "_").lower() + ".lua"
    abs_path = os.path.abspath(folder)
    final_path = os.path.join(abs_path, file)
    print("\tSaving new script to:", final_path)
    try:
        with open(final_path, mode="w", encoding="utf-8") as new_file:
            new_file.write(script)
        # build an array of commands to use w Popen
        if None is not editor_cmd:
            command_array = editor_cmd.split(" ")
            command_array.append(final_path)
            # call the editor w/ the file
            subprocess.Popen(command_array, close_fds=True)
    except OSError as err:
        print("Error saving / opening: ", err,
              "| with file", file, "at", folder)


def terminate_socket():
    """
    gracefully spin down the tcp socket and its connection
    """
    print("\nSpinning down server.")

    # catch exceptions and close socket anyway
    if tcp_socket:
        try:
            tcp_socket.shutdown(socket.SHUT_RDWR)
        except socket.error as err:
            print("Socket shutdown error: ", err)
        finally:
            tcp_socket.close()

    selector.close()


def accept_wrapper(incoming_socket):
    """
    accept incoming connections, make sure they do not block the server,
    and register them with the selector
    """
    connection, address = incoming_socket.accept()
    connection.setblocking(False)
    data = {
        "address": address,
        "inbound": b"",
    }
    # set a mask showing if connection is ready to be read
    connection_events = selectors.EVENT_READ
    selector.register(connection, connection_events, data=data)


def service_connection(sel_key, sel_mask):
    """
    service an incoming connection request from TTS
    """
    # the connection socket stored in our selector key
    connection = sel_key.fileobj
    data = sel_key.data
    if sel_mask & selectors.EVENT_READ:
        received_data = connection.recv(4096)
        if received_data:
            data["inbound"] += received_data
        # we are ready to act upon this request as all its data is received
        else:
            parsed_data = json.loads(data["inbound"])
            message_id = parsed_data["messageID"]
            # print("\n", parsed_data, "\n")
            print("\n")  # separate message with newline
            match message_id:
                case 0:
                    for entry in parsed_data["scriptStates"]:
                        print("Created script for ->", entry["name"],
                              "(guid:)", entry["guid"])
                        save_and_open_received_file(
                            entry["name"],
                            args.folder,
                            entry["script"],
                            args.editor
                        )
                case 1:
                    print("New object and script data received:")
                    iterator = 0
                    for entry in parsed_data["scriptStates"]:
                        print(iterator, "->\t", entry["name"])
                        print("\t", entry["guid"])
                        print("-----------------")
                        iterator += 1
                    print("Writing received scripts to project folder.")
                    save_received_files(
                        parsed_data["scriptStates"],
                        args.folder
                    )
                case 2:
                    print(parsed_data["message"])
                case 3:
                    print(parsed_data["errorMessagePrefix"],
                          "-> guid:", parsed_data["guid"])
                    print("\t", parsed_data["error"])
                case 4:
                    print("Received custom message from TTS:")
                    print("\t", parsed_data["customMessage"])
                case 5:
                    print("External code returned value:\n\t",
                          parsed_data["returnValue"])
                case 6:
                    print("Game saved to", parsed_data["savePath"])
                case 7:
                    print("Object created ->", parsed_data["guid"])
                case _:
                    print("Unrecognized messageID")
            selector.unregister(connection)
            connection.close()


# core event loop, listen for incoming requests / connections from TTS
try:
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind((HOST, PORT))
    tcp_socket.listen()
    print("TTS DevServer listening on port", PORT)
    tcp_socket.setblocking(False)

    atexit.register(terminate_socket)

    selector.register(tcp_socket, selectors.EVENT_READ, data=None)

    while True:
        events = selector.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)
except socket.error as err:
    print("Socket error ", err)
except KeyboardInterrupt:
    # avoid ugly errors in term when SIGINT received and gracefully exit
    sys.exit(0)
