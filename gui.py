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
# qt6
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_gui_mainwindow import Ui_MainWindow
# custom
import modules.listen as Listen
import modules.send as Send


HOST = "localhost"
LISTEN_PORT = 39998
SEND_PORT = 39999

selector = selectors.DefaultSelector()
global_vars = {
    "keep_server_alive": True,
    "main_window": None,
    "specfile": None,
    "editor": None,
    "folder": None,
}


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        event.accept()
        global_vars["keep_server_alive"] = False


def update_current_script_folder():
    folder_entry = global_vars["main_window"].ui.script_folder_entry
    global_vars["folder"] = folder_entry.toPlainText()


def update_editor_cmd():
    editor_cmd_entry = global_vars["main_window"].ui.editor_command_entry
    global_vars["editor"] = editor_cmd_entry.toPlainText()


def update_specfile_path():
    specfile_entry = global_vars["main_window"].ui.spec_file_entry
    global_vars["specfile"] = specfile_entry.toPlainText()


def save_and_play():
    update_specfile_path()
    definitions = Send.gather_files(global_vars["specfile"])
    Send.send_save_and_play_signal(definitions, HOST, SEND_PORT)


def get_new_scripts():
    Send.send_get_scripts_signal(HOST, SEND_PORT)


def execute_lua_code():
    exec_code_entry = global_vars["main_window"].ui.exec_code_entry
    guid_entry = global_vars["main_window"].ui.guid_entry
    code = exec_code_entry.toPlainText()
    guid = guid_entry.toPlainText()
    Send.send_execute_code_signal(guid, code, HOST, SEND_PORT)


def send_message():
    send_message_entry = global_vars["main_window"].ui.send_message_entry
    raw_input = send_message_entry.toPlainText()
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
        events = selector.select(timeout=5)
        for key, mask in events:
            if key.data is None:
                Listen.accept_wrapper(key.fileobj, selector)
            else:
                toprint = Listen.service_connection(
                    key, mask,
                    global_vars["folder"], global_vars["editor"],
                    selector
                )
                if global_vars["main_window"] and len(toprint) > 0:
                    new_console_output = ""
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
    window.ui.save_and_play_button.clicked.connect(save_and_play)
    window.ui.get_scripts_button.clicked.connect(get_new_scripts)
    window.ui.exec_code_button.clicked.connect(execute_lua_code)
    window.ui.send_message_button.clicked.connect(send_message)

    # spin up our persistent listen server
    try:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.bind((HOST, LISTEN_PORT))
        tcp_socket.listen()
        print("TTS DevServer listening on port", LISTEN_PORT)
        tcp_socket.setblocking(False)

        atexit.register(Listen.terminate_socket, tcp_socket, selector)
        selector.register(tcp_socket, selectors.EVENT_READ, data=None)

        receive_thread = threading.Thread(target=receive_loop)
        receive_thread.start()
    except socket.error as err:
        print("Socket error ", err)

    sys.exit(app.exec())
