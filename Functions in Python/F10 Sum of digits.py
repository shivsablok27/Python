# WAF that receive a parameter and add the individual digit of the number and return the sum.
def sd(n):
    s=0
    while n>0:
        r=n%10
        s=s+r
        n=n//10
    return s
x=int(input("Enter any number: "))
y=sd(x)
print ("Sum of digits of the number", x, "is",y)
#================================================================================================
x=str(x)
print (x[0], "+", x[1], "=", y)