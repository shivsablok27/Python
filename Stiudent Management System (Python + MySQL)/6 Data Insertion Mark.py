import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="holy")
mycursor=mydb.cursor()
print("STUDENT INFORMATION SYSTEM")

while True:
    ch=input(" DO YOU WANT TO STORE STUDENT MARKS Y/N : ")
    if ch=='n' or ch=='N':
        break
    
    rn=int(input("ENTER THE ROLL NO: "))
    mycursor.execute("select NAME from STUDENT1 WHERE ROLLNO= "+ str(rn))
    #print(mycursor)
    mr=mycursor.fetchone()
    if mr==[]:
        print('NO RECORD FOUND IN RECORD')
    else:
        #NA=mycursor.fetchone()[0]
        NA=mr[0].upper()
        print("STUDENT NAME: "+NA+'\n')
        
        eng=input("ENTER MARKS IN ENGLISH: ")
        p=input("ENTER MARKS IN PHYSICS: ")
        c=input("ENTER MARKS IN CHEMISTRY: ")
        m=input("ENTER MARKS IN MATHS: ")
        op=input("ENTER MARKS IN OPTIONAL: ")
    
        #mycursor.execute(" insert into student1 values('"+str(rollno)+"' , '"+name+"' ,'"+str(marks)+"')  ")
        st=" insert into MARK values(" +str(rn)+ "," +eng+","+p+","+c+","+m+","+op+")"
        #print(st)
        mycursor.execute(st)
        mydb.commit()
        print("STUDENT MARKS SUCCESSFULLY SAVE")
        

print("GOOD BYE...!\nHAVE A NICE DAY......!")