from controller.admin import Authorize_Admin

admin = Authorize_Admin()

class CarAdmin:

    def CarAdmin(self):
        print("Press H to History of Transactions")
        print("Press V to View available Car")
        print("Press S to Search Car by Name")
        print("Press U to View User Data")
        print("Press C to change Security deposit Amount For the Borrower")
        print("Press A to Add Car")
        print("Press R to Remove Car")
        print()
        print()
        admin.Car_Admin()