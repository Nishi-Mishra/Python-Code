# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Nishi Mishra  
# Section: 543
# Assignment: 11b-2
# Date: 10 October 2020

#just make a number guessing game and tell the user too high/low 

#get the input
#see high/low or equal 
#play the game 

from random import randint

secret_number = randint(1,100) 
#print(secret_number)

print("\n -----------------")
print("|| Guessing Game ||")
print(" -----------------\n")
print("Guess the secret number between 1 and 100 (whole numbers only)")

def getInput():
    guess = input("What's your guess? ")
    return int(guess)

def highLow(guess):
    
    if guess > secret_number: 
        return "Too high! Try again."
    elif guess < secret_number:
        return "Too low! Try again."
    else:
        return 1 
    
#print(highLow(secret_number + 1))

def playgame ():
    
    found = False 
    count = 0
    while not found:
        checkResult = highLow(getInput())
        count += 1
        if checkResult != 1:
            print(checkResult)
        else:
            found = True
            
    return "You guessed it!", count


#### Main Code ####
string, count = playgame()
print("\n" + string, "It took", count, "guesses.")



