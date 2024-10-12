import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="123",database="holy")
mycursor=mydb.cursor()
mycursor.execute("select * from emp")
rows = mycursor.fetchmany(size=4)
for x in rows:
    print (x)
    