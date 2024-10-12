import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="123",database="holy")
mycursor=mydb.cursor()
nm=input("Enter the Medicine ID:  ")
mycursor.execute("select * from Medical where M_ID="+ nm )
print ()
for x in mycursor:
    print (x)
    print ()
    print("Medicine ID: ",x[0])
    print("Medicine Name: ",x[1])
    print("Category of Medicine: ",x[2])
    print("Name of Company: ",x[3])
    print("Form of Dosage: ",x[4])
    print("Estimated Price per pkt.: ",x[5])
    print("Date of Expiry as per shop storage: ",x[6])
    print()
    