# a+ mode
'''
There is also another mode called a+ mode that is used for
appending(writing) and then reading.
It is almost similar to w+ mode.
'''
ob=open("F20.txt","a+")
ob.write("\n We all are Indians...")
ob.seek(0)
s=ob.read()
print (s)
ob.close()