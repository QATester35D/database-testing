# from sqllite3tools1 import dataBase
import sqlite3
import pathlib

################################################
# Database connection to a SQLite database
################################################
db_path="C:\\Users\\shawn\\AppData\\Roaming\\DBeaverData\\workspace6\\.metadata\\sample-database-sqlite-1\\Chinook.db"
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

################################################
# Standard SQL statement
################################################
# cursor.execute("SELECT * from Album")
cursor.execute("SELECT * from Album WHERE Title Like 'Black Sabbath%' ")
result = cursor.fetchall()
print ("check debugger for values")

################################################
# Join statement
################################################
cursor.execute("SELECT Title "
               "FROM Artist a "
                "JOIN Album a2 on a.ArtistId = a2.ArtistId "
                "WHERE a.Name = 'AC/DC' "
                "LIMIT 10")
result = cursor.fetchall()
print ("check debugger for values")

################################################
# Left Join statement
################################################
cursor.execute("SELECT Customer.FirstName, Customer.LastName,CustomerId "
               "FROM Customer "
                "Left JOIN Invoice "
                "Using (CustomerId) "
                "WHERE Customer.LastName = 'Gonçalves'")
nbrOfOrdersByCustomerId=len(cursor.fetchall()) #getting the number of values returned by the SQL statement
print(f"Number of Orders by CustomerId is: {nbrOfOrdersByCustomerId}") #using f-string formatting

################################################
# Close the database connection when done
################################################
connection.close()