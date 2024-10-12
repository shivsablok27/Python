# Tuple Read and Write 
import pickle
ob=open('F29.dat','wb')
student= ('Imran','Himansh','Varun','Arjun','Vishal')
marks= (89,90,91,88,92)
pickle.dump (student,ob)
pickle.dump (marks,ob)
ob.close()

ob=open("F29.dat","rb")
name=input("Enter the name of student to be searched (from the tuple created):")
try:
    sn=pickle.load(ob)
    m=pickle.load(ob)
    for i in range (len(m)):
        if sn[i] == name:
            print ("Student name: ",sn[i])
            print ("Student marks: ", m[i])
except EOFError:
    ob.close()
# Try Except in Python
'''
• The try block is used to check some code for errors i.e. 
  the code inside the try block will execute when there is no error in the program.
• Whereas the code inside the except block will execute whenever the program encounters
  some error in the preceding try block '''