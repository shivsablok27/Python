# New way of creating w+ mode program

ob=open("F19.txt", "w+")
ob.write("Hello Everybody!!")
ob.write("\nMy name is Shiv Sablok")
ob.write("\nI am studying in class - XII Science")
ob.write("\nSchool - Holy Public School")

st=' '
while st:
    st=ob.readline()
    print (st, end='')
ob.write("\nAddress- Sikandra Road, Agra")
ob.close()