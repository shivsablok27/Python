#WAF to input a number from the user and return 1 if number is prime and return zero if the number is not prime (composite).
def primecheck ():
    n=int(input("Enter the number: "))
    f=1
    for i in range (2,n):
        if n%i==0:
            f=0
            break
    return f
x=primecheck()
if x==1:
    print ("Number is prime")
else:
    print ("Number is not prime")