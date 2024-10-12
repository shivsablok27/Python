# 3. Keyword Argument/ Named Argument
def simpleint (p, r, t):
    si=(p*r*t)/100
    return si
x=simpleint(t=4,p=5000,r=2.5)
print ("SI=", x)
x=simpleint(t=2,r=4,p=900)
print ("SI=", x)
x=simpleint(5000,4,6)
print ("SI=", x)