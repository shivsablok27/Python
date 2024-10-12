def fun(i=3,j=4):
    i=i-2
    j=j*10
    print (i,j)
    return i
x=1
y=2
x=fun()
print (x,y)
y=fun(x)
print (x,y)
x=fun(y)
print (x,y)