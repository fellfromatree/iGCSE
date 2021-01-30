# Display the welcome message

print("Welcome to the holiday activity selector")
#print("Choose 1 for a summer activity or 2 for a winter activity")

# Ask the user to enter their choice
# String for text input (this is the default)
# Integer for whole numbers int()
# Float for decimal numbers float()
userInput = int(input("Choose 1 for a summer activity or 2 for a winter activity"))


# Decide which choice the user has made
if(userInput == 1):
    print("You've chosen summer")
    userInput = int(input("Choose 1 for an active activity or 2 for a relaxed activity"))
    if(userInput == 1):
        print("You've chosen an active activity")
    else:
        print("You've chosen a relaxed activity")

else:
    print("You've chosen Winter")
    userInput = int(input("Choose 1 for an active activity or 2 for a relaxed activity"))
    if(userInput == 1):
        print("You've chosen an active activity")
    else:
        print("You've chosen a relaxed activity")

else:
    print("You've chosen winter")
