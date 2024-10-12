'''
tell() function:
  • tell() method can be used to get the position of File Handle.
  • tell() method returns current position of file object.
  • This method takes no parameters and returns an integer value.
  • It also takes the counting of two more characters for \n which is present at the
    end of each line which comprises of two characters \ and n.
seek () function:
  • This is used to change the position of the File Handle to a given specific position.
  • seek() takes a integral parameter to locate a new position.
'''
ob=open ("0igt.txt", "r")
s=ob.readline()
print (s)
print (ob.tell())

s=ob.readline()
print (s)
print (ob.tell())

ob.seek(3) # Takes control directly to the 3rd character of the file.
print (ob.readline())
ob.close()