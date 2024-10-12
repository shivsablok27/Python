import mysql.connector
import os
mydb=mysql.connector.connect(host="localhost",user="root",passwd="123",database="holy")
mycursor=mydb.cursor()
print("**********************MEDICAL INFORMATION SYSTEM***********************")
while True:
  ch=input("\nDO YOU WANT TO UPDATE MEDICINE INFORMATION Y/N : ")
  if ch=='n' or ch=='N':
        break
  mid=input('PLEASE ENTER MEDICINE ID: ')
  st='SELECT * FROM MEDICAL WHERE M_ID='+mid
  #print(st)
  mycursor.execute(st)
  mr=mycursor.fetchall()
  if mr==[]:
            print('MEDICINE ID ', mid,' NOT FOUND IN RECORD')
  else:  
    
    print('\n***************CURRENT MEDICINE INFORMATION AS FOLLOWS**************')
    #print(mr)
    for x in mr:
        print('MEDICINE ID',x[0])
        print('MEDICINE NAME: ',x[1])
        print('CATEGORY: ',x[2])
        print('COMPANY: ',x[3])
        print('DOSAGE: ',x[4])
        print('PRICE: ',x[5])
        print('EXP_DATE: ',x[6])
        print("******************************************************************\n")
    
    print("WHAT DO YOU WANT TO UPDATE: ")
    print('1. MEDICINE NAME: ')
    print('2. CATEGORY :')
    print('3. COMAPANY :')
    print('4. DOSAGE:')
    print('5. PRICE :')
    print ("NOTE- EXPIRY DATE OF MEDICINE CAN NOT BE CHANGED!")
    ch=int(input('PLEASE ENTER THE CHOICE: '))
    if ch==1:
            print('\nEXISTING MEDICINE NAME :',x[1])
            na=input('ENTER UPDATED MEDICINE NAME: ')
            ch1=input("DO YOU WANT TO UPDATE MEDICINE NAME Y/N")
            if ch1=='Y' or ch1=='y':
                st="UPDATE MEDICAL SET name='"+na.upper() + "' WHERE M_ID = "+mid
                #print(st)
                mycursor.execute(st)
                print("\nMEDICINE NAME SUCCESSFULLY UPDATED......!")
    elif ch==2:
            print("YOU WANT TO CHANGE THE CATEGORY OF ", x[1], "MEDICINE ID: ", x[0])
            print('\nEXISTING CATEGORY :',x[2])
            ad=input('ENTER THE NEW CATEGORY: ')
            ch1=input("DO YOU WANT TO UPDATE MEDICAL CATEGORY Y/N")
            if ch1=='Y' or ch1=='y':
                st="UPDATE MEDICAL SET CATEGORY='"+ad.upper() + "' WHERE M_ID= "+mid
                #print(st)
                mycursor.execute(st)
                print("\nMEDICAL CATEGORY SUCCESSFULLY UPDATED......!")
    elif ch==3:
            print("YOU WANT TO CHANGE MEDICINE COMPANY ", x[1], "  MEDICINE ID: ", x[0])
            print('\nEXISTING MEDICINE COMPANY :',x[3])
            cl=input('ENTER THE MEDICINE COMPANY: ')
            ch1=input("DO YOU WANT TO UPDATE COMPANY Y/N")
            if ch1=='Y' or ch1=='y':
                st="UPDATE MEDICAL SET COMPANY='"+cl.upper() + "' WHERE M_ID= "+mid
                #print(st)
                mycursor.execute(st)
                print("\nMEDICINE COMPANY SUCCESSFULLY UPDATED......!")
    elif ch==4:
            print("YOU WANT TO CHANGE THE DOSAGE OF ", x[1], "  MEDICINE ID: ", x[0])
            print('\nEXISTING MEDICAL DOSAGE :',x[4])
            sec=input('ENTER THE NEW DOSAGE TYPE: ')
            ch1=input("DO YOU WANT TO UPDATE DOSAGE TYPE Y/N")
            if ch1=='Y' or ch1=='y':
                st="UPDATE MEDICAL SET DOSAGE='"+sec.upper() + "' WHERE M_ID= "+mid
                #print(st)
                mycursor.execute(st)
                print("\nMEDICAL DOSAGE SUCCESSFULLY UPDATED......!")
    elif ch==5:
            print("YOU WANT TO CHANGE THE PRICE OF ", x[1], "  MEDICINE ID: ", x[0])
            print('\nEXISTING PRICE :',x[5])
            mo=input('ENTER THE NEW PRICE: ')
            ch1=input("DO YOU WANT TO UPDATE PRICE Y/N")
            if ch1=='Y' or ch1=='y':
                st="UPDATE MEDICAL SET PRICE='"+mo.upper() + "' WHERE M_ID= "+mid
                #print(st)
                mycursor.execute(st)
                print("\nPRICE OF MEDICINE SUCCESSFULLY UPDATED......!")
mydb.commit()
