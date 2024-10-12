# WAP to read text file, find and print no. of
# uppercase ch., lowercase ch, digits, spaces, special ch. 
ob=open('0igt.txt', 'r')
st=ob.read()
print (st)
u=0
l=0
d=0
s=0
sp=0
for i in st:
    if i.isupper():
        u=u+1
    elif i.islower():
        l=l+1
    elif i.isdigit():
        d=d+1
    elif i.isspace():
        s=s+1
    else:
        sp=sp+1
print ("Number of uppercase characters: ", u)
print ("Number of lowercase characters: ", l)
print ("Number of digits characters: ", d)
print ("Number of special characters: ", sp)
print ("Number of spaces: ", s)
# for verification:
if u+l+d+s+sp==len(st):
    print ("Program OK ✔✔")
else:
    print ("Mistake in program ✖ ✖")
ob.close()