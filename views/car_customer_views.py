
from controller.customer import Customer
customer = Customer()

class Car_Customer_View:
    def CarCustomer(self):
        print("Press V to View  the list of the available Car")
        print("Press S to Search Car by Name")
        print("Press B Borrow a Car")
        print("Press H to View Previous Rentals")
        print("Press R to Pay Rent")
        print()
        print()
        customer.CarCustomer()