# Open Pixel Control emulator for the browser

This is a really simple implementation of the [Open Pixel Control (OPC)](http://openpixelcontrol.org) protocol that will show an emulation of currently up to 64 pixels in the browser.

The Python program (≥ 3.5) forwards all incoming pixel data from port 7890 to a websocket on port 5678. index.html will then connect to this websocket and set a few `<div>` background colours accordingly. It’s all pretty simple and without much error correction currently and one probably needs to open all programs in a very particular order.

## Start it with:

    $ python3 server.py

open `index.html` in a browser and then run your opc program.

## What do I need?

* Python 3.5 (or later), because it uses `async`/`await` magic
* The Python [websockets](https://pypi.python.org/pypi/websockets) library
