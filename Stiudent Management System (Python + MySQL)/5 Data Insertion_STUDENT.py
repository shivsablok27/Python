import mysql.connector
import os
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="holy")
mycursor=mydb.cursor()
print("STUDENT INFORMATION SYSTEM")

while True:
    
    
    ch=input(" DO YOU WANT TO STORE STUDENT INFORMATION Y/N : ")
    
    os.system("cls") 
    if ch=='n' or ch=='N':
        break
    
    mycursor.execute("select MAX(ROLLNO) from STUDENT1")
    rn=mycursor.fetchone()[0]
    #print(rn)
    if rn is None:
        rollno=1
    else:
        rollno = rn + 1
    print('Rollno: ', rollno)
    name=input("Enter Student Name: ")
    addr=input("Enter the Address: ")
    cla=input("Enter the Class: ")
    Sec=input("Enter the Section: ")
    Mo=input("Enter the Mobile No: ")

    #mycursor.execute(" insert into student1 values('"+str(rollno)+"' , '"+name+"' ,'"+str(marks)+"')  ")
    st=" insert into student1 values(" +str(rollno)+ ",'" +name+ "','"+addr+"','" +cla+"','" +Sec+"','" +Mo+"')"
    #print(st)
    mycursor.execute(st)
    print("STUDENT INFORMATION SUCCESSFULLY SAVE")
    mydb.commit()