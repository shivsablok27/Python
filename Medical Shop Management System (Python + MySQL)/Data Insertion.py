import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="123",database="holy")
mycursor=mydb.cursor()
while True:
    ch=input("Do you want to insert record into medical table Y/N : ")
    if ch=='n' or ch=='N':
        break
    M_Id=int(input("Enter medicine id: "))
    MNAME=input("Enter medicine name: ")
    CATEGORY=input("Enter category: ")
    COMPANY=input("Enter company: ")
    DOSAGE=input("Enter type of dosage: ")
    PRICE=float(input("Enter the price: "))
    EXP_DATE=input("Enter Expiry date: ")
    query="insert into medical values('{}','{}','{}','{}','{}','{}','{}')"\
    .format(M_Id ,MNAME, CATEGORY, COMPANY, DOSAGE, PRICE, EXP_DATE)
    mycursor.execute(query)
mydb.commit()