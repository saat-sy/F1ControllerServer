import socket
import threading
from constants import *
from client_handler import Client
import pyvjoy

IP = ''
ADDRESS = (IP, PORT)
print(IP)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDRESS)
print(server)
print(socket.gethostname())

j = pyvjoy.VJoyDevice(1)
j.reset()

client = Client(j)

try:
    while True:
        data, addr = server.recvfrom(HEADER)
        data = data.decode(DECODE_FORMAT)
        client.receive_message(data)
except KeyboardInterrupt:
    print("Exit")
