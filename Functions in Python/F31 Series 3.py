#  WAF to find the sum of series:
# a/2! - a/3! + a/4! - a/5! ...... + a/10!
def series3():
    f=1
    s=0.0
    sign=1
    a=int(input("Enter the value of a: "))
    for j in range (2,11):
        f=f*j
        s=s+(a/f)*sign
        sign = sign*-1
    print ("Calculated result of series = ",s)
series3()


    
    
