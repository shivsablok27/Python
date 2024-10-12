# w+ mode
ob=open("F18.txt", "w+")
ob.write("Hello Everybody!!")
ob.write("\nMy name is Shiv Sablok")
ob.write("\nI am studying in class - XII Science")
ob.write("\nSchool - Holy Public School")
ob.seek(0) # Control to the beginning of the file.
print (ob.read())
ob.close()
