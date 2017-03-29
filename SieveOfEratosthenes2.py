primeList=[]
print("Enter a Number")
n=input()
n=int(n)
for index in range (0, n+1):
    primeList.append(index)

for index in range ( 2, n+1):
    for factors in range( index*2, n, index):
        primeList[factors]=0
    #print(primeList)

while 0 in primeList:
    primeList.remove(0)

print("The primes till " + str(n) + " are:")   
print(primeList)
    
