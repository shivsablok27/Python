#  WAF to find the sum of series:
# 2/a + 3/a^2 + 5/a^3 + 7/a^4 + ...... + n (Note- Prime number relation)
def series4():
    f=1
    s=0.0
    for j in range (2,N+1):
        if N%j==0:
            f=0
            break
    if f==1:
        for i in range (1, N+1):
            s=s+ ((2i-1)/(a**i))
    return s
a=int(input("Enter the value of a: "))
N=int(input("Enter the number of terms: "))
Result=series4()
print ("Calculated result of series = ",Result)
