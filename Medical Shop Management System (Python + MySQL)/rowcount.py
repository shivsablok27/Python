import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="holy")
mycursor=mydb.cursor()
mycursor = mydb.cursor(buffered=True)
mycursor.execute("select * from emp")
noofrows=mycursor.rowcount
print("No of rows in student table are",noofrows)