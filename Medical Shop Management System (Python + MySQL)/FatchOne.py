#How to fetch one record of a table at run time
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="123",database="holy")
mycursor=mydb.cursor()
mycursor.execute("select * from mybook")
row=mycursor.fetchone()
print (row)
while row is not None:
    print(row)
    row = mycursor.fetchone()