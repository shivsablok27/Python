#Counting number of words starting with vowel:
ob=open("0igt.txt", "r")
st=ob.read()
lst=st.split()
co=0
for word in lst:
    if word[0] in ["A","E","I","O","U","a","e","i","o","u"]:
        print (word, end=' ')
        co+=1
print ("\nNumber of words starting with vowel are :",co)
ob.close()
