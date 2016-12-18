#!/usr/bin/env python

import asyncio
from collections import namedtuple
import datetime
import json
import random
import socket
import struct
import websockets

Header = namedtuple('Header', 'channel command len')
Pixel = namedtuple('Pixel', 'r g b')

async def opc(websocket, path):
    OPC_DEFAULT_PORT = 7890
    HOST = ''

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, OPC_DEFAULT_PORT))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                header_size = struct.calcsize('!BBH')
                header = Header._make(struct.unpack('!BBH', data[:header_size]))
                pixels = [Pixel._make(p) for p in struct.iter_unpack('!BBB', data[header_size:])]

                await websocket.send(json.dumps(pixels))


start_server = websockets.serve(opc, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
