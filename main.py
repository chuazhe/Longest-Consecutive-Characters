inputString=input("Please enter the string:")

currentChar=''
currentCount=int(0)
maxChar=''
maxCount=int(0)
previousChar=''

for char in inputString:
    currentChar=char
    if currentChar == previousChar:
        currentCount +=1
        if currentCount > maxCount:
            maxChar=currentChar
            maxCount=currentCount
    else:
        currentCount=1
    previousChar=currentChar

if currentCount>1:
    print("The longest consecutive character is "+maxChar+" and the count is "+str(maxCount))
else:
    print("No longest consecutive character because the count of longest consecutive character is 1!")
