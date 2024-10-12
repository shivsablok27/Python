ob1=open("0igt.txt", "r")
ob2=open("F13.txt","w")
s=' '
n=0
while(s):
    s=ob1.readline()
    n=n+1
    ob2.write(str(n)+" "+s)
ob1.close()
ob2.close()