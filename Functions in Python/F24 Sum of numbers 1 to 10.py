def Sum():
    s=0
    n=int(input("Calculate the sum of natural numbers from 1 to: "))
    for i in range(1,n+1):
        s=s+i
    print("Sum of Natural Numbers from 1 to", n, "=", s)
    return s
Sum()