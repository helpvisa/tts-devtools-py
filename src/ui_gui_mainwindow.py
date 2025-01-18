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
    QPushButton, QSizePolicy, QSpacerItem, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1344, 759)
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
        self.left_split_frame = QFrame(self.centralwidget)
        self.left_split_frame.setObjectName(u"left_split_frame")
        self.left_split_frame.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout = QVBoxLayout(self.left_split_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.editor_command_label = QLabel(self.left_split_frame)
        self.editor_command_label.setObjectName(u"editor_command_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.editor_command_label.sizePolicy().hasHeightForWidth())
        self.editor_command_label.setSizePolicy(sizePolicy1)
        self.editor_command_label.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.editor_command_label)

        self.editor_command_entry = QPlainTextEdit(self.left_split_frame)
        self.editor_command_entry.setObjectName(u"editor_command_entry")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.editor_command_entry.sizePolicy().hasHeightForWidth())
        self.editor_command_entry.setSizePolicy(sizePolicy2)
        self.editor_command_entry.setMaximumSize(QSize(16777215, 35))
        font = QFont()
        font.setFamilies([u"Monospace"])
        font.setPointSize(9)
        self.editor_command_entry.setFont(font)

        self.verticalLayout.addWidget(self.editor_command_entry)

        self.verticalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.exec_code_button = QPushButton(self.left_split_frame)
        self.exec_code_button.setObjectName(u"exec_code_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.exec_code_button.sizePolicy().hasHeightForWidth())
        self.exec_code_button.setSizePolicy(sizePolicy3)
        self.exec_code_button.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.exec_code_button)

        self.exec_code_entry = QPlainTextEdit(self.left_split_frame)
        self.exec_code_entry.setObjectName(u"exec_code_entry")
        sizePolicy.setHeightForWidth(self.exec_code_entry.sizePolicy().hasHeightForWidth())
        self.exec_code_entry.setSizePolicy(sizePolicy)
        self.exec_code_entry.setMaximumSize(QSize(16777215, 16777215))
        self.exec_code_entry.setFont(font)
        self.exec_code_entry.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.exec_code_entry)

        self.guid_label = QLabel(self.left_split_frame)
        self.guid_label.setObjectName(u"guid_label")

        self.verticalLayout.addWidget(self.guid_label)

        self.guid_entry = QPlainTextEdit(self.left_split_frame)
        self.guid_entry.setObjectName(u"guid_entry")
        sizePolicy2.setHeightForWidth(self.guid_entry.sizePolicy().hasHeightForWidth())
        self.guid_entry.setSizePolicy(sizePolicy2)
        self.guid_entry.setMaximumSize(QSize(16777215, 35))
        self.guid_entry.setFont(font)

        self.verticalLayout.addWidget(self.guid_entry)

        self.verticalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.send_message_button = QPushButton(self.left_split_frame)
        self.send_message_button.setObjectName(u"send_message_button")
        sizePolicy3.setHeightForWidth(self.send_message_button.sizePolicy().hasHeightForWidth())
        self.send_message_button.setSizePolicy(sizePolicy3)
        self.send_message_button.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.send_message_button)

        self.send_message_entry = QPlainTextEdit(self.left_split_frame)
        self.send_message_entry.setObjectName(u"send_message_entry")
        sizePolicy.setHeightForWidth(self.send_message_entry.sizePolicy().hasHeightForWidth())
        self.send_message_entry.setSizePolicy(sizePolicy)
        self.send_message_entry.setMaximumSize(QSize(16777215, 16777215))
        self.send_message_entry.setFont(font)

        self.verticalLayout.addWidget(self.send_message_entry)

        self.verticalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.save_and_play_button = QPushButton(self.left_split_frame)
        self.save_and_play_button.setObjectName(u"save_and_play_button")
        sizePolicy3.setHeightForWidth(self.save_and_play_button.sizePolicy().hasHeightForWidth())
        self.save_and_play_button.setSizePolicy(sizePolicy3)
        self.save_and_play_button.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.save_and_play_button)

        self.spec_file_label = QLabel(self.left_split_frame)
        self.spec_file_label.setObjectName(u"spec_file_label")

        self.verticalLayout.addWidget(self.spec_file_label)

        self.spec_file_entry = QPlainTextEdit(self.left_split_frame)
        self.spec_file_entry.setObjectName(u"spec_file_entry")
        sizePolicy2.setHeightForWidth(self.spec_file_entry.sizePolicy().hasHeightForWidth())
        self.spec_file_entry.setSizePolicy(sizePolicy2)
        self.spec_file_entry.setMaximumSize(QSize(16777215, 35))
        self.spec_file_entry.setFont(font)

        self.verticalLayout.addWidget(self.spec_file_entry)

        self.verticalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.get_scripts_button = QPushButton(self.left_split_frame)
        self.get_scripts_button.setObjectName(u"get_scripts_button")
        sizePolicy3.setHeightForWidth(self.get_scripts_button.sizePolicy().hasHeightForWidth())
        self.get_scripts_button.setSizePolicy(sizePolicy3)
        self.get_scripts_button.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.get_scripts_button)

        self.script_upload_folder_label = QLabel(self.left_split_frame)
        self.script_upload_folder_label.setObjectName(u"script_upload_folder_label")

        self.verticalLayout.addWidget(self.script_upload_folder_label)

        self.script_upload_folder_entry = QPlainTextEdit(self.left_split_frame)
        self.script_upload_folder_entry.setObjectName(u"script_upload_folder_entry")
        sizePolicy2.setHeightForWidth(self.script_upload_folder_entry.sizePolicy().hasHeightForWidth())
        self.script_upload_folder_entry.setSizePolicy(sizePolicy2)
        self.script_upload_folder_entry.setMaximumSize(QSize(16777215, 35))
        self.script_upload_folder_entry.setFont(font)

        self.verticalLayout.addWidget(self.script_upload_folder_entry)

        self.script_download_folder_label = QLabel(self.left_split_frame)
        self.script_download_folder_label.setObjectName(u"script_download_folder_label")

        self.verticalLayout.addWidget(self.script_download_folder_label)

        self.script_download_folder_entry = QPlainTextEdit(self.left_split_frame)
        self.script_download_folder_entry.setObjectName(u"script_download_folder_entry")
        sizePolicy2.setHeightForWidth(self.script_download_folder_entry.sizePolicy().hasHeightForWidth())
        self.script_download_folder_entry.setSizePolicy(sizePolicy2)
        self.script_download_folder_entry.setMaximumSize(QSize(16777215, 35))
        self.script_download_folder_entry.setFont(font)

        self.verticalLayout.addWidget(self.script_download_folder_entry)


        self.toplevel_layout.addWidget(self.left_split_frame)

        self.right_split_frame = QFrame(self.centralwidget)
        self.right_split_frame.setObjectName(u"right_split_frame")
        self.right_split = QVBoxLayout(self.right_split_frame)
        self.right_split.setObjectName(u"right_split")
        self.console_label = QLabel(self.right_split_frame)
        self.console_label.setObjectName(u"console_label")

        self.right_split.addWidget(self.console_label)

        self.console_output = QTextBrowser(self.right_split_frame)
        self.console_output.setObjectName(u"console_output")
        self.console_output.setEnabled(True)
        self.console_output.setMinimumSize(QSize(400, 0))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(61, 56, 70, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(92, 84, 105, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(76, 70, 87, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(31, 28, 35, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(41, 37, 47, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(36, 31, 49, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        brush7 = QBrush(QColor(224, 27, 36, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush7)
        brush8 = QBrush(QColor(0, 0, 0, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush8)
        brush9 = QBrush(QColor(30, 28, 35, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush9)
        brush10 = QBrush(QColor(255, 255, 220, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush8)
        brush11 = QBrush(QColor(255, 255, 255, 127))
        brush11.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush8)
        brush12 = QBrush(QColor(31, 28, 35, 127))
        brush12.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        brush13 = QBrush(QColor(43, 39, 49, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush13)
        self.console_output.setPalette(palette)
        font1 = QFont()
        font1.setFamilies([u"Monospace"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.console_output.setFont(font1)

        self.right_split.addWidget(self.console_output)


        self.toplevel_layout.addWidget(self.right_split_frame)


        self.gridLayout.addLayout(self.toplevel_layout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tabletop Simulator DevServer", None))
        self.editor_command_label.setText(QCoreApplication.translate("MainWindow", u"Editor Command", None))
        self.editor_command_entry.setPlainText(QCoreApplication.translate("MainWindow", u"xterm -e vim", None))
        self.editor_command_entry.setPlaceholderText("")
        self.exec_code_button.setText(QCoreApplication.translate("MainWindow", u"Execute Code", None))
        self.exec_code_entry.setPlainText(QCoreApplication.translate("MainWindow", u"print('Hello, table!')", None))
        self.guid_label.setText(QCoreApplication.translate("MainWindow", u"GUID", None))
        self.guid_entry.setPlainText(QCoreApplication.translate("MainWindow", u"-1", None))
        self.send_message_button.setText(QCoreApplication.translate("MainWindow", u"Send Message With Table", None))
        self.send_message_entry.setPlainText(QCoreApplication.translate("MainWindow", u"key=value", None))
        self.save_and_play_button.setText(QCoreApplication.translate("MainWindow", u"Save and Play", None))
        self.spec_file_label.setText(QCoreApplication.translate("MainWindow", u"Specfile Save/Load Location", None))
        self.spec_file_entry.setPlainText(QCoreApplication.translate("MainWindow", u"your_specfile.json", None))
        self.spec_file_entry.setPlaceholderText("")
        self.get_scripts_button.setText(QCoreApplication.translate("MainWindow", u"Get New Scripts", None))
        self.script_upload_folder_label.setText(QCoreApplication.translate("MainWindow", u"Script Folder (For Upload)", None))
        self.script_upload_folder_entry.setPlainText(QCoreApplication.translate("MainWindow", u"test_scripts", None))
        self.script_download_folder_label.setText(QCoreApplication.translate("MainWindow", u"Script Folder (For Download)", None))
        self.script_download_folder_entry.setPlainText(QCoreApplication.translate("MainWindow", u"test_scripts", None))
        self.console_label.setText(QCoreApplication.translate("MainWindow", u"Console Output", None))
#if QT_CONFIG(whatsthis)
        self.console_output.setWhatsThis(QCoreApplication.translate("MainWindow", u"Output sent from TTS is displayed here.", None))
#endif // QT_CONFIG(whatsthis)
    # retranslateUi

