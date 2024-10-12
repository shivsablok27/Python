def count ():
    st=input("Enter your string: ")
    a=0
    d=0
    sp=0
    for s in st:
        if s.islower() or s.isupper():
            a=a+1
        elif s.isdigit():
            d=d+1
        elif s.isalnum()==False and s.isspace()==False:
            sp=sp+1
    print ("Number of Alphabets: ",a)
    print ("Number of Digits: ",d)
    print ("Number of Special Characters, excluding space: ",sp)
count()
print ("*"*67)
count()


