from models.db import DB_Helper
from models.bikes import BikeDB
from models.cars import CarDb
from cleint import Client

cars = CarDb()
bike = BikeDB()
db = DB_Helper()

class UserDb:
    def Get_Input(self):
        while True:
            try:
                ch = int(input())
                if ch==1:
                    username = input("Enter Username : ")
                    email = input("Enter Email Id : ")
                    password = input("Enter Password : ")
                    role = input("Enter Role (Admin or Customer) : ")
                    db.Insert_User(username, email, password ,role)
                elif ch == 2:
                    Client()
            except Exception as e:
                print(e)
                
        

class Authorize_Admin:
      
    def Car_Admin(self):
        #CarAdmin()    
        while True:
            try:
                ch = input()
                if ch=="V":
                    print(cars.View_Car())
                elif ch=="S":
                    print(cars.Search_Car())
                elif ch =="C":
                    cars.Change_Deposit()
                elif ch=="A":
                    Car_Name = input("Car Name : ")
                    Car_Color = input("Car Color : ")
                    Car_Num_Plate = input("Number Plate : ")
                    Travelled_Km = int(input("Kilometers(Km) Travelled : "))
                    Rent = int(input("Rent Amount : "))
                    Rent_Status = input("Rent Status (Rented or Not Rented): ")
                    Service_Status = input("Service Status (Serviced or Yet to be Serviced) : ")
                    Damage = input("Damage : ")
                    cars.Insert_Car(Car_Name, Car_Color, Car_Num_Plate, Travelled_Km, Rent, Rent_Status ,Service_Status,Damage)
                elif ch =="R":
                    cars.Remove_Car()
                elif ch =="H":
                    cars.View()
                elif ch=="U":
                    db.View_User()
                elif ch=="quit":
                    print()
                    print()
                    break
            
            except Exception as e:
                print(e)
                    
    
    def Bike_Admin(self):
        #Bikeview()
        while True:
            try:
                ch = input()
                if ch=="V":
                    bike.View_Bike()
                elif ch=="S":
                    bike.Search_Bike()
                elif ch =="C":
                    bike.Change_Deposit()
                elif ch=="A":
                    Bike_Name = input("Bike Name : ")
                    Bike_Color = input("Bike Color : ")
                    Bike_Num_Plate = input("Number Plate : ")
                    Travelled_Km = int(input("Kilometers(Km) Travelled : "))
                    Rent = int(input("Rent Amount : "))
                    Rent_Status = input("Rent Status (Rented or Not Rented): ")
                    Service_Status = input("Service Status (Serviced or Yet to be Serviced) : ")
                    Damage = input("Damage : ")
                    
                    bike.Insert_Bike(Bike_Name, Bike_Color, Bike_Num_Plate, Travelled_Km, Rent, Rent_Status ,Service_Status,Damage)
                elif ch =="R":
                    bike.Remove_Bike()
                
                elif ch=="H":
                    bike.View()
                    
                elif ch=="U":
                    db.View_User()
                
                elif ch=="quit":
                    print()
                    print()
                    break
        
            except Exception as e:
                print(e)