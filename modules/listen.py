import os
import subprocess
import json
import socket
import selectors

def save_received_files(files, folder) -> list[str]:
    """
    save a table of files/scripts/xml to the specified folder
    """
    rd = []  # return data
    for entry in files:
        if "script" in entry:
            script = entry["name"]
            script = script.replace(" ", "_").lower() + ".lua"
            abs_path = os.path.abspath(folder)
            final_path = os.path.join(abs_path, script)
            rd.extend(["\tWriting script to: ", final_path, "\n"])
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
            rd.extend(["\tWriting script to: ", final_path, "\n"])
            try:
                with open(final_path, mode="w", encoding="utf-8") as new_file:
                    new_file.write(entry["ui"])
            except OSError as err:
                print("Error saving / opening: ", err,
                      "| with file", xml, "at", folder)
    return rd


def save_and_open_received_file(file, folder, script, editor_cmd) -> list[str]:
    """
    save the given script with name "file" to the specified folder and open it
    in an editor using the provided editor_cmd
    """
    rd = []  # return data
    # process a new filename
    file = file.replace(" ", "_").lower() + ".lua"
    abs_path = os.path.abspath(folder)
    final_path = os.path.join(abs_path, file)
    rd.extend(["\tSaving new script to:", final_path, "\n"])
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
    finally:
        return rd


def terminate_socket(sock, selector):
    """
    gracefully spin down the tcp socket and its connection
    """
    print("\nSpinning down server.")

    # catch exceptions and close socket anyway
    if sock:
        try:
            sock.shutdown(socket.SHUT_RDWR)
        except socket.error as err:
            print("Socket shutdown error: ", err)
        finally:
            sock.close()

    selector.close()


def accept_wrapper(incoming_socket, selector):
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


def service_connection(sel_key, sel_mask, folder, editor, selector) -> list[str]:
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
            return []
        # we are ready to act upon this request as all its data is received
        else:
            rd = []  # return data
            parsed_data = json.loads(data["inbound"])
            message_id = parsed_data["messageID"]
            match message_id:
                case 0:
                    for entry in parsed_data["scriptStates"]:
                        rd.extend([
                            "Created script for ->",
                            entry["name"],
                            "(guid:)",
                            entry["guid"],
                            "\n"
                        ])
                        rd.extend(save_and_open_received_file(
                            entry["name"],
                            folder,
                            entry["script"],
                            editor
                        ))
                case 1:
                    rd.append("New object and script data received:\n")
                    iterator = 0
                    for entry in parsed_data["scriptStates"]:
                        rd.extend([iterator, "->\t", entry["name"], "\n"])
                        rd.extend(["\t", entry["guid"], "\n"])
                        rd.append("---------------------------------------\n")
                        iterator += 1
                    rd.append("Writing received scripts to project folder.\n")
                    rd.extend(save_received_files(
                        parsed_data["scriptStates"],
                        folder
                    ))
                case 2:
                    rd.extend([parsed_data["message"], "\n"])
                case 3:
                    rd.extend([
                        parsed_data["errorMessagePrefix"],
                        "-> guid:",
                        parsed_data["guid"],
                        "\n"
                    ])
                    rd.extend(["\t", parsed_data["error"], "\n"])
                case 4:
                    rd.append("Received custom message from TTS:")
                    rd.extend(["\t", parsed_data["customMessage"], "\n"])
                case 5:
                    rd.extend([
                        "External code returned value:\n\t",
                        parsed_data["returnValue"],
                        "\n"
                    ])
                case 6:
                    rd.extend([
                        "Game saved to",
                        parsed_data["savePath"],
                        "\n"
                    ])
                case 7:
                    rd.extend([
                        "Object created ->",
                        parsed_data["guid"],
                        "\n"
                    ])
                case _:
                    rd.append("Unrecognized messageID")
            selector.unregister(connection)
            connection.close()

            return rd
    else:
        return []
