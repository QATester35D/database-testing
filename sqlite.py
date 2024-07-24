from sqllite3tools1 import dataBase
import sqlite3
import pathlib

db_path="C:\\Users\\shawn\\AppData\\Roaming\\DBeaverData\\workspace6\\.metadata\\sample-database-sqlite-1\\Chinook.db"
connection = sqlite3.connect(db_path)
# connection = sqlite3.connect("{db_path}?mode=rw", uri=True) #this didn't work; probably need pathlib.path
cursor = connection.cursor()
# cursor.execute("SELECT * from Album")
cursor.execute("SELECT * from Album WHERE Title Like 'Black Sabbath%' ")
result = cursor.fetchall()
print ("result")

cursor.execute("SELECT Title "
               "FROM Artist a "
                "JOIN Album a2 on a.ArtistId = a2.ArtistId "
                "WHERE a.Name = 'AC/DC' "
                "LIMIT 10")
result = cursor.fetchall()
print ("result")

connection.close()

# db=dataBase('path') #by default main.db
# db.create_table('Students',id='INTEGER PRIMARY KEY AUTOINCREMENT',name='varchar(255)',email="varchar(255)")
# #create_table(table_name:str,**kwargs) 
# db.info('Students')
# '|| 0, id, INTEGER, 0, None, 1 ||'
# '|| 1, name, varchar(255), 0, None, 0 ||'
# '|| 2, email, varchar(255), 0, None, 0 ||'
# #info(table_name:str) return table info,cols,data types
# db.add_to_table('Students',data1) #parametrs: <table_name:str>,<data:dict>
# 'Executing:'
# "INSERT INTO Users5('name', 'email') VALUES('John','John@gmail.com')"
# # db.drop_table('Studets') #drop_table(table_name:str)

