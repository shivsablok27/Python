import mysql.connector
from tabulate import tabulate
mydb=mysql.connector.connect(host="localhost",user="root",passwd="123",database="holy")
mycursor=mydb.cursor()
while True:
    ch=input("Do you want to enter the query to get the result: ")
    if ch=='N' or ch=='n':
        break
    quer=input("Enter the query: ")
    mycursor.execute(quer)
    fet=mycursor.fetchall()
    tab=tabulate (fet,tablefmt='psql')
    print (tab)
mydb.commit()