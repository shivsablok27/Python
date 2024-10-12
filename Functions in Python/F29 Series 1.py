#  WAF to find the sum of series:
# a + a/2! + a/3! + a/4! + ...... + a/n!
def series1():
    f=1
    s=0.0
    a=int(input("Enter the value of a: "))
    n=int(input("Enter the number of terms: "))
    for j in range (1,n+1):
        f=f*j
        s=s+(a/f)
    print ("Calculated result of series = ",s)
series1()
    
    