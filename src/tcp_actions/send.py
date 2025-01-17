"""
functions to be used when poking a tcp listen socket to send messages to TTS
"""

import socket
import json


def poke_tcp_server(data, host, port) -> list[str]:
    """
    send a data packet to the tcp socket at host:port
    """
    rd = []
    # prevent name being unbound in 'finally'
    tcp_socket = None
    try:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.connect((host, port))
        tcp_socket.sendall(bytes(data, encoding="utf-8"))
        tcp_socket.shutdown(socket.SHUT_RDWR)
    except socket.error as err:
        print("Socket error ", err)
        rd.extend([
            "<font color='#FF0000'>",
            "Socket error:",
            str(err),
            "\n"
        ])
    finally:
        if tcp_socket:
            tcp_socket.close()
    return rd


def gather_files(specfile) -> list[dict]:
    """
    gather all the files from the paths in the given specfile
    """
    definitions = []
    try:
        with open(specfile, mode="r", encoding="utf-8") as spec:
            json_spec = json.load(spec)
            for entry in json_spec:
                new_definition = {
                    "name": entry["name"],
                    "guid": entry["guid"],
                }
                if "script" in entry:
                    # validate filepath
                    validation_str = entry["script"].split(".")
                    validation_str = validation_str[len(validation_str) - 1]
                    if validation_str != "lua":
                        continue
                    with open(entry["script"],
                              mode="r",
                              encoding="utf-8") as scr:
                        new_definition["script"] = scr.read()
                if "ui" in entry:
                    # validate filepath
                    validation_str = entry["ui"].split(".")
                    validation_str = validation_str[len(validation_str) - 1]
                    if validation_str != "xml":
                        continue
                    with open(entry["ui"],
                              mode="r",
                              encoding="utf-8") as xml:
                        new_definition["ui"] = xml.read()
                definitions.append(new_definition)
    except OSError as error:
        print("Error opening specfile: ", error)
        return definitions  # ensure definitions is returned regardless
    return definitions


def send_save_and_play_signal(script_definitions, host, port) -> list[str]:
    """
    send the provided definitions to TTS and trigger a save+reload
    """
    message = {
        "messageID": 1,
        "scriptStates": script_definitions
    }
    data = json.dumps(message)

    return poke_tcp_server(data, host, port)


def send_get_scripts_signal(host, port) -> list[str]:
    """
    request new servers from the running TTS instance
    """
    message = {
        "messageID": 0,
    }

    data = json.dumps(message)

    return poke_tcp_server(data, host, port)


def send_execute_code_signal(guid, code, host, port) -> list[str]:
    """
    send a bit of code over to TTS to be executed on object with given GUID
    """
    message = {
        "messageID": 3,
        "guid": guid,
        "script": code
    }

    data = json.dumps(message)

    return poke_tcp_server(data, host, port)


def send_message_signal(table, host, port) -> list[str]:
    """
    send a lua table to TTS to be operated on with onExternalMessage()
    """
    message = {
        "messageID": 2,
        "customMessage": table
    }

    data = json.dumps(message)

    return poke_tcp_server(data, host, port)
