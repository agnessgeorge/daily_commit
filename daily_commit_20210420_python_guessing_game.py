# Guessing Game Challenge
# Version 1
from random import randint

x = randint(1, 101)

print "Welcome to my guessing game! \n" \
      "The game will generate a random number between 1 and 100 and you have to guess it correctly to win!\n" \
      "If your guess is close enough you'll get an alert 'WARM!' or 'WARMER!'\n" \
      "If your guess if too far you'll get an alert 'COLD! or 'COLDER!'\n"

y = int(raw_input("Enter your guess: "))

guesses = 0
guess_list = []

# first turn
if y != x:
    guess_list.append(y)
    guesses += 1
    z = abs(y - x)
    if y < 1 or y > 100:
        print "OUT OF BOUNDS!"
    elif z < 10:
        print "WARM"
    elif z >= 10:
        print "COLD!"
    y = int(raw_input("Enter your guess: "))

# subsequent turns
while y != x:
    guess_list.append(y)
    guesses += 1
    z = abs(y - x)

    if y < 1 or y > 100:
        print "OUT OF BOUNDS!"
    elif z < 10 and abs(x - guess_list[-2] > z):
        print "WARMER!"
    elif z >= 10 and z > abs(x - guess_list[-2]):
        print "COLDER!"

    y = int(raw_input("Enter your guess: "))

else:
    guesses += 1
    print("You guessed correctly after %d guesses" % guesses)
    print guess_list
