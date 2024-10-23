def interface():
    import pymysql as sql
    import datetime
    connection = sql.connect(
      host="localhost",#YOUR DATABASE host name
      user="root", #YOUR DATABASE user name
      passwd="", #YOUR DATABASE PASS
      database="library" #YOUR DATABASE name
    )
    cursor=connection.cursor()
      
    try:
        input_val = int(input("""
                                1: FOR SHOW BOOKS ALL DATA
                                2: FOR BORROW
                                3: FOR RETURN
                                4: FOR HOME PAGE
                                5: FOR EXIT

                                    """))
    except ValueError:
           interface()


    def show_books():
              print(" ")
              print("{:<6}{:<26}{:<17}{:<15}{:<13}{:<10}{:<6}{:<15}{:<15}".format("ID","BOOK NAME","AUTHOR","GENRE","PUBLISH YEAR","LANGUAGE","PAGES","CARRIED BY","CARRIED DATE"))
              execute_show_books="SELECT book_id,book_name,author,genre,publication_year,language,number_pages,carry_off,carry_date FROM data"
              cursor.execute(execute_show_books)
              data = cursor.fetchall()
              for i in data: 
                        print("{:<5}{:<25}{:<22}{:<20}{:<5}{:<12}{:<6}{:<13}{:<25}".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],str(i[7]),str(i[8])))
              print(" ")
              interface()

                     
   
    def borrow(): 
           try:
            input_borrow= input("""
                            WHICH BOOK YOU WANT TO BORROW?
                                
                            """)
            execute_check_book= "SELECT carry_off,carry_date FROM data WHERE book_name=%s"
            execute_book_id="SELECT book_id FROM data WHERE book_name=%s"
            execute_borrow=("SELECT COUNT(*) FROM data WHERE book_name=%s")
            cursor.execute(execute_check_book,input_borrow.upper())
            result_book=cursor.fetchone()
            if result_book[0] ==None and result_book[1]==None:          
                cursor.execute(execute_borrow,input_borrow.capitalize())
                result = cursor.fetchone()
                if result[0]>0:
                    date = datetime.datetime.now()
                    borrow_date = date.strftime("%Y-%m-%d")
                    returning = date + datetime.timedelta(days=30)
                    return_date = returning.strftime("%Y-%m-%d")
                    combine_date = borrow_date + " to " + return_date
                    your_name = str(input("INPUT YOUR NAME: ").capitalize())
                    execute_name = "UPDATE data SET carry_off=%s, carry_date=%s WHERE book_name=%s"
                    data_input = (your_name, combine_date, input_borrow)
                    cursor.execute(execute_name, data_input)
                    connection.commit()
                    print(f"YOU BORROWED {input_borrow.upper()} BOOK FOR 1 MONTHS..")
                    ##FOR BOOK ID NUMBER
                    cursor.execute(execute_book_id,input_borrow)
                    result_book_id = cursor.fetchone()
                    print(" ")
                    print("YOUR BOOK ID IS", result_book_id[0])
                    print(" ")
                    print(" REMEMBER BOOK ID OR YOU GET IT FROM SHOW BOOK DATA!!")
                    interface()
                
                else:
                    print(f"NO RECORD FOUND OF {input_borrow} BOOK")
                    interface()


                    

            else:
                    print("CHOOSE ANOTHER BECAUSE IT IS ALREADY BORROWED...\n")
                    borrow()
           except Exception as e:
                 print("YOUR BOOK NAME DOESN'T FOUND OUR RECORD...")
                 borrow()      


    def retur_book():
           try:
            input_borrow= input("""
                            WHICH BOOK YOU WANT TO RETURN?
                                
                            """).title()
            execute = "SELECT book_name,carry_off,book_id FROM data WHERE book_name=%s"
            cursor.execute(execute,input_borrow)
            result = cursor.fetchone()
            if result[0]==input_borrow.title():
                    input_borrow_name= input("""
                           WHAT IS YOUR NAME?
                                
                                    """).capitalize()
                    
                    if result[1]==input_borrow_name.capitalize():
                          yes_no = str(input("DID YOU REMEMBER YOUR BOOK ID? Y/N "))
                          if yes_no.upper()=="N":
                                print(f"IS THIS YOUR BOOK ID?",result[2])
                                yes_no1 = str(input("Y/N "))
                                if yes_no1.upper()=="Y":
                                      print("THANKS FOR RETURNING BOOK....")
                                      execute_update="UPDATE data SET carry_off=%s,carry_date=%s WHERE book_name=%s"
                                      data_val = (None,None,input_borrow.title())
                                      cursor.execute(execute_update,data_val)
                                      connection.commit()
                                      interface()
                                else:
                                      print(" ")
                                      print("PLEASE CHECK YOUR BOOK ID\n")
                                      show_books()
                          else:
                                try:
                                    input_isbin= str(input("ENTER YOUR BOOK ID: "))
                                    
                                    if input_isbin==str(result[2]):
                                          print("THANKS FOR RETURNING BOOK....\n")

                                          execute_update1="UPDATE data SET carry_off=%s,carry_date=%s WHERE book_name=%s"
                                          data_val1 = (None,None,input_borrow.title())
                                          cursor.execute(execute_update1,data_val1)
                                          connection.commit()
                                          interface()
                                    
                                    else:
                                      print(" ")
                                      print("YOUR BOOK ID IS WRONG!\n")
                                      retur_book()
                                          
                                except:
                                      retur_book()
                    else:
                          print("YOUR DATA IS INVALID/YOU HAVENT TAKE THE BOOK...\n")
                          retur_book()
                        

                        
                  
                  

           except:
                 print("ERROR YOUR DATA IS INVALID...\n")      
                 retur_book()





    while True:
          if input_val==1:
                show_books()
          elif input_val==2:
                borrow()
          elif input_val==3:
                retur_book()
          elif input_val==4:
                from Authentication import object1
          elif input_val>=5:
                break

interface()


