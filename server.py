'''
import socket
from _thread import *

import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = "localhost"
port = "5050"

server_ip = socket.gethostbyname(socket.gethostname()) # replace with server var if not working 

try:
    s.bind((server, port)) # we've bound this server to this address
except socket.error as e:
    print(str(e))

s.listen(2) # two connections 
print("Waiting...")

currentId = "0"
pos=["0:50,50", "1:100,100"]

def threaded_client(conn):
    global currentId, pos
    conn.send(str.encode(currentId))
    currentId = "1"
    reply = ""

    while True:
        try:
            data = conn.recv(2048)

'''