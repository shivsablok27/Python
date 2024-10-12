#Call by reference
def abc(s):
    l=len(s)
    for i in range (0,l):
        s[i]=s[i]-10
    print ("Inside tye function:", s)
L=eval(input("Enter a list:"))
print ("Before func. call: ",L)
abc(L)
print ("After func. call: ",L)
