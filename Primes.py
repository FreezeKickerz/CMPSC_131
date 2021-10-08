userInput = int(input("Please Enter n: "))

higherPrimes = []
lowerPrimes =[]
counter = userInput

i = 0
while i < 5:
# Find 5 Lower Primes
    counter+=1
    for j in range(2, counter):
        if counter % j == 0:
            break
    else: 
        higherPrimes.append(counter)
        i+=1
# End Code for Higher Primes
counter=userInput
p = 0
while p < 5:
    counter-=1
    for j in range(2,counter):
        if counter % j == 0:
            break
    else:
        lowerPrimes.append(counter)
        p+=1
    if counter <= 2:
        break
print("Larger primes: ", higherPrimes[0],higherPrimes[1],higherPrimes[2],higherPrimes[3],higherPrimes[4])
print("Smaller primes: ", lowerPrimes[0],lowerPrimes[1],lowerPrimes[2],lowerPrimes[3],lowerPrimes[4])