# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Nishi Mishra 
# Section: 543
# Assignment: 7b-1
# Date: 12 October 2020

#goal is to take in a name and replace with the rest of rhyme. 
#Check if the first letter is a vowel, then do not take out, 
#instead turn lowercase and add full name

name = input("What is your name? ")

if name[0].lower() in "aeiou": #is first letter a vowel
    short = name.lower()
    print("{X}, {X}, Bo-B{Y}".format(X = name, Y = short))
    print("Banana-Fana Fo-F{Y}\nMe Mi Mo-M{Y}".format(Y = short))
    print("{X}!".format(X = name))
else:
    i = 0
    while name[i] not in "aeiouy": #scott #added a y bc idk how to deal with 'Wyatt'
        i += 1
    short = name[i:] #finds the first index of a vowel 
    
    print("{X}, {X}, Bo-B{Y}".format(X = name, Y = short))
    print("Banana-Fana Fo-F{Y}\nMe Mi Mo-M{Y}".format(Y = short))
    print("{X}!".format(X = name))