from controller.admin import Authorize_Admin

class Bikeview:
    #print("hello")
    def print_menu(self):
        print("Press H to History of Transactions")
        print("Press V to View Bike List")
        print("Press S to Search   Bike by Name")
        print("Press U to View User Data")
        print("Press C to change Security deposit Amount For the Borrower")
        print("Press A to Add Bike")
        print("Press R to Remove Bike")
        print()
        print()
        admin = Authorize_Admin()
        admin.Bike_Admin()