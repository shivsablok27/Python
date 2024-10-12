from tabulate import tabulate 
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="123",database="holy")
mycursor=mydb.cursor()
mycursor.execute("show databases")
for x in mycursor:
   y= tabulate(x, tablefmt='psql')
   print (y)
   
