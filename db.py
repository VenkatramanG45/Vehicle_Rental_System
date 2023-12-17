import sqlite3
import hashlib

class DB_Helper:
    def __init__(self):
        self.conn = sqlite3.connect("DATA.db")
        cur = self.conn.cursor()
        
        cur.execute(""" 
        CREATE TABLE IF NOT EXISTS userdata(
            ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            username VARCHAR(255) NOT NULL,
            email TEXT NOT NULL,
            password VARCHAR(255) NOT NULL,
            role varchar(255)  NOT NULL
        )
        """)
        print("Created")
        
    
    def Insert_User(self, username, email, password, role):
        cur = self.conn.cursor()
        hashed_email = hashlib.sha256(email.encode()).hexdigest()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cur.execute('INSERT INTO userdata (username, email, password, role) VALUES (?, ?, ?, ?)',
                    (username, hashed_email, hashed_password, role))
        self.conn.commit()
        print("User saved to the database")


