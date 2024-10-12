from tabulate import tabulate
import mysql.connector
import os
mydb=mysql.connector.connect(host="localhost",user="root",passwd="123",database="holy")
mycursor=mydb.cursor()
print("******************MEDICAL INFORMATION SEARCH SYSTEM*************************\n")
while True:
    ch=input("\nDO YOU WANT TO SEARCH MEDICINE INFORMATION Y/N : ")
    if ch=='n' or ch=='N':
        break
    print(" MEDICINE INFORMATION SEARCH BY: ")
    print('1. M_ID: ')
    print('2. M_NAME :')
    print('3. CATEGORY :')
    print('4. COMAPNY:')
    print('5. DOSAGE :')
    ch=int(input('PLEASE ENTER THE CHOICE: '))
    if ch==1:
        na=input('ENTER MEDICINE ID: ')
        st="SELECT * FROM MEDICAL WHERE M_ID='"+na+"'"
        #print(st)
        mycursor.execute(st)
        mr=mycursor.fetchall()
        #print(mr)
        if mr==[]:
            print('NO MEDICINE FOUND WITH THIS ENTRY ',na.upper())
        else:
            #print(tabulate(mr))
             print('\nUNIQUE MEDICINE EXISTING IN SYSTEM WITH THIS ID :',na.upper())
             headers=['M_ID','MNAME','CATEGORY','COMPANY','DOSAGE','PRICE','EXP_DATE']
             x=tabulate(mr,headers,tablefmt='psql')
             print('\n',x)
    elif ch==2:
        na=input('ENTER MEDICINE NAME: ')
        st="SELECT * FROM MEDICAL WHERE MNAME='"+na+"'"
        #print(st)
        mycursor.execute(st)
        mr=mycursor.fetchall()
        #print(mr)
        if mr==[]:
            print('NO MEDICINE FOUND WITH THIS ENTRY ',na.upper())
        else:
            #print(tabulate(mr))
             print('\nUNIQUE MEDICINE EXISTING IN SYSTEM WITH THIS NAME:',na.upper())
             headers=['M_ID','MNAME','CATEGORY','COMPANY','DOSAGE','PRICE','EXP_DATE']
             x=tabulate(mr,headers,tablefmt='psql')
             print('\n',x)       
    elif ch==3:
        na=input('ENTER MEDICINE CATEGORY: ')
        st="SELECT * FROM MEDICAL WHERE CATEGORY='"+na+"'"
        #print(st)
        mycursor.execute(st)
        mr=mycursor.fetchall()
        #print(mr)
        if mr==[]:
            print('NO MEDICINE FOUND WITH CATEGORY ',na.upper())
        else:
            #print(tabulate(mr))
             print('\nFOLLOWING MEDICINES EXISTING IN SYSTEM WITH CATEGORY :',na.upper())
             headers=['M_ID','MNAME','CATEGORY','COMPANY','DOSAGE','PRICE','EXP_DATE']
             x=tabulate(mr,headers,tablefmt='psql')
             print('\n',x)         
    elif ch==4:
        na=input('ENTER MEDICINE COMPANY: ')
        st="SELECT * FROM MEDICAL WHERE COMPANY='"+na+"'"
        #print(st)
        mycursor.execute(st)
        mr=mycursor.fetchall()
        #print(mr)
        if mr==[]:
            print('NO MEDICINE FOUND WITH THIS COMPANY ',na.upper())
        else:
            #print(tabulate(mr))
             print('\nFOLLOWING MEDICINE FOUND IN THE COMPANY :',na.upper())
             headers=['M_ID','MNAME','CATEGORY','COMPANY','DOSAGE','PRICE','EXP_DATE']
             x=tabulate(mr,headers,tablefmt='psql')
             print('\n',x)
    elif ch==5:
        na=input('ENTER MEDICAL DOSAGE TYPE: ')
        st="SELECT * FROM MEDICAL WHERE DOSAGE='"+na+"'"
        #print(st)
        mycursor.execute(st)
        mr=mycursor.fetchall()
        #print(mr)
        if mr==[]:
            print('NO MEDICINE FOUND WITH THIS DOSAGE ',na.upper())
        else:
            #print(tabulate(mr))
             print('\nFOLLOWING MEDICINES EXISTING WITH THIS DOSAGE :',na.upper())
             headers=['M_ID','MNAME','CATEGORY','COMPANY','DOSAGE','PRICE','EXP_DATE']
             x=tabulate(mr,headers,tablefmt='psql')
             print('\n',x)
             
mydb.commit()
