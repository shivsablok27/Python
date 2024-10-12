# Question: Write a code to print just last line of a file 0igt.txt
ob=open('0igt.txt','r')
print (ob.read())
print ('*'*70)
print ("Main Output: ---- ")
# ___________ Way 1 ___________ 
def displayword():
    z=1
    ob=open('0igt.txt','r')
    lst=ob.readlines()
    print("By Way 1: ",lst[len(lst)-1])       
displayword()
# ___________ Way 2 ____________ 
ob=open('0igt.txt','r')
for i in ob:
    l=ob.readline()
print ("By Way 2:  ",l)