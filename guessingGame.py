import random
number = random.randint(1,10)
guess = int(input("Guess a number from 1 to 10: "))
while number != "guess":
    print
    if guess < number:
        print ("guess higher")
        guess = int(input("Guess a number from 1 to 10: "))
    elif guess > number:
        print ("guess lower")
        guess = int(input("Guess a number from 1 to 10: "))
    else:
        print ("you guessed the number!")
        break
    print
        