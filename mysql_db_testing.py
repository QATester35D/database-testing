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
# Standard SQL statements
################################################
cur.execute("SELECT * from sakila.city")
result = cur.fetchall()
print ("check debugger for values")

# Get the count for the rental table
cur.execute("select count(rental_id) from sakila.rental")
result = cur.fetchall()
print (f"The total record count for the Rental table is: {result[0][0]}")

# Get the average payment amount from the payment table for Mary Smith
cur.execute("select avg(amount) from sakila.payment where customer_id = '1'")
result = cur.fetchall()
print (f"The average amount spent by Mary Smith before formatting is: {result[0][0]}")
currency_string = '${:,.2f}'.format(result[0][0])
print (f"The formated amount spent is now: {currency_string}")

# Get the total amount spent by Mary Smith
cur.execute("select sum(amount) from sakila.payment where customer_id = '1'")
result = cur.fetchall()
currency_string = '${:,.2f}'.format(result[0][0])
print (f"The total amount spent by Mary Smith is: {currency_string}")

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

##################################################################################
# Inner Join statement on the city Lethbridge - matching city_id from both tables
##################################################################################
cur.execute("SELECT address.address, city.city "
               "FROM address "
                "INNER JOIN city on address.city_id = city.city_id "
                "WHERE city.city_id = '300'")
result = cur.fetchall()
print ("check debugger for values")

################################################
# Left Join statement - Returns all records from the left table, and the matched records from the right table
################################################
cur.execute("SELECT customer.first_name, customer.last_name, payment.payment_id, payment.amount "
               "FROM sakila.customer "
                "LEFT JOIN sakila.payment ON customer.customer_id = payment.customer_id "
                "ORDER BY customer.last_name ")
result = cur.fetchall()
print ("check debugger for values")

################################################
# Close the database connection when done
################################################
mydb.close()