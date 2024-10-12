# Board Question: Generate output for the following code:
Msg1= "WeLcOME"
Msg2= "GUeSTs"                                              # (Given)
Msg3= ""                                    ##################################################
for I in range (0, len(Msg2)+1):                 #   Msg1=   W   e   L   c   O   M   E
    if Msg1[I]>="A" and Msg1[I]<="M":            #           0   1   2   3   4   5   6
        Msg3=Msg3 + Msg1[I]                   
    elif Msg1[I]>="N" and Msg1[I]<="Z":          #  Msg2=    G   U   e   S   T   s
        Msg3=Msg3 + Msg2[I]                      #           0   1   2   3   4   5
                                                             
                                                             # (Execution)
    else:                                   ##################################################
        Msg3=Msg3 + "*"                          #  Msg3=    G   *   L   *   T   M   E
print (Msg3)                                     #           0   1   2   3   4   5   6
                                            ##################################################
                                                             # Output = G*L*TME