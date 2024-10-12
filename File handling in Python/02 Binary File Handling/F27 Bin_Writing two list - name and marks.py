# Creating two list, one for name and other for marks of students
import pickle
ob=open("F27.dat",'wb')
name=[]
marks=[]
ch='y'
while ch=='y' or ch=='Y':
    n=input("Enter Student name: ")
    m=input("Enter Student Marks: ")
    name.append(n)
    marks.append(m)
    ch=input('Do You want to enter more data? Y/N: ')
pickle.dump(name,ob)
pickle.dump(marks,ob)
ob.close()
# Load Marks in next program