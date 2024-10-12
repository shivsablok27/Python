# WAF to reverse a given number
def rev(n):
    s=0
    while n>0:
        r=n%10
        s=s*10 +r
        n=n//10
    return s
x=int(input("Enter any number: "))
y=rev(x)
print ("Reversed number of", x, "is",y)