bookList = open("booklist-1.txt","r")
books = bookList.read().split("\n")
bookList.close()

#BookList Variables
bookName = []
bookCopies = []
bookRestrictions = []
totalDaysBorrowed = []
daysFree = []

# Format <book name>#<number of copies>#<restricted>
for x in books:
    line = x.split("#")
    restrictions = 0
    bookName.append(line[0])
    bookCopies.append(int(line[1]))
    if line[2] == "TRUE":
        restrictions = 1
    bookRestrictions.append(restrictions)
    totalDaysBorrowed.append(0)
    
print(bookName)
print(bookCopies)
print(bookRestrictions)

# Library Log Variables

#Name:NameOfBook:
#DaysOverdue[0]DayTakenOut[1]DaysBorrowedFor[2]Returned[3]
personInfo = {}

#Name:Amount of Books out[0]Fines[1]
personBlacklist = {}

libraryLog = open("librarylog-2.txt","r")
log = libraryLog.read().split("\n")[:-1]
libraryLog.close()

#Running Library Log
for x in log:
    line = x.split("#")
    if line[2] not in personInfo and line[0] != "A":
        personInfo[line[2]] = {}
        personBlacklist[line[2]] = [0,0]
    
    #Borrow Function
    if line[0] == "B":     
        if line[3] not in personInfo[line[2]]:
            personInfo[line[2]][line[3]] = [0,int(line[1]),int(line[4]),0]
       
        personInfo[line[2]][line[3]][1] = int(line[1])
        personInfo[line[2]][line[3]][2] = int(line[4])
        personInfo[line[2]][line[3]][3] = 0
        personBlacklist[line[2]][0]+= 1

    #Return Function
    if line[0] == "R":
        bookPosition = bookName.index(line[3])
        bookCopies[bookPosition] += 1
        personInfo[line[2]][line[3]][3] = 1
        personBlacklist[line[2]][0] -=1
        
        days_borrowed = int(line[1]) - personInfo[line[2]][line[3]][1]
        totalDaysBorrowed[bookPosition] += days_borrowed
        
        #Fine Calculations
        if days_borrowed > int(personInfo[line[2]][line[3]][2]):
            sum = days_borrowed - int(personInfo[line[2]][line[3]][2])
            personInfo[line[2]][line[3]][0] += sum
            personBlacklist[line[2]][1] = sum*(1+(4*bookRestrictions[bookPosition]))

    #Paying Fine Calculation
    if line[0] == "P":
        personBlacklist[line[2]][1] -= int(line[3])

    #Adding Book Function
    if line[0] == "A":
        if line[2] not in bookName:
            bookName.append(line[2])
            bookCopies.append(1)
            bookRestrictions.append(0)
        else:
            bookPosition = bookName.index(line[2])
            bookCopies[bookPosition] += 1
    totalDaysBorrowed.append(0)

print(personBlacklist)
print(personInfo)












