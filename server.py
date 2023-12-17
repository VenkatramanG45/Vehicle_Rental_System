import sqlite3
import hashlib
import socket
import threading


class Server:
    def __init__(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("localhost", 9999))
        server.listen()

        def handle_connection(c):
           
            c.send("email: ".encode())
            email = c.recv(1024)
            email = hashlib.sha256(email).hexdigest()
            
            c.send("Password: ".encode())
            password = c.recv(1024)
            password = hashlib.sha256(password).hexdigest()
            
            
            conn = sqlite3.connect("DATA.db")
            cur = conn.cursor()
            #cur.execute()
            
            cur.execute("SELECT * FROM userdata WHERE email = ? AND password = ?", (email, password))
            
            
            if cur.fetchall():  
                c.send("Login successfull!".encode())
            else:
                c.send("login Failed!".encode())
                
                
        while True:
            cleint, addr = server.accept()
            threading.Thread(target=handle_connection, args = (cleint,)).start()

server = Server()