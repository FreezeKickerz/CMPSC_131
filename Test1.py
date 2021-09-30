x = input("Please enter a character: ")
if type(x)==int:
    if x<=3:
        print("small")
    elif x>=4 & x <=6:
        print("medium")
    elif x>=7 & x<=9:
        print("large")

if ord(x)>= 97 & ord(x)<=122:
    print((ord(x)-96)*x)
elif ord(x)>=65 & ord(x)<=90:
    newInt = ord(x) + 32
    print(chr(70))
else:
    print("Invalid")