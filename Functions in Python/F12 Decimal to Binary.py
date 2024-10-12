#WAF to convert the decimal number into its equivalent binary number
def binary(n):                        # for n=13    #  r    n    s    p
                                                #############################
    s=0                                             #  1    13   0    1
    p=1                                             #  0    6    1    10
    while n>0:                                      #  1    3    1    100
        r=n%2                                       #  1    1   101   1000
        s=s+ p*r                                    #       0   1101  10000
        p=p*10
        n=n//2
    return s
x=int(input("Enter any decimal number: "))
y=binary(x)
print ("Binary equivalent of", x, "is",y)