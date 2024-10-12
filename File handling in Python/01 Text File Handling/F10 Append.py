'''
• write() can also use the mode 'a' stands for append.
  This is also used to write in a file. 
• If python doesnot find our text file,
  it will create the same by the name mentioned in the program.
• It starts writing in the file created as per our input and output.
• If the file already exists with that name,
  the write() will add the next output in the previously written text.
• It will now, not erase the previous text,
  it will append the newly generated output into the text file.
• Each time, we use the run command, write() used with 'a' mode will
  append the new data to previous data.
• The text file will be stored along with the python file.
'''
ob=open("F10.txt", "a")  
ch= "y"                
while ch=="y" or ch=="Y":
    r=input("Enter the Roll number: " )
    n=input("Enter the name: ")
    c=input("Enter the class & Section: ")
    st= r+"  "+n+"  "+c+ "\n"
    ob.write(st)
    ch=input("Do you want to enter more records? Y/N: ")
ob.close()
    