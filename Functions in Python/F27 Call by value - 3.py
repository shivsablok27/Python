def fun(i,j=7):
    i=i+2
    j=j+6
    print (i,j)
    return i
x=3
y=4
print(x,y)
y=fun(x)
print (x,y)
x=fun(x,y)
print (x,y)