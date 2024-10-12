#What will be the output of the following code?
def fun(i, j=7):
    i=i+2
    j=j+6
    print ("i=",i, "j=",j)                                  
    return i                                     
x=9                                            
y=5                                              
print ("x=",x, " y=",y)                                                                                                            
x=fun(x)                                          
print ("x=",x, "y=",y)                            
y=fun(x)                                        
print ("x=",x, "y=",y)