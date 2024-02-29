#from db import DB_Helper
#from controller.admin import Authorize_Admin
from views.bikeview import Bikeview
from views.carview import CarAdmin
from views.Bike_customer_views import bike_Customer_View
from views.car_customer_views import Car_Customer_View

#from controller.customer import Customer
#from . import main
import sqlite3
import hashlib
import socket
import threading

#m = Authorize_Admin()
#customer = Customer()
bike_Admin_view = Bikeview()
car_Admin_view = CarAdmin()
bike_customer_view = bike_Customer_View()
car_customer_view = Car_Customer_View()

class Server():
    
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
            cur.execute("SELECT * FROM userdata WHERE (email = ? AND password = ?)", (email, password))
                
            if cur.fetchall():
                c.send("Login successfull!".encode())
                result = cur.execute("Select * from userdata where (email = ? AND password = ?)", (email, password))
                lst = []
                for i in result:
                    for j in i:
                        lst.append(j)
                    
                #print(lst)
                if lst[-1]=="Admin":
                    #print(lst[-1])
                    while True:     
                        try:
                            ch = input("Choose Vehicle Car or Bike or quit : ")
                            if ch =="Car":
                                car_Admin_view.CarAdmin()
                                pass
                            elif ch == "Bike":
                                bike_Admin_view.print_menu()
                            elif ch == "quit":
                                break
                                        
                        except Exception as e:
                            print(e)
                                    
                elif lst[-1] == "Customer": 
                    while True:
                        try:
                            character = input("Choose Vehicle Car or Bike or quit : ")
                            if character =="Car":
                                car_customer_view.CarCustomer()
                                pass
                            elif character == "Bike":
                                bike_customer_view.Bike_Customer()
                                pass
                            elif character == "quit":
                                break
                             
        
                                            
                        except Exception as e:
                            print(e)
                    
         
            else:
                c.send("login Failed!".encode())
                 
                
        while True:
            cleint, addr = server.accept()
            threading.Thread(target=handle_connection, args = (cleint,)).start()
            

server = Server()