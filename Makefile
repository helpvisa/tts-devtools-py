WORKPATH =
DISTPATH =
BINARY_NAME = tts_devserver_gui
PYINSTALLER_FLAGS = -F
TARGET = gui.py


ifdef WINDOWS
	WORKPATH = build/windows
	DISTPATH = release/windows
	BINARY_NAME = tts_devserver_gui.exe
else
	WORKPATH = build/linux
	DISTPATH = release/linux
endif


all:
	pyinstaller -F \
		-n $(BINARY_NAME) \
		--workpath=$(WORKPATH) \
		--distpath=$(DISTPATH) \
		$(TARGET)
