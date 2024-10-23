print("""
                                WELCOME TO ADMIN PAGE\n""")
def admin_role():
    import datetime
    import pymysql as sql
    connection = sql.connect(
            host="localhost",#YOUR DATABASE host name
            user="root", #YOUR DATABASE user name
            passwd="", #YOUR DATABASE PASS
            database="library" #YOUR DATABASE name
    )
    cursor = connection.cursor()
    date= datetime.datetime.now()
    year = date.strftime("%Y-%m-%d")


    try:
        
        input_val = int(input("""
                            1: FOR UPLOAD A BOOK RECORD
                            2: FOR DELETE A BOOK RECORD
                            3: FOR HOMEPAGE
                            4: FOR EXIT

                                """))
        if input_val==3:
             from Authentication import object1
        elif input_val==4:
            exit
    except:
        print("ERROR.. YOUR VAUE MUST BE INTEGER")
        admin_role()
        return
    
    def inputing_val():
            if input_val==1:
                try:
                    book_name=str(input("ENTER BOOK NAME: "))
                    print(" ")
                    author_name=str(input("ENTER AUTHOR NAME: "))
                    print(" ")
                    genre_name=str(input("ENTER GENRE: "))
                    print(" ")
                    publication_year=str(input("ENTER PUBLICATION YEAR: "))
                    print(" ")
                    language_name=str(input("ENTER LANGUAGE NAME: "))
                    print(" ")
                    number_pages=int(input("ENTER NUMBER OF PAGES: "))
                    
                except Exception as e:
                    print("VALUE ERROR...",e)
                    admin_role()
                    


        
                def recheck():
                        if input_val==1:
                            try:
                                print(f"BOOK NAME:",book_name, "AUTHOR NAME: ", author_name, "GENRE NAME: ",genre_name, "PUBLICATION YEAR: ",publication_year, "LANGUAGE: ",language_name, "NUMBER OF PAGES: ",number_pages)
                                yes_no = input("YOUR ALL VALUES ARE CORRECT Y/N?? ")
                                
                                if yes_no.upper()=="Y":
                                    execute = """INSERT INTO data(book_name,author,genre,publication_year,language,number_pages,date_added,carry_off,carry_date)
                                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                                    data = (book_name,author_name,genre_name,publication_year,language_name,number_pages,year,None,None)
                                    cursor.execute(execute,data)
                                    print("UPLOADED SUCCESSFULLY")
                                    connection.commit()
                                    admin_role()
                                    
                                else:
                                    print("LET'S REUPLOAD IT!!\n")
                                    inputing_val()
                            except Exception as e:
                                admin_role()

                recheck()

    inputing_val() 

   
    def deleting_val():
         
         if input_val==2:
              print("{:<10}{:<28}{:<25}{:<15}{:<15}{:<15}{:<15}{:<20}".format("BOOK ID","BOOK NAME","AUTHOR","GENRE","PUBLISH YEAR","LANGUAGE","PAGES","DATE ADDED"))
              cursor.execute("SELECT book_id,book_name,author,genre,publication_year,language,number_pages,date_added FROM data")
              data = cursor.fetchall()
              for i in data:
                    print("{:<8}{:<28}{:<25}{:<20}{:<15}{:<12}{:<15}{:<20}".format(i[0],i[1],i[2],i[3],i[4],i[5],str(i[6]),str(i[7])))
              try:
                   delete_id_val = int(input("ENTER ID VALUE WHICH YOU WANT TO DELETE: "))
                   for i in data:
                        if delete_id_val==int(i[0]):
                            execute=("DELETE FROM data WHERE book_id=%s")
                            cursor.execute(execute,delete_id_val)
                            connection.commit()
                            print(f"ID {delete_id_val} IS DELETED FROM DATA...")

                             
                            
              except ValueError:
                   print("VALUE ERROR.... Please enter a valid integer.")
                   admin_role()


     

    deleting_val()

    

                
            
                
        
        




admin_role()

