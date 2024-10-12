# Writing Multiple Rows
import csv
ob=open('04_student_records2.csv','w',newline='')   
obw=csv.writer(ob)       

obw.writerow(['Roll','Name','Mark'])
l=[['101','AJAY','89'],
   ['102','ANOOP','77'],
   ['103','TARUN','66'],
   ['104','HARI','58'],
   ['105','GAURAV','47']]
obw.writerows(l)
ob.close()