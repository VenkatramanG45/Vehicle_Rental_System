import sqlite3
import hashlib

class BikeDB:
    
    def __init__(self):
        self.conn = sqlite3.connect("DATA.db",check_same_thread=False,timeout=1000)
        cur = self.conn.cursor()
        
        cur.execute(""" 
        CREATE TABLE IF NOT EXISTS Bike(
            ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            Bike_Name VARCHAR(255) NOT NULL,
            Bike_Color VARCHAR(255) NOT NULL,
            Bike_Num_Plate VARCHAR(255) NOT NULL,
            Travelled_Km INT  NOT NULL,
            Rent INT NOT NULL,
            Rent_Status VARCHAR NOT NULL,
            Security_Deposit INT DEFAULT 0,
            Service_Status VARCHAR(255) NOT NULL,
            RETURNED_DATE varchar(256),
            DAMAGE VARCHAR(256) NOT NULL
        )
        """)
        #print("Bike Database Created")
        
    def Insert_Bike(self, Bike_Name, Bike_Color, Bike_Num_Plate, Travelled_Km, Rent, Rent_Status ,Service_Status, Damage):
        cur = self.conn.cursor()
        cur.execute('INSERT INTO Bike(Bike_Name, Bike_Color, Bike_Num_Plate, Travelled_Km, Rent, Rent_Status ,Service_Status, Damage) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',(Bike_Name, Bike_Color, Bike_Num_Plate, Travelled_Km, Rent, Rent_Status ,Service_Status, Damage))
        self.conn.commit()
        print("User saved to the Bike database")
        cur.close()
    
    def View_Bike(self):
        cur = self.conn.cursor()
        result  = cur.execute('select * from Bike')
        for i in result:
            print(i)
            
    def Search_Bike(self):
        ch = input("Enter Bike Name : ")
        cur = self.conn.cursor()
        result  = cur.execute('select * from Bike where Bike_Name = ?',(ch,))
        for i in result:
            print(i)
            
    def Remove_Bike(self):
        ch = int(input("Enter Bike ID : "))
        cur = self.conn.cursor()
        cur.execute("DELETE from Bike WHERE ID = ?",(ch,))
        self.conn.commit()
        print(f"{ch} is Removed")
        cur.close()
        
    def Change_Deposit(self):
        ch = int(input("Enter the Initial Deposit : "))
        bike_name = input("Enter Bike Name :")
        cur = self.conn.cursor()
        cur.execute('Update Bike set Security_Deposit = ? where Bike_Name = ?', (ch,bike_name))
        self.conn.commit()
        cur.close()
        
    def Borrow_Bike(self):
        Bike = input("Enter Bike Name : ")
        cur = self.conn.cursor()
        res = cur.execute("Select * from Bike where Bike_Name = ?",(Bike,))
        lst = []
        for i in res:
            for j in i:
                lst.append(j)
        self.Deposit = int(input(f"Pay Deposit amount  Rs {lst[5]} :"))        
        cur.execute(f'update Bike set Rent_Status = "Rented" where Bike_Name = ?',(Bike,))
        if self.Deposit == lst[6]:
            print(f"Security Deposit of amount {self.Deposit} paid Successfully")
        else:
            print(f'Paid Rs {self.Deposit}')
        print(len(lst))
        self.conn.commit()
        cur.close()    
        
        
    def Update(self, total_km, vehicle_brand):
        cur = self.conn.cursor()
        cur.execute('update Bike set Travelled_Km = ? where Bike_Name = ?',(total_km,vehicle_brand,))
        self.conn.commit()
        cur.close()
        
    def Update_Service(self, total_km, vehicle_brand):
        if total_km>=3000:
            cur = self.conn.cursor()
            cur.execute('update Bike set Travelled_Km = ?,  Service_Status = "Need Service" where Bike_Name = ?',(total_km,vehicle_brand,))
            self.conn.commit()
            cur.close()
            
            
    def Bike_Rent(self,bike):
        cur = self.conn.cursor()
        cur.execute('Update  Bike set Rent_Status = "Not Rented" where Bike_Name = ?', (bike,))
        self.conn.commit()
        cur.close()
        
        
    def Available_Bike(self):
        cur = self.conn.cursor()
        for i in cur.execute('SELECT * from Bike where Travelled_km < 1000 and Rent_Status  = "Not Rented" and Service_Status = "Serviced"'):
            print(i)
        self.conn.commit()

    def Pay_Rent(self):  
        self.conn = sqlite3.connect("DATA.db", check_same_thread=False)
        cur = self.conn.cursor()
        #CarDb.__init__(self)
        cur = self.conn.cursor()
        cur.execute("""Create Table  if not  exists Bike_Trans(
            user varachar(256),
            email varchar(256),
            vehicle_type varchar(256),
            vehicle_brand varchar(256),
            travelled_km varchar(256),
            rent INT,
            rent_status varchar(256),
            Damage varchar(256),
            returned_Date varchar(256)
            )"""
        )
        print("Transaction DB created")
        
 
        cur = self.conn.cursor()
        user = input("Enter Username : ")
        email = input("Enter Email : ")
        hashed_email = hashlib.sha256(email.encode()).hexdigest()
        vehicle_type = input("Choose Vehicle : ")
        vehicle_brand = input("Brand : ")
        Damage = input("Damage Level  :")
        travelled_km = int(input("Travelled Km : "))
        res= cur.execute("select Rent from Bike")
        lst=[]
        for i in res:
            for j in i:
                lst.append(j)
        #print(lst)
        rent = lst[0]
        if travelled_km >=1500:
            rent+=15//100
            
        result = cur.execute("select Travelled_Km from Bike where Bike_Name = ?",(vehicle_brand,))
        ls=[]   
        for i in result:
            for j in i:
                ls.append(j)
        total_km = ls[0]+travelled_km
        #print(total_km)
        if total_km >=3000:
            self.Update_Service(total_km, vehicle_brand)
        else:
            self.Update(total_km, vehicle_brand)
        rent_status = int(input(f"Pay  rent amount {rent} : "))
        #print(rent_status)
        s=""
        if rent_status == rent:
            s+="Paid"
        elif rent_status!=rent:
            print("Pay Correct Amount")
        else:
            s+='Not Paid'
        returned_date = cur.execute('select datetime("now", "localtime")')
        date = ""
        for i in returned_date:
            for j in i:
                date+=str(j)
        print(date)
        cur.execute('INSERT INTO Bike_Trans(user, email ,vehicle_type ,vehicle_brand ,travelled_km ,rent, rent_status, Damage, returned_Date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',(user, hashed_email, vehicle_type, vehicle_brand, travelled_km ,rent, s ,Damage, date))
      
        self.Bike_Rent(vehicle_brand)
        self.conn.commit()
        cur.close()
        
    def View(self):
        cur = self.conn.cursor()
        for i in cur.execute("select * from Bike_Trans"):
            print(i)
        self.conn.commit()
        cur.close()
        
    def View_Prev_Rentals(self):
        user = input("Enter username : ")
        cur = self.conn.cursor()
        for i in cur.execute("Select * from Bike_Trans where user = ?", (user,)):
            print(i)
        self.conn.commit()
        
    
        

