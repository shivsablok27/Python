# WAP to count the number of lines from the text file that starts with a vowel

ob=open("0igt.txt","r") 
st=' '
c=0 
st=ob.readlines() 
print (st) 
print () 
for i in st: 
    print (i, end='') 
    if i[0] in ['a','e','i','o','u','A','E','I','O','U']:
        c=c+1 
print () 
print ("\n", "Total number of lines starting with vowels are= ",c) 
ob.close() 
