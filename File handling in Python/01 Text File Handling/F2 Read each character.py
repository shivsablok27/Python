# WAP to read each character of the text from the file
ob=open("0igt.txt", 'r')
st=ob.read()

for i in st:
    print(i)
ob.close()