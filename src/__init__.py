#!/usr/bin/env python
"""
A graphical version of the tts_devserver that combines the various scripts'
functionalities into one application.
"""

# standard library
import sys
import socket
import selectors
import atexit
import threading
import json
# qt6
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_gui_mainwindow import Ui_MainWindow
# custom
import tcp_actions.listen as Listen
import tcp_actions.send as Send
from generate_specfile import generate_specfile_from_folder


HOST = "localhost"
LISTEN_PORT = 39998
SEND_PORT = 39999
USER_SETTINGS_FILE = "user_devserver_settings.json"

selector = selectors.DefaultSelector()
global_vars = {
    "keep_server_alive": True,
    "main_window": None,
    "specfile": None,
    "editor": None,
    "up_folder": None,
    "down_folder": None,
    "send_message": None,
    "code": None,
    "guid": None,
}


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        event.accept()
        global_vars["keep_server_alive"] = False


def save_user_settings():
    """
    save the user's settings in a json file stored next to the
    executable. This is stuff like the up / dump folder locations,
    specfile locations, and editor command
    """
    # first we ensure entries are up-to-date
    update_specfile_path()
    update_editor_cmd()
    update_current_script_folder()
    update_code_entry()
    update_send_message_table()
    # then we construct our dictionary
    settings_dict = {
        "specfile": global_vars["specfile"],
        "editor": global_vars["editor"],
        "up_folder": global_vars["up_folder"],
        "down_folder": global_vars["down_folder"],
        "send_message": global_vars["send_message"],
        "code": global_vars["code"],
        "guid": global_vars["guid"]
    }
    settings_data = json.dumps(settings_dict)
    try:
        with open(USER_SETTINGS_FILE, mode="w", encoding="utf-8") as save_file:
            save_file.write(settings_data)
    except OSError as err:
        print("Error saving user settings: ", err)


def load_user_settings() -> bool:
    """
    load previously saved user settings
    return True if successful or False if not
    """
    try:
        with open(USER_SETTINGS_FILE, mode="r", encoding="utf-8") as save_file:
            loaded_data = save_file.read()
            if loaded_data is not None:
                parsed_data = json.loads(loaded_data)
                if "specfile" in parsed_data:
                    global_vars["specfile"] = parsed_data["specfile"]
                if "editor" in parsed_data:
                    global_vars["editor"] = parsed_data["editor"]
                if "up_folder" in parsed_data:
                    global_vars["up_folder"] = parsed_data["up_folder"]
                if "down_folder" in parsed_data:
                    global_vars["down_folder"] = parsed_data["down_folder"]
                if "send_message" in parsed_data:
                    global_vars["send_message"] = parsed_data["send_message"]
                if "code" in parsed_data:
                    global_vars["code"] = parsed_data["code"]
                if "guid" in parsed_data:
                    global_vars["guid"] = parsed_data["guid"]
    except OSError as err:
        print("Error loading user settings: ", err)
        return False
    return True


def update_current_script_folder():
    up_folder = global_vars["main_window"].ui.script_upload_folder_entry
    down_folder = global_vars["main_window"].ui.script_download_folder_entry
    if up_folder is not None:
        global_vars["up_folder"] = up_folder.toPlainText()
    if down_folder is not None:
        global_vars["down_folder"] = down_folder.toPlainText()


def update_editor_cmd():
    editor_cmd_entry = global_vars["main_window"].ui.editor_command_entry
    if editor_cmd_entry is not None:
        global_vars["editor"] = editor_cmd_entry.toPlainText()


def update_specfile_path():
    specfile_entry = global_vars["main_window"].ui.spec_file_entry
    if specfile_entry is not None:
        global_vars["specfile"] = specfile_entry.toPlainText()
        # update the script folder, just incase
        update_current_script_folder()


def update_code_entry():
    exec_code_entry = global_vars["main_window"].ui.exec_code_entry
    guid_entry = global_vars["main_window"].ui.guid_entry
    code = exec_code_entry.toPlainText()
    guid = guid_entry.toPlainText()
    global_vars["code"] = code
    global_vars["guid"] = guid


def update_send_message_table():
    send_message_entry = global_vars["main_window"].ui.send_message_entry
    raw_input = send_message_entry.toPlainText()
    global_vars["send_message"] = raw_input


def save_and_play():
    update_specfile_path()
    generate_specfile_from_folder(
        global_vars["up_folder"],
        global_vars["specfile"]
    )
    definitions = Send.gather_files(global_vars["specfile"])
    Send.send_save_and_play_signal(definitions, HOST, SEND_PORT)


def get_new_scripts():
    Send.send_get_scripts_signal(HOST, SEND_PORT)


def execute_lua_code():
    update_code_entry()
    guid = global_vars["guid"]
    code = global_vars["code"]
    Send.send_execute_code_signal(guid, code, HOST, SEND_PORT)


def send_message():
    update_send_message_table()
    raw_input = global_vars["send_message"]
    # process data, separate tables entries by newline (\n)
    keys = []
    values = []
    processed_input = raw_input.split("\n")
    if len(processed_input) > 0:
        for pair in processed_input:
            processed_pair = pair.split("=")
            if len(processed_pair) > 1:
                keys.append(processed_pair[0])
                values.append(processed_pair[1])
    to_send = dict(zip(keys, values))
    Send.send_message_signal(to_send, HOST, SEND_PORT)


def receive_loop():
    while global_vars["keep_server_alive"]:
        update_current_script_folder()
        update_editor_cmd()
        events = selector.select(timeout=1)
        for key, mask in events:
            if key.data is None:
                Listen.accept_wrapper(key.fileobj, selector)
            else:
                toprint = Listen.service_connection(
                    key, mask,
                    global_vars["down_folder"], global_vars["editor"],
                    selector
                )
                if global_vars["main_window"] and len(toprint) > 0:
                    new_console_output = ""
                    # new_console_output = "<font color='#00FF00'>"
                    for entry in toprint:
                        new_console_output += str(entry)
                    console = global_vars["main_window"].ui.console_output
                    console.append(new_console_output)
                    scrollbar = console.verticalScrollBar()
                    scrollbar.setValue(scrollbar.maximum())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    global_vars["main_window"] = window
    window.show()

    # connect some signals to our buttons
    # create a short macro for the ui
    ui = window.ui
    # for poking the TTS api
    ui.save_and_play_button.clicked.connect(save_and_play)
    ui.get_scripts_button.clicked.connect(get_new_scripts)
    ui.exec_code_button.clicked.connect(execute_lua_code)
    ui.send_message_button.clicked.connect(send_message)

    # load user data
    if load_user_settings():
        # create an even shorter macro name for window.ui
        u = ui

        u.spec_file_entry.setPlainText(global_vars["specfile"])
        u.editor_command_entry.setPlainText(global_vars["editor"])
        u.script_upload_folder_entry.setPlainText(global_vars["up_folder"])
        u.script_download_folder_entry.setPlainText(global_vars["down_folder"])
        u.send_message_entry.setPlainText(global_vars["send_message"])
        u.exec_code_entry.setPlainText(global_vars["code"])
        u.guid_entry.setPlainText(global_vars["guid"])

    # for saving user text boxes for next time
    # we do this *after* loading to prevent redudantly saving the newly loaded
    # settings all over again
    ui.spec_file_entry.textChanged.connect(save_user_settings)
    ui.editor_command_entry.textChanged.connect(save_user_settings)
    ui.script_upload_folder_entry.textChanged.connect(save_user_settings)
    ui.script_download_folder_entry.textChanged.connect(save_user_settings)
    ui.send_message_entry.textChanged.connect(save_user_settings)
    ui.exec_code_entry.textChanged.connect(save_user_settings)
    ui.guid_entry.textChanged.connect(save_user_settings)

    # spin up our persistent listen server
    try:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.bind((HOST, LISTEN_PORT))
        tcp_socket.listen()
        tcp_socket.setblocking(False)

        print("TTS DevServer listening on port", LISTEN_PORT)
        error_output = "<font color='#009900'>Listening on " + str(LISTEN_PORT)
        window.ui.console_output.append(error_output)

        atexit.register(Listen.terminate_socket, tcp_socket, selector)
        selector.register(tcp_socket, selectors.EVENT_READ, data=None)

        receive_thread = threading.Thread(target=receive_loop)
        receive_thread.start()
    except socket.error as err:
        print("Socket error ", err)
        error_output = "<font color='#FF0000'> SOCK ERR, please reboot."
        window.ui.console_output.append(error_output)

    sys.exit(app.exec())
