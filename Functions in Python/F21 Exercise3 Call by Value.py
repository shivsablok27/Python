# Generate Output:-
def fun (i=3, j=4):
    i=i-2
    j=j*10
    print (i,j)                             # DRY RUN
    return i                      #  x    y    i    j         Output
x=1                              #######################################
y=2                               #  1    2    3    4       
x=fun()                           #            1    40         1   40
print (x,y)                       #  1    2    1    4          1   2
y=fun (x)                         #           -1    40        -1   40         
print (x,y)                       #  1   -1   -1    4          1   -1
x=fun (y)                         #           -3    40        -3   40
print (x,y)                       # -3   -1                   -3   -1
