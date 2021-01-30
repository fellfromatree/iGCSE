# June 2020 Pre-release Task

# Declare arrays and variables used throughout
days = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
selectedDay = -1
maxHours = [8,2,2,2,2,2,4]
ratePerHour = [2,10,10,10,10,10,3]
discount=False

# Get user input & validate

while(selectedDay==-1):
    parkingOn = input("Which day of the week are you parking? ")
    parkingOn = parkingOn.lower()
    for x in range(len(days)):
        if(days[x]==parkingOn):
            selectedDay=x

entryTime = int(input("What time are you arriving? Enter the hour only "))
while(entryTime<8 or entryTime>23):
    print("The car park is only open 8am until midnight")
    entryTime = int(input("What time are you arriving? Enter the hour only "))

lengthOfStay = int(input("How long are you parking for? "))

if(entryTime<16):
    while(lengthOfStay>maxHours[selectedDay] or lengthOfStay<1):
        print("You've entered an invlid time, you can park for up to",maxHours[selectedDay],"hours on a",days[selectedDay])
        lengthOfStay = int(input("How long are you parking for? "))

else:
    while(lengthOfStay<1 or lengthOfStay>(24-entryTime)):
        print("You've entered an invalid time")
        lengthOfStay = int(input("How long are you parking for? "))

fpn = input("Please enter your frequent parking number if applicable ")
if(len(fpn)!=0):
    while(len(fpn)!=5):
        print("Your frequent parking number must be 5 digits in length")
        fpn = input("Please enter your frequent parking number if applicable ")

    total=0
    multi=5

    for x in range(4):
        total = total+(int(fpn[x])*multi)
        multi -=1

    check = total%11

    if(check==int(fpn[4])):
       discount=True

payment = lengthOfStay*ratePerHour[selectedDay]

if entryTime>=16:
    payment=2

if(discount):
    if(entryTime<16):
        payment = payment*0.9
    else:
        payment = payment*0.5

print("You entered the car park on a",days[selectedDay],"at",entryTime)
print("You will pay $"+str(ratePerHour[selectedDay]),"per hour")
print("Total payment due is $"+str(payment))
