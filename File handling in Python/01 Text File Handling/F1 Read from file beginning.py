'''
• File Handling is the storing of data in a file using a program.
• It allows users to handle files i.e., to read and write files.
• abc.txt file and xyz.py file should be in same folder otherwise path is to be mentioned.
• An Object (denoted by any identifier) is a mediocre which connects abc.txt file to xyz.py file.
• For establishing relation between   abc.txt   and    xyz.py
    Syntax 1:       File_object = open ("Filename", "mode")            
    eg:             ob = open ("abc.txt", "r")
    Syntax 2:       File_object = open ("Path_of_the_file", "mode")     --- by using full path address
    eg:             ob = open ("D:\\Data\\hps\\abc.txt", "r")
• For reading the text from the abc.txt file by python program
    Syntax 1:       Identifier = File_object.read()                     --- reading whole text
    eg:             st = ob.read()
    Syntax 2:       Identifier = File_object.read(reading_limit_upto)   --- reading upto certain character limit
    eg:             st = ob.read(20)
• After finihing, closing the text file
    Syntax:         File_object.close()
    eg:             ob.close()
'''

# WAP to read complete text from the file
'''ob=open("0igt.txt", 'r')
st=ob.read()
print (st)
ob.close()

print ()

#WAP to read a specific number of characters (as passed by the user) from the file

ob=open("0igt.txt", 'r')
st=ob.read(10)              
print (st)
ob.close()

print ()
'''
#After reading once, the second reading starts from where the first reading left
ob=open("0igt.txt", 'r')
print (ob.read(10))
print (ob.read(20))
print (ob.read(50))
print (ob.read())
ob.close()



