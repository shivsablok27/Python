# CSV reading the previously written file -
#  "02_Book_records.csv"
import csv
ob=open('02_Book_records.csv','r',newline='')   
obr=csv.reader(ob)
for i in obr:
    #print (i)
    print (i[0],'    ',i[1],'    ',i[2]) 
ob.close()
