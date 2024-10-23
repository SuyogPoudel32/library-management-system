
##Make database first!!



# import pymysql as sql
# connection = sql.connect(
        # host="localhost",#YOUR DATABASE host name
        # user="root", #YOUR DATABASE user name
        # passwd="", #YOUR DATABASE PASS
        # database="library" #YOUR DATABASE name
# )
# cursor = connection.cursor()
# cursor.execute("""
#                CREATE TABLE IF NOT EXISTS data(
#                book_id INT PRIMARY KEY AUTO_INCREMENT,
#                book_name VARCHAR(255),
#                author VARCHAR(255),
#                genre VARCHAR(255),
#                publication_year VARCHAR(255),
#                language VARCHAR(100),
#                number_pages INT,
#                date_added VARCHAR(100)
#                )
               
#                """)
# ##FOR ADDING VALUES::
# execute = ("""INSERT INTO data(book_name,author,genre,publication_year,isbin,language,number_pages,date_added) 
#                VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
#                 """)
# data = [
# ('To Kill a Mockingbird', 'Harper Lee', 'Fiction', '1960', '9780061120084', 'English', 281, '2024-09-15'),
# ('1984', 'George Orwell', 'Dystopian', '1949', '9780451524935', 'English', 328, '2024-09-15'),
# ('The Great Gatsby', 'F. Scott Fitzgerald', 'Classic', '1925', '9780743273565', 'English', 180, '2024-09-15'),
# ('The Catcher in the Rye', 'J.D. Salinger', 'Fiction', '1951', '9780316769488', 'English', 277, '2024-09-15'),
# ('Pride and Prejudice', 'Jane Austen', 'Romance', '1813', '9780141439518', 'English', 279, '2024-09-15'),
# ('Moby Dick', 'Herman Melville', 'Adventure', '1851', '9781503280786', 'English', 635, '2024-09-15'),
# ('War and Peace', 'Leo Tolstoy', 'Historical Fiction', '1869', '9781853260629', 'Russian', 1225, '2024-09-15'),
# ('The Hobbit', 'J.R.R. Tolkien', 'Fantasy', '1937', '9780547928227', 'English', 310, '2024-09-15'),
# ('The Alchemist', 'Paulo Coelho', 'Adventure', '1988', '9780062315007', 'English', 208, '2024-09-15'),
# ('Brave New World', 'Aldous Huxley', 'Dystopian', '1932', '9780060850524', 'English', 288, '2024-09-15')
# ]
# cursor.executemany(execute,data)
# connection.commit()

# import pymysql

# # Connect to the database
# connection = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='suyog123poudel',
#     database='library'  # Your database name
# )

# try:
#     with connection.cursor() as cursor:
#         # 1. Set a user-defined variable to use in the next query
#         set_variable_query = "SET @new_id = 0;"
#         cursor.execute(set_variable_query)
        
#         # 2. Re-sequence the remaining records in the idpass table
#         resequence_query = """
#         UPDATE idpass
#         SET id_val = (@new_id := @new_id + 1)
#         ORDER BY id_val;
#         """
#         cursor.execute(resequence_query)
#         connection.commit()

#         # 3. Get the current maximum id_val from the idpass table
#         get_max_id_query = "SELECT MAX(id_val) FROM idpass;"
#         cursor.execute(get_max_id_query)
#         max_id_val = cursor.fetchone()[0]

#         # 4. Reset the AUTO_INCREMENT value to the next available ID in idpass
#         reset_auto_increment_query = f"ALTER TABLE idpass AUTO_INCREMENT = {max_id_val + 1};"
#         cursor.execute(reset_auto_increment_query)
#         connection.commit()

# finally:
#     connection.close()

# print("IDs resequenced and AUTO_INCREMENT reset.")




###IF YOU WANT TO MAKE ID SEQUENCE SERIALLY THEN EXECUTE THIS CODE!!
import pymysql

# Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='suyog123poudel', #Your pass
    database='library'  # Your database name
)

try:
    with connection.cursor() as cursor:
        set_variable_query = "SET @new_id = 0;"
        cursor.execute(set_variable_query)
        
        resequence_query = """
        UPDATE data
        SET book_id = (@new_id := @new_id + 1)
        ORDER BY book_id;
        """
        cursor.execute(resequence_query)
        connection.commit()

        get_max_id_query = "SELECT MAX(book_id) FROM data;"
        cursor.execute(get_max_id_query)
        max_id_val = cursor.fetchone()[0]


        reset_auto_increment_query = f"ALTER TABLE data AUTO_INCREMENT = {max_id_val + 1};"
        cursor.execute(reset_auto_increment_query)
        connection.commit()

finally:
    connection.close()

print("IDs resequenced and AUTO_INCREMENT reset.")
