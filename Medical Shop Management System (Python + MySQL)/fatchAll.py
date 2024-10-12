import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="123",database="holy")
mycursor=mydb.cursor()
mycursor.execute("select * from medical")
myrecords=mycursor.fetchall()
print (myrecords)
