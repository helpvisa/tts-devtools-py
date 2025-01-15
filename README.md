# TableTop Simulator Dev Server
## A set of tools to aid development in TTS

The Atom plugin for TTS is naturally rather defunct at this juncture, and given
that I'm not prone to coding with VSCode (the only other place a viable plugin
is to be found) I figured it was worth developing a simple set of python
scripts which can interact with the TTS API in order to ease scripting.

The various .py files included in this repository all interface with the TCP
server spun up by TTS when you launch a new game, and some also listen to the
requests made by TTS in order to synchronize scripts (this aspect is still in
the TODO stages). They are completely IDE agnostic and can be used from
within the terminal.

## How to use
You can run any one of the scripts with the -h flag to get a quick rundown of
how they might be used.

```dev_server.py``` spins up a listen server which waits for messages from TTS
on port 39998. A folder must be specified to which the listen server can dump
scripts it receives from TTS upon loading a save; if you want TTS to actually
open newly-created scripts for objects in the text editor of your choice, you
must specify a command that the server can run with the ```-e``` flag, for
example:
```
./dev_server.py /path/to/scripts/folder -e "xterm -e 'vim'"
```

```send_message.py``` interacts with the onExternalMessage() event in TTS. It
allows you to send a table of key=value pairs which can be used by scripted
objects in-game.

```execute_lua_code.py``` allows you to execute lua code on any object in the
loaded game. Use a GUID of ```-1``` instead of an object GUID in order to
execute code in a Global scope. This is useful for templating functions and
trying them out on various in-game objects. For example, you could write some
code into a test_code.lua file and run the command like so (assuming a
POSIX-compliant terminal is at hand):

```
./execute_lua_code.py "67362e" "$(cat ./test_code.lua)"
```

```save_and_play.py``` uses a spec.json file (it can be named anything you want)
to send a set of scripts and xml files to the currently loaded game, triggering
a reload. This is the meat-and-potatoes script, and you'll be running it a lot
when you're done making changes in your editor of choice. In order for it to
work correctly, you must create a JSON file that follows a format like:

```
[
    {
        "name": "Global",
        "guid": "-1",
        "script": "/global/path/to/script.lua",
        "ui": "/global/path/to/definition.xml"
    },
    {
        "name": "Block Square",
        "guid": "67362e",
        "script": "/global/path/to/another/script.lua"
    }
]
```

Once this is setup, ```save_and_play.py``` can be pointed at it and it will act
upon your definitions. The ```script``` and ```ui``` keys can optionally be
omitted, however at least one of the two is required for each object.
