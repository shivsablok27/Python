import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="holy")
mycursor=mydb.cursor()
mycursor.execute("delete from emp where ename='seth'")
mydb.commit()