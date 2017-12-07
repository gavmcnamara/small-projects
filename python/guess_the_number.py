import random

random_number = random.randint(1, 10)
print("Random number has been generated")
guessed = False

while guessed == False:
    user_input = int(input("Guess number from 1-10: "))
    if user_input == random_number:
        print("well done")
        break
    elif user_input > random_number:
        print("too high, guess again: ")
    elif user_input < random_number:
        print("Too low, guess again: ")

print("End of program")