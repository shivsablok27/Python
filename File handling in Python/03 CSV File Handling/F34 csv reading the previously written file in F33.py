# Reading the previously written file - '03_Medicine_records.csv'
''' If we are writing a file with a particular delimiter,
    then to read the same file we have to use the same delimiter
    otherwise it will be a cause of error. '''
import csv
ob=open('03_Medicine_records.csv','r',newline='')    
obr=csv.reader(ob,delimiter='*')     
for i in obr:
    #print(i)
    print(i[0],'   ',i[1],'   ',i[2],'   ',i[3]) 
ob.close()

''' 1st output is for: print (i)
    2nd output is for: print(i[0],' ',i[1],' ',i[2],' ',i[3])
    3rd output is for: delimiter='$' - Causes an error
'''