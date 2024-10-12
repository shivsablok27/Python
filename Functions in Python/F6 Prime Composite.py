#WAF to check whether a given number is prime or composite
def primecheck (N):
    f=1
    for i in range (2,N):
        if N%i==0:
            f=0
            break
    if f==1:
        print (N, "is a prime number")
    else:
        print (N, "is a composite number")
primecheck(2)
primecheck(8)
num=int(input("Enter the number to check: "))
primecheck(num)