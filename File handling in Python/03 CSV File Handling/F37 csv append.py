# Append mode 
import csv
ob=open('05_Employee_records.csv','a',newline='')   
obw=csv.writer(ob)           
obw.writerow(['E_No.','E_Name','E_Salary'])
i=1
ch='y'
while ch=='y' or ch=='Y':
    eno=input("Enter the Employee number: ")
    ename=input("His Name: ")
    esal=input("His Salary: ")
    st=[eno,ename,esal]
    obw.writerow(st)
    ch=input('Do you want to enter more data? Y/N')
ob.close()
    