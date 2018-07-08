inputString=input("Please enter the string:")

currentChar=''
currentCount=int(0)
maxChar=''
maxCount=int(0)
previousChar=''

# Loop through each character in a string
for char in inputString:
    currentChar=char
    if currentChar == previousChar:
        currentCount +=1 # Increment the count
        if currentCount > maxCount: # If the current count is higher than the max count
            # Update the result
            maxChar=currentChar
            maxCount=currentCount
    else:
        # Restart the count
        currentCount=1
    # Restart the character
    previousChar=currentChar

if maxCount>1:
    print("The longest consecutive character is "+maxChar+" and the count is "+str(maxCount))
else:
    print("No longest consecutive character because the count of longest consecutive character is 1!")
