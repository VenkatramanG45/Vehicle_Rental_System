import socket
class Client:
    def __init__(self):
        cleint = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cleint.connect(("localhost", 9999))

       
        message = cleint.recv(1024).decode()
        cleint.send(input(message).encode())
        message = cleint.recv(1024).decode()
        cleint.send(input(message).encode())
        print(cleint.recv(1024).decode())
