# Writing csv file
# Using a different delimiter other than comma
'''
When we write file using any other delimiter,
the whole data of a single row is embedded into first cell.
That is why comma (,) is a preferable as well as default delimiter.
'''
import csv
ob=open('03_Medicine_records.csv','w',newline='')  
obw=csv.writer(ob,delimiter='*')           
obw.writerow(['M_No','M_Name','M_Company','M_Cost'])
for i in range(3):
    print('Medicine record',(i+1))
    mno=input("Enter the Medicine Number: ")
    mname=input("Enter the Medicine Name: ")
    mcom=input("Enter the Medicine Company: ")
    mcost=input("Enter the Medicine Price per packet: ")
    st=[mno,mname,mcom,mcost]
    obw.writerow(st)
ob.close()
    
