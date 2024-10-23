
print("")
print("""
                                WELCOME TO HOME PAGE\n""")
import argon2
import pymysql as sql
class admin():
    def __init__(self):
        self.connection = sql.connect(
            host="localhost",#YOUR DATABASE host name
            user="root", #YOUR DATABASE user name
            passwd="", #YOUR DATABASE PASS
            database="library" #YOUR DATABASE name
        )
        self.cursor = self.connection.cursor()
        self.pass_hasher = argon2.PasswordHasher()   
    
    def email(self):

        try:
            email_val = input("ENTER YOUR EMAIL...\n")
            self.cursor.execute("SELECT email_val,pass_val FROM idpass WHERE id_val= 1")
            data = self.cursor.fetchone()
            if email_val in data[0]:
                self.password(data)
            else:
                print("THIS EMAIL IS INVALID FOR ADMIN\n")
                self.email()

        except Exception as e:
            print(f" VALUE ERROR {e}" )

    def password(self,data):  
        pass_val = input("ENTER YOUR PASSWORD...\n")
        try:
            if self.pass_hasher.verify(data[1], pass_val):
                print("PASSWORD VERIFIED SUCCESSFULLY...\n")
                from admin import admin_role
            else:
                print("PASSWORD IS WRONG")
                self.pass_fncn(data)
    

        except argon2.exceptions.VerifyMismatchError:
            print("PASSWORD IS WRONG")
            self.password()


    







object1= admin()



def input_fncn():
    while True:
        try:
            input_val= int(input("""
                                 1: FOR ADMIN
                                 2: FOR LOGIN
                                 3: FOR REGISTER AS A NEW MEMBER 
                                 4: FOR EXIT

                                 """))
            if input_val==1:
                object1.email()
            elif input_val==2:
                import Login
            elif input_val==3:
                from registration import register
            elif input_val>=4:
                break

        except:
            print("ERROR.. YOUR VAUE MUST BE INTEGER")
            input_fncn()
input_fncn()