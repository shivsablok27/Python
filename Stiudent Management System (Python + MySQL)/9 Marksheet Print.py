from tabulate import tabulate
import mysql.connector
import os
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="holy")
mycursor=mydb.cursor()
print("****************************STUDENT MARKSHEET PRINTING SYSTEM**************************************")
ch='Y'
while ch=='Y' or ch=='y':
  
  r=int(input('PLEASE ENTER STUDENT ROLL NO: '))
  st='SELECT * FROM STUDENT1 WHERE ROLLNO='+str(r)
  mycursor.execute(st)
  mr=mycursor.fetchall()      #student data
  if mr==[]:
            print('ROLL NUMBER ', r,' NOT FOUND IN RECORD')
  else:
      m='SELECT * FROM MARK WHERE ROLLNO='+str(r)
      #print(st)
      mycursor.execute(m)
      marks=mycursor.fetchall()      #marks data
        
      print('\n*********************STUDENT DETAIL**************************')
      print("\n", "*"*62)
      #print(mr)
      for x in mr:
        print('ROLL NO     :',x[0])
        print('Name        : ',x[1])
        print('ADDRESS     : ',x[2])
        print('CLASS       : ',x[3])
        print('SECTION     : ',x[4])
        print('MOBILE NO   : ',x[5])
        print("\n", "*"*62)
        print("SUBJECT     : MARKS")
        print("*"*62)
      for x in marks:
        #print('ROLL NO   : ',x[0])
        print('ENGLISH     : ',x[1])
        print('PHYSICS     : ',x[2])
        print('CHEMISTRY   : ',x[3])
        print('MATHS       : ',x[4])
        print('OPTIONAL    : ',x[5])
        print("\n", "*"*62)

      
  ch=input("\nDO YOU WANT TO SHOW MARK SHEET OF ANY OTHER STUDENT Y/N : ")
  
print("GOOD BYE...!\nHAVE A NICE DAY......!")

