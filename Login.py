print("WELCOME TO LOGIN PANEL...")

import argon2
import pymysql as sql

class Login:
    def __init__(self):
        self.connection = sql.connect(
            host="localhost",#YOUR DATABASE host name
            user="root", #YOUR DATABASE user name
            passwd="", #YOUR DATABASE PASS
            database="library" #YOUR DATABASE name
        )
        self.cursor = self.connection.cursor()
        self.pass_hasher = argon2.PasswordHasher()

    def login_2(self):
        try:
            email_val = input("ENTER YOUR EMAIL...\n")
            
          
            query = "SELECT email_val, pass_val FROM idpass WHERE email_val=%s"
            self.cursor.execute(query, (email_val,))
            data = self.cursor.fetchone()

            ##CHECKING DATA EXISTS OR NOT
            if data:
                self.pass_fncn(data)
            else:
                print("YOUR EMAIL IS INVALID")
                self.login_2()

        except Exception as e:
            print(f"Error: {e}")

    def pass_fncn(self, data):
        try:
            
            pass_val = input("ENTER YOUR PASSWORD...\n")
            
            if self.pass_hasher.verify(data[1], pass_val):
                print("PASSWORD VERIFIED SUCCESSFULLY...")
                from Login_Sow import interface
            else:
                print("PASSWORD IS WRONG")
                self.pass_fncn(data)
        except argon2.exceptions.VerifyMismatchError:
            print("PASSWORD IS WRONG")
            self.pass_fncn(data)

object = Login()
object.login_2()
