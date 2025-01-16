# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QTextBrowser, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1020, 552)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.toplevel_layout = QHBoxLayout()
        self.toplevel_layout.setObjectName(u"toplevel_layout")
        self.toplevel_layout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.left_split = QVBoxLayout()
        self.left_split.setObjectName(u"left_split")
        self.exec_code_layout = QVBoxLayout()
        self.exec_code_layout.setObjectName(u"exec_code_layout")
        self.exec_code_button = QPushButton(self.centralwidget)
        self.exec_code_button.setObjectName(u"exec_code_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.exec_code_button.sizePolicy().hasHeightForWidth())
        self.exec_code_button.setSizePolicy(sizePolicy1)
        self.exec_code_button.setMaximumSize(QSize(16777215, 16777215))

        self.exec_code_layout.addWidget(self.exec_code_button)

        self.exec_code_entry = QTextEdit(self.centralwidget)
        self.exec_code_entry.setObjectName(u"exec_code_entry")
        sizePolicy.setHeightForWidth(self.exec_code_entry.sizePolicy().hasHeightForWidth())
        self.exec_code_entry.setSizePolicy(sizePolicy)
        self.exec_code_entry.setMaximumSize(QSize(16777215, 16777215))
        self.exec_code_entry.setFrameShadow(QFrame.Shadow.Sunken)

        self.exec_code_layout.addWidget(self.exec_code_entry)


        self.left_split.addLayout(self.exec_code_layout)

        self.guid_label = QLabel(self.centralwidget)
        self.guid_label.setObjectName(u"guid_label")

        self.left_split.addWidget(self.guid_label)

        self.guid_entry = QPlainTextEdit(self.centralwidget)
        self.guid_entry.setObjectName(u"guid_entry")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.guid_entry.sizePolicy().hasHeightForWidth())
        self.guid_entry.setSizePolicy(sizePolicy2)
        self.guid_entry.setMaximumSize(QSize(16777215, 35))

        self.left_split.addWidget(self.guid_entry)

        self.send_message_layout = QVBoxLayout()
        self.send_message_layout.setObjectName(u"send_message_layout")
        self.send_message_button = QPushButton(self.centralwidget)
        self.send_message_button.setObjectName(u"send_message_button")
        sizePolicy1.setHeightForWidth(self.send_message_button.sizePolicy().hasHeightForWidth())
        self.send_message_button.setSizePolicy(sizePolicy1)
        self.send_message_button.setMaximumSize(QSize(16777215, 16777215))

        self.send_message_layout.addWidget(self.send_message_button)

        self.send_message_entry = QTextEdit(self.centralwidget)
        self.send_message_entry.setObjectName(u"send_message_entry")
        sizePolicy.setHeightForWidth(self.send_message_entry.sizePolicy().hasHeightForWidth())
        self.send_message_entry.setSizePolicy(sizePolicy)
        self.send_message_entry.setMaximumSize(QSize(16777215, 16777215))

        self.send_message_layout.addWidget(self.send_message_entry)

        self.save_and_play_button = QPushButton(self.centralwidget)
        self.save_and_play_button.setObjectName(u"save_and_play_button")
        sizePolicy1.setHeightForWidth(self.save_and_play_button.sizePolicy().hasHeightForWidth())
        self.save_and_play_button.setSizePolicy(sizePolicy1)
        self.save_and_play_button.setMaximumSize(QSize(16777215, 16777215))

        self.send_message_layout.addWidget(self.save_and_play_button)

        self.spec_file_entry = QPlainTextEdit(self.centralwidget)
        self.spec_file_entry.setObjectName(u"spec_file_entry")
        sizePolicy2.setHeightForWidth(self.spec_file_entry.sizePolicy().hasHeightForWidth())
        self.spec_file_entry.setSizePolicy(sizePolicy2)
        self.spec_file_entry.setMaximumSize(QSize(16777215, 35))

        self.send_message_layout.addWidget(self.spec_file_entry)


        self.left_split.addLayout(self.send_message_layout)

        self.editor_command_layout = QVBoxLayout()
        self.editor_command_layout.setObjectName(u"editor_command_layout")
        self.editor_command_label = QLabel(self.centralwidget)
        self.editor_command_label.setObjectName(u"editor_command_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.editor_command_label.sizePolicy().hasHeightForWidth())
        self.editor_command_label.setSizePolicy(sizePolicy3)
        self.editor_command_label.setMaximumSize(QSize(16777215, 16777215))

        self.editor_command_layout.addWidget(self.editor_command_label)

        self.editor_command_entry = QPlainTextEdit(self.centralwidget)
        self.editor_command_entry.setObjectName(u"editor_command_entry")
        sizePolicy2.setHeightForWidth(self.editor_command_entry.sizePolicy().hasHeightForWidth())
        self.editor_command_entry.setSizePolicy(sizePolicy2)
        self.editor_command_entry.setMaximumSize(QSize(16777215, 35))

        self.editor_command_layout.addWidget(self.editor_command_entry)


        self.left_split.addLayout(self.editor_command_layout)

        self.script_folder_label = QLabel(self.centralwidget)
        self.script_folder_label.setObjectName(u"script_folder_label")

        self.left_split.addWidget(self.script_folder_label)

        self.script_folder_entry = QPlainTextEdit(self.centralwidget)
        self.script_folder_entry.setObjectName(u"script_folder_entry")
        sizePolicy2.setHeightForWidth(self.script_folder_entry.sizePolicy().hasHeightForWidth())
        self.script_folder_entry.setSizePolicy(sizePolicy2)
        self.script_folder_entry.setMaximumSize(QSize(16777215, 35))

        self.left_split.addWidget(self.script_folder_entry)

        self.get_scripts_button = QPushButton(self.centralwidget)
        self.get_scripts_button.setObjectName(u"get_scripts_button")
        sizePolicy1.setHeightForWidth(self.get_scripts_button.sizePolicy().hasHeightForWidth())
        self.get_scripts_button.setSizePolicy(sizePolicy1)
        self.get_scripts_button.setMaximumSize(QSize(16777215, 16777215))

        self.left_split.addWidget(self.get_scripts_button)


        self.toplevel_layout.addLayout(self.left_split)

        self.right_split = QVBoxLayout()
        self.right_split.setObjectName(u"right_split")
        self.console_label = QLabel(self.centralwidget)
        self.console_label.setObjectName(u"console_label")

        self.right_split.addWidget(self.console_label)

        self.console_output = QTextBrowser(self.centralwidget)
        self.console_output.setObjectName(u"console_output")
        self.console_output.setMinimumSize(QSize(800, 0))

        self.right_split.addWidget(self.console_output)


        self.toplevel_layout.addLayout(self.right_split)


        self.gridLayout.addLayout(self.toplevel_layout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tabletop Simulator DevServer", None))
        self.exec_code_button.setText(QCoreApplication.translate("MainWindow", u"Execute Code", None))
        self.exec_code_entry.setMarkdown(QCoreApplication.translate("MainWindow", u"print('hello, table!')\n"
"\n"
"", None))
        self.exec_code_entry.setPlaceholderText("")
        self.guid_label.setText(QCoreApplication.translate("MainWindow", u"GUID", None))
        self.guid_entry.setPlainText(QCoreApplication.translate("MainWindow", u"-1", None))
        self.send_message_button.setText(QCoreApplication.translate("MainWindow", u"Send Message With Table", None))
        self.send_message_entry.setMarkdown(QCoreApplication.translate("MainWindow", u"key=value\n"
"\n"
"", None))
        self.send_message_entry.setPlaceholderText("")
        self.save_and_play_button.setText(QCoreApplication.translate("MainWindow", u"Save and Play", None))
        self.spec_file_entry.setPlainText(QCoreApplication.translate("MainWindow", u"your_specfile.json", None))
        self.spec_file_entry.setPlaceholderText("")
        self.editor_command_label.setText(QCoreApplication.translate("MainWindow", u"Editor Command", None))
        self.editor_command_entry.setPlainText(QCoreApplication.translate("MainWindow", u"xterm -e vim", None))
        self.editor_command_entry.setPlaceholderText("")
        self.script_folder_label.setText(QCoreApplication.translate("MainWindow", u"Script Folder", None))
        self.script_folder_entry.setPlainText(QCoreApplication.translate("MainWindow", u"test_scripts", None))
        self.get_scripts_button.setText(QCoreApplication.translate("MainWindow", u"Get New Scripts", None))
        self.console_label.setText(QCoreApplication.translate("MainWindow", u"Console Output", None))
#if QT_CONFIG(whatsthis)
        self.console_output.setWhatsThis(QCoreApplication.translate("MainWindow", u"Output sent from TTS is displayed here.", None))
#endif // QT_CONFIG(whatsthis)
    # retranslateUi

