import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="123",database="holy")
mycursor=mydb.cursor()
mycursor.execute("insert into medical values(" + str(1813) + ',' +  'THEOPHYLLINE' + ',' + 'Anti-Asthamatic' + ',' + 'Dr. Reddy' + ',' + 'Tablet' + ',' +  str(45.00) + ',' + '2023-04-28);')
mydb.commit()