#WAF to calculate the simple interest
def simpleinterest(p,r,t):
    si=(p*r*t)/100
    return si
x=simpleinterest(1000,5,2)
print ("Simple interest=",x)

p=float(input("Enter principal: "))
r=float(input("Enter rate: "))
t=float(input("Enter time: "))
print ("simple interest of the given data is = ", simpleinterest(p,r,t))