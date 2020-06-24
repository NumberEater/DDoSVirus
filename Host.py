import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 1234))
s.listen(5)


def main():
    while True:
        clientsocket, address = s.accept()
        while address != None:
            message = input("Enter Message: ")
            messageb = message.encode("utf-8")
            clientsocket.send(messageb)


main()
