import random # Import random for randint function

def dice(n): # n is the amount of dice the user chooses
    rolls = [] # Creates array to store number of dice
    for i in range(n): # for the individual number of dice
        rolling = random.randint(1, 6) # takes randint and pick a random number between 1 and 6
        rolls.append(rolling) # takes rolling and stores in rolls array
    return rolls # returns array rolls out of for loop

print(dice(input("How Many Dice Will You Roll? ")))
# takes user input and will return random number for each dye

