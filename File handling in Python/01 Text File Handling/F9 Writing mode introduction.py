'''
• write() used with 'w' mode is used to write in a file. 
• If python doesnot find our text file, it will create the same by
  the name mentioned in the program.
• It starts writing in the file created as per our input and output.
• If the file exists with that name, the write() used with 'w' mode
  will do overwriting by deleting the previously stored data.
• Each time, we use the run command, write() used with 'w' mode
  will erase previous data and insert new data.
• The text file will be stored along with the python file.
'''
# WAP to store (write) records of students by creating a text file.
ob=open("F9.txt", "w")  
ch= "y"                
while ch=="y" or ch=="Y":
    r=input("Enter the Roll number: " )
    n=input("Enter the name: ")
    c=input("Enter the class & Section: ")
    st= r+"  "+n+"  "+c+ "\n"
    ob.write(st)
    ch=input("Do you want to enter more records? Y/N: ")
ob.close()
    
