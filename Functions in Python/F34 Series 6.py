#   1 + 3/2!  +  5/3!   +  7/4! + --------- (to n terms)

def series6():
    f=1
    s=0.0
    n=int(input("Enter the number of terms: "))
    for j in range (1, n+1):
        f=f*j
        s=s+  ((j*2)-1)/f
    print ("Calculated Result of series: ",s)
series6()