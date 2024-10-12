# Reading multiple lines from previously written
#- '04_student_records2.csv'

import csv
ob=open('04_student_records2.csv','r')
obr=csv.reader(ob)

for i in obr:

        #print(i)
        print(i[0],'   ',i[2])
ob.close()