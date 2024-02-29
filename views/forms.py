#from Sockets.cleint import Client
#from Sockets.server import Server
from controller.admin import UserDb

user= UserDb()

class View:
    def Print_menu(self):
        print("*********WELCOME**********")
        print()
        print("PRESS 1 to Sign up")
        print("PRESS 2 to Sign In")
        print()

        user.Get_Input()
        
 
        