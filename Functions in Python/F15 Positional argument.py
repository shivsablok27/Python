#Passing parameters
# 1. Positional Argument/ Required Arqument
def simpleint(p,r,t):
    si=(p*r*t)/100
    return si
x=simpleint(1000,5,2)
print ("Simple interest =",x)

#To show error:
x=simpleint(1000,5,3,2)
print ("Simple interest=",x) #TypeError: simpleint() takes 3 positional arguments but 4 were given
x=simpleint(1000,5)
print ("Simple interest=",x) #TypeError: simpleint() missing 1 required positional argument: 't'
