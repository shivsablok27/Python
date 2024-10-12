def fab():
    a=0
    b=1
    print (a)
    for i in range (1,10):
        print(b)
        c=a+b
        a=b
        b=c
fab()