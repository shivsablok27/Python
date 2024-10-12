import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="holy")
mycursor=mydb.cursor()
while True:
    ch=input("Do you want to insert record into student table Y/N : ")
    
    if ch=='n' or ch=='N':
        break
    mycursor.execute("select MAX(ROLLNO) from STUDENT1")
    rn=mycursor.fetchone()[0]
    if rn is None:
        rollno=101
    else:
        rollno = rn + 1
    #rollno=int(input("Enter rollno"))
    print('Rollno=', rollno)
    name=input("Enter name").upper()
    marks=int(input("Enter marks"))
    #mycursor.execute(" insert into student1 values('"+str(rollno)+"' , '"+name+"' ,'"+str(marks)+"')  ")
    mycursor.execute(" insert into student1 values(" +str(rollno)+ ",'" +name+ "'," +str(marks)+ ")")
    mydb.commit()