#Call by value
def abc(a,b):
    a=a+2
    b=b+5
    print ("Inside the function:    ",a," ",b)
x=3
y=7
print ("Before the function call:",x," ",y)
abc(x,y)
print ("After the function call:",x," ",y)
