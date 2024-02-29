from controller.customer import Customer

customer = Customer()
class bike_Customer_View:
    def Bike_Customer(self):
        print("Press V to search View  the available Bikes")
        print("Press S to Search Bike by Name")
        print("Press B Borrow a bike")
        print("Press H to view Previous Rentals")
        print("Press R to Pay Rent")
        print()
        print()
        customer.BikeCustomer()