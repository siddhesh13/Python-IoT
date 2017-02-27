primeList=[2] # We need a starting seed number for the primeList
print ("Enter a Number: ") # Ask the User for a number till which he/she requires primes.
rangeMax=int(input()) # accept input, convert to int
for testNumber in range (3,rangeMax): # start a for Loop, from 3  to rangeMax
    isPrime=True #assume the number is prime
    print(primeList)# print the primelist Progress
    # traverse through the primelist, test the number i against all numbers in the primeList   
    for prime in primeList: 
        if testNumber%prime==0: # test divisibility, % is notation for Modulo, operation returns remainder after division.
            isPrime=False # since the remainder is zero, the current number in primeList divides i fully. 
            print(str(testNumber) + " is divisible by " +str(prime))
            break # we dont need to test for any other number. Loop ends here abruptly
#--------------------
#        The Loop ends here, Was our assumption of the number being prime correct? If yes, the variable
#        isPrime will continue to stay True


        
    if isPrime==True: # Hurray, we found another prime, lets add it to our primeList
        primeList.append(testNumber)

# All numbers from 3 to a have been tested, our PrimeList array would be filled, Lets print it


print("Numbers which are prime till " +str(rangeMax) +" are")
print(primeList)        
        
        
        

