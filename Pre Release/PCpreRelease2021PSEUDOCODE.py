# Setup data structures
trips = [9, 11, 13, 15, 10, 12, 14, 16]
upPosition = 0
downPosition = 0
trainCapacity = [480, 480, 480, 480, 480, 480, 480, 480]
income = [0, 0, 0, 0, 0, 0, 0, 0]

# While there is more inputs

# Display the departures board
# Output outbound journeys

# For x = 0 to 3

# Output departure time heading

# If capacity = 0

# Output sold out

# Otherwise

# Output available capacity

# Next loop

# For x = 4 to 7

# Output return time heading

# If capacity = 0

# Output sold out

# Otherwise

# Output available capacity

# Next loop

# Space = false (to check capacity on trains)

# While space != true

# Get number of tickets
# Input number of tickets

# While outwith range 1-80

# Reinput number of tickets

# Get journeys

# Input upPosition

# While upPosition outwith range 0-3

# Reinput upPosition

# Input downPosition

# While downPosition-4 < upPosition OR downPosition over 7

# Reinput downPosition

# Check capacity (loop back to number of tickets)

# If trainCapacity[up]>journeys and trainCapacity[down]>journeys

# Set space to true



# Calculate income
# Free tickets = 0

# Chargable = 0

# Free = journeys DIV 10

# Charge = tix - free

# Cost = charge * 25

# Update data
# Decrement trainCapacity[up]

# Decrement trainCapacity[down]

# Increment income[up]

# Increment income[down]

# End while

# Outputs
# For x = 0 to 3

# Output departure time, capacity and income

# Next loop

# For x = 4 to 7

# Output departure time, capacity and income

# Next loop

# Busiest = 0

# For x= 1 to 7

# If capacity[x]<capacity[Busiest]

# Busiest = x

# End if

# Next loop

# Output busiest train time
