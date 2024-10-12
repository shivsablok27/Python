'''
Introduction to more modes of python:
 • We have already studied r mode for reading , w mode for writing, a for append.
 • Now, we have two more modes here, namely, r+ and w+
 • r+ mode is used to   _first read_    and   _then write_   in a file.
 • w+ mode is used to   _first write_   and   _then read_    in a file.
 • In both r+ and w+ modes, writing is done unlike the "w" mode writing.
   In this, each new execution do appending  (instead of destroying the previous data and inserting
   the new data after each execution).
 • Both the modes r+ and w+ are meant for reading and writing (or vice versa) together
   in the same file.
'''
ob=open("0igt.txt", "r+")
st=' '
while st:
    st=ob.readline()
ob.write("\nMalaika Arora, Kirron Kher and Karan Johar are the Judges")
ob.close()