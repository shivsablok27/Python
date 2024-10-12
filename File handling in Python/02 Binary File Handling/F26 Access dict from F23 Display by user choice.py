# Loading Dictionary, display marks according to user choice
import pickle
ob=open("F23.dat", "rb")
d=pickle.load(ob)
print ("Refer this Dictionary:")
for entity in d:
    print (entity,' ', d[entity])
print ()
ch='y'
while ch=='y' or ch=='Y':
    name=input ("Enter the name of the student: ")
    if name in ['Rajat', 'Jatin', 'Amreek']:
        sub=input("Enter the subject to get the marks: ")
        if sub=='Physics':
            print (d[name]['Physics'], 'marks')
        elif sub=='Chemistry':
            print (d[name]['Chemistry'])
        elif sub=='Math':
            print (d[name]['Math'])
    else:
        print ("Name not found!!")
        break
        ch=input("Do you want to search for more? Y/N: ")
ob.close()
        
    