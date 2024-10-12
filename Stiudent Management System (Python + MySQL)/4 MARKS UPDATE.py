import mysql.connector
import os
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="holy")
mycursor=mydb.cursor()
print("****************************STUDENT MARKS INFORMATION SYSTEM**************************************")
while True:
  ch=input("\nDO YOU WANT TO UPDATE STUDENT MARKS Y/N : ")
  if ch=='n' or ch=='N':
       break
  r=int(input('PLEASE ENTER STUDENT ROLL NO: '))
  st='SELECT * FROM MARK WHERE ROLLNO='+str(r)
  #print(st)
  mycursor.execute(st)
  myrecords=mycursor.fetchall()
  if myrecords==[]:
            print('ROLL NUMBER ', r,' NOT FOUND IN RECORD')
  else:  
    print('\n*********************CURRENT MARKS INFORMATION AS FOLLOWS**************************')
    for x in myrecords:
        print('ROLL NO',x[0])
        print('ENGLISH: ',x[1])
        print('PHYSICS: ',x[2])
        print('CHEMISTRY: ',x[3])
        print('MATHS: ',x[4])
        print('OPTIONAL: ',x[5])
        print("***********************************************************************************\n")
    
    print("UPDATE STUDENT MARKS IN: ")
    print('1. ENGLISH: ')
    print('2. PHYSICS: ')
    print('3. CHEMISTRY: ')
    print('4. MATHS: ')
    print('5. OPTIONAL: ')
    ch=int(input('PLEASE ENTER THE CHOICE: '))
    if ch==1:
            print('\nEXISTING MARKS IN ENGLISH :',x[1])
            m=input('ENTER UPDATED MARKS IN ENGLISH: ')
            ch1=input("\nDO YOU WANT TO UPDATE MARKS IN ENGLISH Y/N")
            if ch1=='Y' or ch1=='y':
                st="UPDATE MARK SET ENGLISH="+m + " WHERE rollno= "+str(r)
                #print(st)
                mycursor.execute(st)
                mydb.commit()
                print("\nSTUDENT MARKS IN ENGLISH SUCCESSFULLY UPDATED......!")
    elif ch==2:
            print('\nEXISTING MARKS IN PHYSICS :',x[2])
            m=input('ENTER UPDATED MARKS IN PHYSICS: ')
            ch1=input("\nDO YOU WANT TO UPDATE MARKS IN PHYSICS Y/N")
            if ch1=='Y' or ch1=='y':
                st="UPDATE MARK SET PHYSICS="+m + " WHERE rollno= "+str(r)
                #print(st)
                mycursor.execute(st)
                mydb.commit()
                print("\nSTUDENT MARKS IN PHYSICS SUCCESSFULLY UPDATED......!")
    elif ch==3:
            print('\nEXISTING MARKS IN CHEMISTRY :',x[3])
            m=input('ENTER UPDATED MARKS IN CHEMISTRY: ')
            ch1=input("\nDO YOU WANT TO UPDATE MARKS IN CHEMISTRY Y/N")
            if ch1=='Y' or ch1=='y':
                st="UPDATE MARK SET CHEMISTRY='"+m + "' WHERE rollno= "+str(r)
                #print(st)
                mycursor.execute(st)
                mydb.commit()
                print("\nSTUDENT MARKS IN CHEMISTRY SUCCESSFULLY UPDATED......!")
    elif ch==4:
            print('\nEXISTING MARKS IN MATHS:',x[4])
            m=input('ENTER UPDATED MARKS IN MATHS: ')
            ch1=input("\nDO YOU WANT TO UPDATE MARKS IN MATHS Y/N")
            if ch1=='Y' or ch1=='y':
                st="UPDATE MARK SET MATHS='"+m + "' WHERE rollno= "+str(r)
                #print(st)
                mycursor.execute(st)
                mydb.commit()
                print("\nSTUDENT MARKS IN MATHS SUCCESSFULLY UPDATED......!")
    elif ch==5:
            print('\nEXISTING MARKS IN OPTIONAL:',x[5])
            m=input('ENTER UPDATED MARKS IN OPTIONAL: ')
            ch1=input("\nDO YOU WANT TO UPDATE MARKS IN OPTIONALY/N")
            if ch1=='Y' or ch1=='y':
                st="UPDATE MARK SET OPTIONAL='"+m + "' WHERE rollno= "+str(r)
                #print(st)
                mycursor.execute(st)
                mydb.commit()
                print("\nSTUDENT MARKS IN OPTIONAL SUCCESSFULLY UPDATED......!")            

print("GOOD BYE...!\nHAVE A NICE DAY......!")
