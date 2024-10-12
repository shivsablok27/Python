import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="holy")
mycursor=mydb.cursor()

mycursor.execute("drop table if exists MARK")
st="create table Mark(\
ROLLNO int(3)primary key,\
English numeric(3),\
Physics numeric(3),\
Chemistry numeric(3),\
Maths numeric(3),\
Optional numeric(3),\
FOREIGN KEY (ROLLNO) REFERENCES STUDENT1(ROLLNO))"
mycursor.execute(st)
mydb.commit()
mydb.commit()
print('MARKS TABLE SUCCESSFULLY CREATED ')
