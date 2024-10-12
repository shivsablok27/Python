def fun(i=3,j=7):
    i=i+2
    j=j+6
    print (i,j)
    return i
x=9
y=5
print(x,y)
x=fun(x)
print (x,y)
y=fun(x)
print (x,y)