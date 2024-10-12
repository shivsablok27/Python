'''
rstrip() method returns a copy of the string by removing
the trailing characters specified as argument.
If the characters argument is not provided,
all trailing whitespaces are removed from the string.
'''

# Remove all new line characters from the text file
# and write in new file
ob1=open("0igt.txt","r")
ob2=open("F14.txt","w")
st=' '
while st:
    st=ob1.readline()
    st=st.rstrip('\n')
    print (st, end='')
    ob2.write(st)
ob1.close()
ob2.close()