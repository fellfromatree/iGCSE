import time

# Setup data structures
trips = ["9:00", "11:00", "13:00", "15:00", "10:00", "12:00", "14:00", "16:00"]
upPosition = 0
downPosition = 0
trainCapacity = [480, 480, 480, 480, 480, 480, 480, 640]
income = [0, 0, 0, 0, 0, 0, 0, 0]
sold = [0, 0, 0, 0, 0, 0, 0, 0]
ticketChoice = 1 # 1 means they want to buy more tickets, 2 means they don't

print("Welcome to the mountain railway ticket office")
# While there is more inputs
while(ticketChoice == 1):

# Display the departures board
# Output outbound journeys
    print("\nJourneys up the mountain")
# For x = 0 to 3
    for x in range(4):
# Output departure time heading
# If capacity = 0
        if(trainCapacity[x]==0):
# Output sold out
            print("Train",x+1,"Departs",trips[x],"closed")
# Otherwise
        else:
# Output available capacity
            print("Train",x+1,"Departs",trips[x],"seats available",trainCapacity[x])
            
# Next loop
    print("\nJourneys down the mountain")
# For x = 4 to 7
    for x in range(4,8):
# Output return time heading
# If capacity = 0
        if(trainCapacity[x]==0):
# Output sold out
            print("Train",x+1,"Departs",trips[x],"closed")
# Otherwise
        else:
# Output available capacity
            print("Train",x+1,"Departs",trips[x],"seats available",trainCapacity[x])
# Next loop


# Space = false (to check capacity on trains)
    space = False

# While space != true
    while(space != True):
# Get number of tickets
# Input number of tickets
        tix = int(input("How many tickets do you want to purchase?"))
# While outwith range 1-80
        while(tix<1 or tix>80):
# Reinput number of tickets
            tix = int(input("How many tickets do you want to purchase?\nYou can only buy 1-80 tickets"))
            
# Get journeys
# Input upPosition
        upPosition = int(input("Please choose your outbound journey, 1-4"))
# While upPosition outwith range 0-3
        while(upPosition<1 or upPosition>4):
# Reinput upPosition
            upPosition = int(input("Please choose your outbound journey, 1-4"))
        
# Input downPosition
        downPosition = int(input("Please choose your return journey, 5-8"))
# While downPosition-4 < upPosition OR downPosition over 7
        while(downPosition-4<upPosition or downPosition>8):
# Reinput downPosition
            print("Your return train must be later than your outbound train")
            downPosition = int(input("Please choose your return journey, 5-8"))
            
# Adjust positions for indexing from 0
        upPosition = upPosition-1
        downPosition = downPosition-1
        
# Check capacity (loop back to number of tickets)         
# If trainCapacity[up]>journeys and trainCapacity[down]>journeys
        if(trainCapacity[upPosition]>tix and trainCapacity[downPosition]>tix):
# Set space to true
            space=True
            
# Calculate income
# Free tickets = 0
    free = 0
# Chargable = 0
    chargable = 0
# Free = journeys DIV 10
    free = tix // 10
# Charge = tix - free
    charge = tix-free
# Cost = charge * 25
    cost = charge*25
    
# Update data
# Decrement trainCapacity[up]
    trainCapacity[upPosition] = trainCapacity[upPosition]-tix
# Decrement trainCapacity[down]
    trainCapacity[downPosition] = trainCapacity[downPosition]-tix
# Increment tickers sold [up]
    sold[upPosition] = sold[upPosition]+tix
# Decrement tickers sold [down]
    sold[downPosition] = sold[downPosition]+tix
# Increment income[up]
    income[upPosition] = income[upPosition]+cost
# Increment income[down]
    income[downPosition] = income[downPosition]+cost

    print("Seats purchased",tix)
    print("Seats charged",charge)
    print("Total cost",cost*2)
    time.sleep(2)
# End while
    ticketChoice = int(input("Do you need to buy more tickets? Enter 1 for yes, 2 for no"))
    while(ticketChoice<1 or ticketChoice>2):
        ticketChoice = int(input("Do you need to buy more tickets? Enter 1 for yes, 2 for no"))
    
# Outputs
print("\nDaily sales totals\n")
# For x = 0 to 3
for x in range(4):
# Output departure time, capacity and income
    print("Departs",trips[x],"tickets sold",sold[x],"seats. Total income",income[x])
# Next loop

# For x = 4 to 7
for x in range(4,8):
# Output departure time, capacity and income
    print("Departs",trips[x],"tickets sold",sold[x],"seats. Total income",income[x])

# Next loop

# Calculate total passengers and income
# Initialise totals
totalIncome = 0
totalPassengers = 0

# For x = 0 to 7
for x in range(8):
    # Total up income
    totalIncome = totalIncome + income[x]

    # Total up passengers
    totalPassengers = totalPassengers + sold[x]

# Output totals
print("Total income today:", totalIncome)
print("Total passengers today:", totalPassengers)

# Calculate busiest train
# Busiest = 0
busiest = 0
# For x = 0 to 7
for x in range(8):
# If capacity[x]<capacity[Busiest]
    if(sold[x]>sold[busiest]):
# Busiest = x
        busiest=x
# End if
# Next loop

# Output busiest train time
print("\nThe busiest departure today was",trips[busiest])
