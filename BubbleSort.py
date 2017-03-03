#Python Program to Demonstrate Bubble Sort Algorithm

unorderedlist=[1,300,2,50,20,2,3,3, 5,8,60,2,-12, 0] # Initalise the List to be sorted
listlength=len(unorderedlist) # How many elements exist in this list?

for i in range(0,listlength): # Start a For Loop to execute "listlength" number of times
    print(unorderedlist) # print the List contents here 
    for i in range(0,listlength-1): # Start Looping through each of the List Elements
            # if current element ( at i index) greater than the next element ( at i+1 index)
            # then swap, else dont do anything.
        if(unorderedlist[i]>unorderedlist[i+1]): 
                                                 
            a=unorderedlist[i+1] # assign the next element to a temporary variable
            unorderedlist[i+1]=unorderedlist[i] #Make the Swap
            unorderedlist[i]=a #set current Element to value saved in temporary variable. 

                  





