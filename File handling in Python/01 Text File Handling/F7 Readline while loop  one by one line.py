# Read and print each line in an organised way
ob=open("0igt.txt","r")
st=' '
n=1
while st:
    st=ob.readline()
    print (n,st,end='')
    n=n+1
ob.close()
