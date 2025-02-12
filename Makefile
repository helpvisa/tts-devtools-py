WORKPATH = build/linux
DISTPATH = release/linux
BINARY_NAME = tts_devserver_gui
PYINSTALLER_FLAGS = -F
TARGET_FOLDER = src
TARGET = __init__.py


all:
	mkdir -p $(WORKPATH)
	mkdir -p $(DISTPATH)
	pyinstaller $(PYINSTALLER_FLAGS) \
		-p $(TARGET_FOLDER) \
		-n $(BINARY_NAME) \
		--workpath=$(WORKPATH) \
		--distpath=$(DISTPATH) \
		$(TARGET_FOLDER)/$(TARGET)

clean:
	rm -rf ./$(WORKPATH)
	rm -rf ./$(DISTPATH)
