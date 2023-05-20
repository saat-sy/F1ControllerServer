import socket
import threading
from constants import *
from client_handler import Client
import pyvjoy

IP = ''
ADDRESS = (IP, PORT)
print(IP)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)
server.listen(10)
print(server)
print(socket.gethostname())

j = pyvjoy.VJoyDevice(1)
j.reset()

try:
    while True:
        connection, address = server.accept()
        client = Client(connection, address, j)

        thread = threading.Thread(target=client.recieve_messages)
        thread.start()

        print(f'Active connections = {threading.active_count() - 1}')
except KeyboardInterrupt:
    print("Exit")
