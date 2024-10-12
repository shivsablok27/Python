#   1   +      a/1!   +   (a^2)/2!  +    (a^3)/3!   +  ---------  (upto n terms)
import math
def series5 (a,n):
    s=0.0
    for i in range (0, n+1):
        s=s+  (a**i)/(math.factorial(i))
    return s
p=int (input ("Enter the value of a: "))
q=int (input ("Enter the value of n: "))
Result = series5 (p,q)
print ("Result of the series is ", Result)
    