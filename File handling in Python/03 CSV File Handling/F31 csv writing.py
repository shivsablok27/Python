import csv
ob=open('02_Book_records.csv','w',newline='')   
obw=csv.writer(ob)           
obw.writerow(['Book No.','Book Name','Book Cost'])
i=1
ch='y'
while ch=='y' or ch=='Y':
    bno=input("Enter the Book Number: ")
    bname=input("Enter the Book Name: ")
    bcost=input("Enter the book price: ")
    st=[bno,bname,bcost]
    obw.writerow(st)
    ch=input('Do you want to enter more data? Y/N')
ob.close()
    
