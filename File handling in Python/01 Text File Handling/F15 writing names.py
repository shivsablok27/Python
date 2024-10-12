# Write any five names:
ob=open("F15.txt", "w")
for i in range (5):
    s=input("Enter the name: ")
    ob.write(s+' ')
ob.close()

ob2=open("F15.txt","r")
print (ob2.read())
ob2.close()
    