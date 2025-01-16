import socket
import json


def poke_tcp_server(data, host, port):
    # prevent name being unbound in 'finally'
    tcp_socket = None
    try:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.connect((host, port))
        tcp_socket.sendall(bytes(data, encoding="utf-8"))
        tcp_socket.shutdown(socket.SHUT_RDWR)
    except socket.error as err:
        print("Socket error ", err)
    finally:
        if tcp_socket:
            tcp_socket.close()


def gather_files(specfile) -> list[dict]:
    """
    gather all the files from the paths in the given specfile
    """
    definitions = []
    try:
        with open(specfile, mode="r", encoding="utf-8") as specfile:
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
    finally:
        return definitions


def send_save_and_play_signal(script_definitions, host, port):
    """
    send the provided definitions to TTS and trigger a save+reload
    """
    message = {
        "messageID": 1,
        "scriptStates": script_definitions
    }
    data = json.dumps(message)

    poke_tcp_server(data, host, port)


def send_get_scripts_signal(host, port):
    """
    request new servers from the running TTS instance
    """
    message = {
        "messageID": 0,
    }

    data = json.dumps(message)

    poke_tcp_server(data, host, port)


def send_execute_code_signal(guid, code, host, port):
    message = {
        "messageID": 3,
        "guid": guid,
        "script": code
    }

    data = json.dumps(message)

    poke_tcp_server(data, host, port)


def send_message_signal(table, host, port):
    message = {
        "messageID": 2,
        "customMessage": table
    }

    data = json.dumps(message)

    poke_tcp_server(data, host, port)
