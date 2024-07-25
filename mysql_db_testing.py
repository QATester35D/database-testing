################################################################################################
# This file is demo'ing various MySQL statements
#
# Note: For MySQL - python file can't be named "mysql.py" as it causes an error. 
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

#############################################################################
# Standard SQL statement getting a specific address by city_id - Kansas City
# This query is just to confirm that I get the same results in the join
#############################################################################
cur.execute("SELECT address from sakila.address where address.city_id = '262'")
result = cur.fetchall()
print ("check debugger for values")

################################################
# Join statement
################################################
cur.execute("SELECT address "
               "FROM address "
                "JOIN city on address.city_id = city.city_id "
                "WHERE city.city = 'Kansas City' "
                "LIMIT 10")
result = cur.fetchall()
print ("check debugger for values")

#############################################################################
# Getting multiple addresses that have the same city_id - Alberta
# This query is just to confirm that I get the same results in the join
#############################################################################
cur.execute("SELECT address from sakila.address where address.city_id = '300'")
result = cur.fetchall()
print ("check debugger for values")

################################################
# Inner Join statement on the city Lethbridge from Alberta
################################################
cur.execute("SELECT address.address, city.city "
               "FROM address "
                "INNER JOIN city on address.city_id = city.city_id "
                "WHERE city.city_id = '300'")
result = cur.fetchall()
print ("check debugger for values")

################################################
# Left Join statement
################################################


################################################
# Close the database connection when done
################################################
connection.close()