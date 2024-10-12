import pickle
ob=open("F24.dat","wb")
l=[]
ch='y'
while ch=='y' or ch=='Y':
    name=input("Enter Student's Name: ")
    l.append(name)
    ch=input("Do you want to enter more data? Y/N ")
pickle.dump(l,ob)
ob.close()

obr=open("F24.dat","rb")
lst=pickle.load(obr)
print (lst)
obr.close()