import socket
from constants import *
from client_handler import Client
import pyvjoy

IP = ''
ADDRESS = (IP, PORT)
print(IP)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDRESS)
print(f"Server {socket.gethostname()} started on port {PORT}")

client = {}
vjoy_device_index = 1

try:
    while True:
        data, addr = server.recvfrom(HEADER)
        data = data.decode(DECODE_FORMAT)

        if addr not in client:
            print(f"New connection from {addr}")
            j = pyvjoy.VJoyDevice(vjoy_device_index)
            j.reset()
            client[addr] = Client(j)
            vjoy_device_index += 1

        client[addr].receive_message(data)
except KeyboardInterrupt:
    print("Exit")
