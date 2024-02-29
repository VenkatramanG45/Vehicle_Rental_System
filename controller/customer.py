from models.db import DB_Helper
from models.cars import CarDb
from models.bikes import BikeDB

cars = CarDb()
bike = BikeDB()
db = DB_Helper()


class Customer:
    
                  
    def CarCustomer(self):
        
        #Car_Customer_View()
        while True:
            try:
                ch = input()
                if ch=="V":
                   print(cars.Available_Car())
                elif ch=="S":
                    print(cars.Search_Car())
                elif ch =="B":
                    cars.Borrow_Car()
                elif ch =="R":
                   cars.pay_rent()
                elif ch=="H":
                    cars.View_Prev_Rentals()
                elif ch=="quit":
                    print()
                    print()
                    break
        
            except Exception as e:
                print(e)


    
    def BikeCustomer(self):
        #Bike_Customer_View()
        while True:
            try:
                
                ch = input()
                if ch=="V":
                    bike.Available_Bike()
                elif ch=="S":
                    bike.Search_Bike()
                elif ch =="B":
                    bike.Borrow_Bike()
                elif ch =="R":
                    bike.Pay_Rent()
                elif ch=="H":
                    bike.View_Prev_Rentals()
                elif ch=="quit":
                    print()
                    print()
                    break
        
            except Exception as e:
                print(e)
    