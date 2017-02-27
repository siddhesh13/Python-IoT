sortedList=[12,14,18,25,35,67,98,123,145,167,189]
temporaryList=sortedList

print ("Please Enter the number to search for")
a=int(input())

while(1):
    listLength=len(temporaryList)
    if(listLength==2): # If the List is so small to have only two Element
        #print("Exit Condition")
        if(temporaryList[0]==a or temporaryList[1]==a):
            print("Number Found in List")
        else:
            print("Number Not Found in List")
            
        break # exit the while Loop
    
    if(listLength%2==0): #List has Even number of Elements
        middleIndex=int((listLength/2)+1)
    else:#List has Odd number of Elements
        middleIndex=int((listLength+1)/2)

    if (temporaryList[middleIndex]==a): #compare the Middle Value to User Entered Number
        print("Number Exists in List")
        break # We found Our Number, lets Exit

    
    # The searched Value is less than the Middle Value in the List, so the number probably exists in the lower half.
    if(temporaryList[middleIndex] > a):
        temporaryList=temporaryList[:middleIndex] # Modify the Temporary List to have values from the Lower Half
    else:
        temporaryList=temporaryList[middleIndex:] # Modify the Temporary List to have values from the Upper Half
    
        
    
    
