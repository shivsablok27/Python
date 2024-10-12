# WAP to count number of uppercase letters in the text
ob=open("0igt.txt", 'r')
st=ob.read(30)
print (st)
co=0
for i in st:
    if i.isupper():
        co=co+1
print ("number of uppercase letters=",co)
ob.close()