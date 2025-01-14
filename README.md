# TableTop Simulator Dev Server
## A set of tools to aid development in TTS

The Atom plugin for TTS is naturally rather defunct at this
juncture, and given that I'm not prone to coding with VSCode
(the only other place a viable plugin is to be found) I figured
it was worth developing a simple set of python scripts which
can interact with the TTS API in order to ease scripting.

The various .py files included in this repository all
interface with the TCP server spun up by TTS when you launch a
new game, and some also listen to the requests made by TTS in
order to synchronize scripts (this aspect is still in the TODO
stages). They are completely IDE agnostic and can be used from
within the terminal.
