# Writing and reading in Binary modes.
import pickle

ob1=open("F22.dat","wb")
l=["Shiv", "Amit", "Tanishq", "Hariom"]
pickle.dump(l,ob1)
ob1.close()

ob2=open("F22.dat","rb")
lst=pickle.load(ob2)
print (lst)
ob2.close()