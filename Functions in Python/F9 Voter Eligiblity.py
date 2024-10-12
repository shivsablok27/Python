#WAF to find whether a candidate is valid for vote or not
def voter():
    age=int(input("Enter your age: "))
    if age>=18:
        print ("You are eligible to vote")
    else:
        print ("You are not eligible to vote")
voter()
voter()