# Reading csv files
import csv
ob=open('01_Student_records.csv','r') # ob is the file_object
obr=csv.reader(ob) # obr is the file_reader_object
print(obr) # shows the address of file reader object in memory
for i in obr:
    print(i) # Return full data in the form of lists
ob.close()

ob=open('01_Student_records.csv','r')           
obr=csv.reader(ob)         
for j in obr:
    print (j[0],j[1],j[2],j[3]) # Indexes data (column wise)
ob.close()

