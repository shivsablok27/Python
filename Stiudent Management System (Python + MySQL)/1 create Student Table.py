import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="123",database="holy")
mycursor=mydb.cursor()

mycursor.execute("drop table if exists student1")
st="create table student1(\
ROLLNO int(3)primary key,\
NAME varchar(15),\
Address varchar(15),\
Class varchar(5),\
Section varchar(2),\
phone varchar(12))"
mycursor.execute(st)
mydb.commit()
print('Table successfully created ')
