userInput = int(input("Enter an upto 5 bit number: "))
digitOne = userInput//10000
digitTwo = (userInput - (digitOne*10000))//1000
digitThree = (userInput - (digitOne*10000 + digitTwo*1000))//100 
digitFour = (userInput - (digitOne*10000 + digitTwo*1000 + digitThree*100))//10
digitFive = (userInput - (digitOne*10000 + digitTwo*1000 + digitThree*100 + digitFour*10))//1

if digitOne <= 1 & digitTwo <= 1 & digitThree <= 1 & digitFour <= 1 & digitFive <= 1:
    if digitOne <= 1 & digitTwo <= 1 & digitThree <= 1 & digitFour <= 1 & digitFive <= 1:
        digitOne = (2**4)*digitOne
        digitTwo = (2**3)*digitTwo
        digitThree = (2**2)*digitThree
        digitFour = (2**1)*digitFour
        digitFive = (2**0)*digitFive
        print(digitOne + digitTwo + digitThree + digitFour + digitFive)
    else: 
        print("Over 5 digits") 
elif userInput//100000 > 0:
    print("Over 5 digits")
else: 
    print("Not a valid binary number")