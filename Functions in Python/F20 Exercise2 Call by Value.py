# Genrerate output:-
def fun(i,j=7):
    i=i+2
    j=j+6
    print (i,j)                                              # DRY RUN
    return i                                  #  x      y       i      j          Output
x=3                                         ################################################
y=4                                           #   3      4       3      7           3   4
print (x,y)                                   #                  5      13          5   13
y=fun (x)                                     #   3      5       3      5           3   5
print (x,y)                                   #                  5      11          5   11
x=fun (x,y)                                   #   5      5                          5   5
print (x,y)