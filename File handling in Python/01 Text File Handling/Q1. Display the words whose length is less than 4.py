'''
Question: Write a method DISPLAYWORDS() in python to read lines from a text file 0igt.txt,
and display the words whose length is less than 4.
'''
def displayword(): # Defining the given function
    z=1 # Initialising line number
    ob=open('0igt.txt','r')  # opening the given file
    lst=ob.readlines()   # Read all lines
    for line in lst :    # Read a line at a time
        x=line.split()  # Splitting each line into words
        print('line no :',z, end=' ')  #showing line number
        for word in x:      # Access one word at a time from given line
            if len(word)<4: # Applying the condition given in question    
                print(word,end= ', ') # Printing the words that satisfy given condition
        print() # For Spacing
        z=z+1   # Increment in the line number
    ob.close()   # Closing the file
    
displayword() # Calling the function