import sqlite3
import hashlib

class CarDb:
    
    def __init__(self):
        self.conn = sqlite3.connect("DATA.db",check_same_thread=False,timeout=1000)
        cur = self.conn.cursor()
        
        cur.execute(""" 
        CREATE TABLE IF NOT EXISTS Cars(
            ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            Car_Name VARCHAR(255) NOT NULL,
            Car_Color VARCHAR(255) NOT NULL,
            Car_Num_Plate VARCHAR(255) NOT NULL,
            Travelled_Km INT  NOT NULL,
            Rent INT NOT NULL,
            Rent_Status VARCHAR NOT NULL,
            Security_Deposit INT DEFAULT 0,
            Service_Status VARCHAR(255) NOT NULL,
            DAMAGE VARCHAR(255) NOT NULL
        )
        """)
        #print("Car Database Created")
        
    def Insert_Car(self,Car_Name, Car_Color, Car_Num_Plate, Travelled_Km, Rent, Rent_Status ,Service_Status, Damage):
        cur = self.conn.cursor()
        cur.execute('INSERT INTO Cars(Car_Name, Car_Color, Car_Num_Plate, Travelled_Km, Rent, Rent_Status ,Service_Status, Damage) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',(Car_Name, Car_Color, Car_Num_Plate, Travelled_Km, Rent, Rent_Status ,Service_Status, Damage))
        self.conn.commit()
        print("User saved to the Car database")
        cur.close()
        
    def View_Car(self):
        cur = self.conn.cursor()
        query = f"select * from Cars"
        
        result  = cur.execute(query)
        res = cur.fetchall()
        #print(tabulate(res, headers=['Car_Name', 'Car_Color', 'Number_plate', 'Travelled_Km', 'Rent', 'Rent_status', 'Security_Deposit', 'Service_Status' ,'Damage']))
        for i in res:
            print(i) 
              
    def Search_Car(self):
        ch = input("Enter Car Name : ")
        cur = self.conn.cursor()
        result  = cur.execute('select * from Cars where Car_Name = ?',(ch,))
        for i in result:
            print(i)
            
    def Remove_Car(self):
        ch = int(input("Enter Car ID : "))
        cur = self.conn.cursor()
        cur.execute("DELETE from Cars WHERE ID = ?",(ch,))
        self.conn.commit()
        print(f"{ch} is Removed")
        
        
    def Available_Car(self):
        cur = self.conn.cursor()
        for i in cur.execute('SELECT * from Cars where Travelled_km < 1000 and Rent_Status  = "Not Rented" and Service_Status = "Serviced"'):
            print(i)
        self.conn.commit()

    def Search_Car(self):
        ch = input("Enter Car Name : ")
        cur = self.conn.cursor()
        
        res= cur.execute('SELECT * from Cars where Travelled_km < 1000 and Rent_Status  == "Not Rented" and Service_Status = "Serviced" and Car_Name = ?',(ch,))
        for i in res:
            print(i)
        self.conn.commit()
        
    def Change_Deposit(self):
        ch = int(input("Enter the Initial Deposit : "))
        car_name = input("Enter Car Name :")
        cur = self.conn.cursor()
        cur.execute('Update Cars set Security_Deposit = ? where Car_Name = ?', (ch, car_name))
        self.conn.commit()
        cur.close()
        
    def Borrow_Car(self):
        car = input("Enter Car Name : ")
        cur = self.conn.cursor()
        res = cur.execute("Select * from Cars where Car_Name = ?",(car,))
        lst = []
        for i in res:
            for j in i:
                lst.append(j)
        self.Deposit = int(input(f"Pay Deposit amount  Rs {lst[5]} :"))        
        cur.execute(f'update Cars set Rent_Status = "Rented" where Car_Name = ?',(car,))
        if self.Deposit == lst[6]:
            print(f"Security Deposit of amount {self.Deposit} paid Successfully")
        else:
            print(f'Paid Rs {self.Deposit}')
        print(len(lst))
        self.conn.commit()
        cur.close()
        
    def Update(self, total_km, vehicle_brand):
        cur = self.conn.cursor()
        cur.execute('update Cars set Travelled_Km = ? where Car_Name = ?',(total_km,vehicle_brand,))
        self.conn.commit()
        cur.close()
        
    def Update_Service(self, total_km, vehicle_brand):
        if total_km>=3000:
            cur = self.conn.cursor()
            cur.execute('update Cars set Travelled_Km = ?,  Service_Status = "Need Service" where Car_Name = ?',(total_km,vehicle_brand,))
            self.conn.commit()
            
            
    def Car_Rent(self,car):
        cur = self.conn.cursor()
        cur.execute('Update  Cars set Rent_Status = "Not Rented" where Car_Name = ?', (car,))
        self.conn.commit()
        
            
    def pay_rent(self):  
        self.conn = sqlite3.connect("DATA.db", check_same_thread=False)
        cur = self.conn.cursor()
        #CarDb.__init__(self)
        cur = self.conn.cursor()
        cur.execute("""Create Table  if not  exists Transactions(
            user varachar(256),
            email varchar(256),
            vehicle_type varchar(256),
            vehicle_brand varchar(256),
            travelled_km varchar(256),
            rent INT,
            Damage varchar(256),
            rent_status varchar(256),
            returned_Date varchar(256)
            )
        """)
        print("Transaction DB created")
        
 
        cur = self.conn.cursor()
        user = input("Enter Username : ")
        email = input("Enter Email : ")
        hashed_email = hashlib.sha256(email.encode()).hexdigest()
        vehicle_type = input("Choose Vehicle : ")
        vehicle_brand = input("Brand : ")
        Damage = input("Damage :")
        travelled_km = int(input("Travelled Km : "))
        res= cur.execute("select Rent from Cars")
        lst=[]
        for i in res:
            for j in i:
                lst.append(j)
        rent = lst[0]
        if travelled_km >=500:
            rent+=15//100
        
        
            
        result = cur.execute("select Travelled_Km from cars where Car_Name = ?",(vehicle_brand,))
        ls=[]   
        for i in result:
            for j in i:
                ls.append(j)
        total_km = ls[0]+travelled_km
        print(total_km)
        if total_km >=3000:
            self.Update_Service(total_km, vehicle_brand)
        else:
            self.Update(total_km, vehicle_brand)
        rent_status = int(input(f"Pay  rent amount {rent} : "))
        print(rent_status)
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
        self.Car_Rent(vehicle_brand)
        cur.execute('INSERT INTO Transactions(user, email ,vehicle_type ,vehicle_brand ,travelled_km ,rent, rent_status, Damage, returned_Date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',(user, hashed_email, vehicle_type, vehicle_brand, travelled_km ,rent ,s ,Damage, date))
        self.conn.commit()
        cur.close()
        
    def View(self):
        cur = self.conn.cursor()
        for i in cur.execute("select * from Transactions"):
            print(i)
        cur.close()
        
    def View_Prev_Rentals(self):
        user = input("Enter username : ")
        cur = self.conn.cursor()
        for i in cur.execute("Select * from Transactions where user = ?", (user,)):
            print(i)
        self.conn.commit()