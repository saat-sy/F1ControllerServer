import socket
import threading
from constants import *
from client_handler import Client

IP = ''
ADDRESS = (IP, PORT)
print(IP)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)
server.listen(10)
print(server)
print(socket.gethostname())

while True:
    connection, address = server.accept()
    client = Client(connection, address)

    thread = threading.Thread(target=client.recieve_messages)
    thread.start()

    print(f'Active connections = {threading.active_count() - 1}')
