################################################################################################
# For MySQL - when dealing with MySQL, the python file can't be named "mysql.py" as it causes an error. 
# Renamed it to "mysql_db_testing.py" and the import succeeded
################################################################################################
import mysql.connector
mydb = mysql.connector.connect(user='root', password='root', database='sakila')

################################################
# Database connection to a MySQL database
################################################
cur = mydb.cursor()

################################################
# Standard SQL statement
################################################
cur.execute("SELECT * from sakila.city")
result = cur.fetchall()
print ("check debugger for values")
