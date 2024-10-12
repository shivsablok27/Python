#  WAF to find the sum of series:
# a - a/2! + a/3! - a/4! + ...... (upto n)
def series2():
    f=1
    s=0.0
    sign=1
    a=int(input("Enter the value of a: "))
    n=int(input("Enter the number of terms: "))
    for j in range (1,n+1):
        f=f*j
        s=s+((a/f)*sign)
        sign=sign*-1        
    print ("Calculated result of series = ",s)
series2()
    
    