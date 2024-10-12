# Loading dictionary
import pickle

ob=open("F23.dat", "rb")
d=pickle.load(ob)
print (d)

print ()

for name in d:
    print (name)

print ()

for name in d:
    print (name, d[name])

ob.close()