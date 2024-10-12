import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="holy")
mycursor=mydb.cursor()
mycursor.execute("update EMP set SAL=2000 where EMPNO=8499")
mydb.commit()