#WAF to find the sum of two numbers

#Designing function body
def SumOfNumbers(x,y):
    s=x+y
    print ("Sum of the numbers is=", s)
    return s
#Using function out of function body
SumOfNumbers(4,5)
SumOfNumbers(-8,100)
#By user input
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
SumOfNumbers(a,b)


