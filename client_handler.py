import socket
from constants import *

class Client:
    def __init__(self, connection: socket.socket, address: tuple):
        self.connection = connection
        self.address = address

    def recieve_messages(self):
        while True:
            length = self.connection.recv(HEADER).decode(DECODE_FORMAT)
            if type(length) != int:
                print(length)
                break
            if length:
                message = self.connection.recv(length).decode(DECODE_FORMAT)

                if (message == DISCONNECT_MESSAGE):
                    break

                print(message)


        self.close()

    def close(self):
        self.connection.close()