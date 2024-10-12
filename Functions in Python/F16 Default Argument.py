# 2. Default Argument
def simpleint (p, r=5, t=2):
    si=(p*r*t)/100
    return si
x=simpleint(5000)
print ("SI=", x)
x=simpleint(5000,6)
print ("SI=", x)
x=simpleint(5000,6,3)
print ("SI=", x)

#To show errors
x=simpleint()
print ("SI=", x)         #TypeError: simpleint() missing 1 required positional argument: 'p'
x=simpleint(5000,5,3,4)  
print ("SI=", x)         #TypeError: simpleint() takes from 1 to 3 positional arguments but 4 were given