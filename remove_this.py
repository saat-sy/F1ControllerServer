import socket
from constants import *

IP = "127.0.1.1"
ADDRESS = (IP, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)