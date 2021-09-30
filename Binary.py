userInput = int(input("Enter an upto 5 bit number: "))
if userInput<= 11111:
    digitOne = userInput//10000
    digitTwo = (userInput - (digitOne*10000))//1000
    digitThree = (userInput - (digitOne*10000 + digitTwo*1000))//100 
    digitFour = (userInput - (digitOne*10000 + digitTwo*1000 + digitThree*100))//10
    digitFive = (userInput - (digitOne*10000 + digitTwo*1000 + digitThree*100 + digitFour*10))//1
else: 
    print("Over 5 digits") 
if digitOne <= 1 & digitTwo <= 1 & digitThree <= 1 & digitFour <= 1 & digitFive <= 1:
    print(2**4(digitOne), 2**3(digitTwo), 2**2(digitThree), 2**1(digitFour), 2**0(digitFive))
else: 
    print("Not a valid binary number")