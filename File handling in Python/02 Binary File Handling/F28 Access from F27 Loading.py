# Accessing Lists from F27
# Loading and _Sequential and ordered data arrangement_
import pickle
ob=open('F27.dat','rb')
name=pickle.load(ob)
marks=pickle.load(ob)
print (name, marks)
for i in range (len(marks)):
    print ("Student Name: ",name[i], "\n Marks: ",marks[i])
ob.close()