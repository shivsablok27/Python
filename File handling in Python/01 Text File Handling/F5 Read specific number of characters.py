# WAP to read only a specific number of
# characters at a time from the text file.
ob=open('0igt.txt', 'r')
st=' '
while st:
    st=ob.read(2)
    print (st, end=' ')
ob.close()