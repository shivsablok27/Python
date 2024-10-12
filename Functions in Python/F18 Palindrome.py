#Write a Function to find whether a given no is palindrome no or not.
def PalindromeCheck ():
    choice=input("Palindrome Check-- String or Number? ")
    if choice=='Number' or choice=='number':
        n=int(input("Enter number:"))
        temp=n
        s=0
        while n>0:
            r=n%10
            s=s*10+ r
            n=n//10
        if temp==s:
            print("The number is a palindrome!")
        else:
            print("The number is not a palindrome!")
#########################################################################            
    elif choice=='string' or choice=='String':
        if (st==st[::-1]) :
            print ("String is a palindrome!")
        else:
            print ("String is not a palindrome!")
PalindromeCheck()
