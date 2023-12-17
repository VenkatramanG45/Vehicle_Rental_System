from db import DB_Helper
#from server import Server
from cleint import Client

class Main():
    
    def Print_menu(self):
        print("*********WELCOME**********")
        print()
        print("PRESS 1 to Sign up")
        print("PRESS 2 to Sign In")
        print()
        
    def GetInput(self):
        #self.userid=int(input("Enter user id:"))
        self.username=input("Enter the Name:")
        self.email=input("Enter Email:")
        self.password = input("Enter the Password:")
        self.role = input("Role : Admin or Customer: ")
        
        
        db.Insert_User(self.username,self.email,self.password,self.role)
        
    def Get_Choice(self):
        
        while True:
            try:
                choice=int(input())
                if choice==1:
                    self.GetInput()
        
                elif choice==2:
                    Client()
                     
            except Exception as e:
              print(e)

    
db = DB_Helper()

def main():
    main1 = Main()
    main1.Print_menu()
    main1.Get_Choice()
    
   
    

if __name__ == "__main__":
    main()
