#WAF to calculate factorial of any number
def fact(n):
    f=1
    for i in range (n,0,-1):
        f=f*i
    return f
s=fact(4)
print ("factorial=",s)
n=int(input("Enter any number: "))
s=fact(n)
print("Factorial=",s)