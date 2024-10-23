print("WELCOME TO REGISTRATION...")
import argon2
def register():
    import pymysql as sql
    import datetime
    connection = sql.connect(
        host="localhost",#YOUR DATABASE host name
        user="root", #YOUR DATABASE user name
        passwd="", #YOUR DATABASE PASS
        database="library" #YOUR DATABASE name
    )
    cursor = connection.cursor()
    date=datetime.datetime.now()
    year = date.strftime("%Y-%m-%d")

    try:
        email_val = str(input("""
                        ENTER YOUR EMAIL FOR REGISTRATION...
        
                            """))
        if "@" in email_val and "gmail.com" in email_val:
            execute="SELECT COUNT(*) FROM idpass WHERE email_val=%s"
            cursor.execute(execute,email_val)
            result =cursor.fetchone()
            if result[0]>0:
                print("EMAIL ALREADY EXISTS..\n")
                register()
            else:
                pass_val = input("""
                        ENTER YOUR PASSWORD:
                                  
                            """)
                pass_hasher_opn = argon2.PasswordHasher()
                hashed= pass_hasher_opn.hash(pass_val)
                execute_val ="INSERT INTO idpass(email_val,pass_val,date_added) VALUES(%s,%s,%s)"
                data = (email_val,hashed,year)
                cursor.execute(execute_val,data)
                connection.commit()
                print("REGISTRATION COMPLETED..\n")
                from Login import login

        else:
            print("INVALID EMAIL...\n")
            register()


    except:
        print("VALUE ERROR...\n")
        register()


register()