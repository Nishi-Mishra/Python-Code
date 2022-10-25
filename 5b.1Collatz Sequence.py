# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 23:18:08 2020

@author: nishi
"""

#By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Nishi Mishra
# Section: 543
# Assignment: 5b-1-a
# Date: 26 September 2020

#Collatz sequence is when: if the number is even it is divided by 2; 
#if odd then number is multiplied by 3 and 1 is added 
#the rule says it will eventually reach 1 

#Enter a positive integer to compute the Collatz sequence: 6
#Here is the Collatz sequence starting at 6:
#6, 3, 10, 5, 16, 8, 4, 2, 1
#It took 8 iterations to reach 1

num = int(input("Enter a positive integer to compute the Collatz sequence: "))

Collatz_seq = str(num) 
iterator = 0 

if num <= 0:
    print("Invalid number, must be positive.")
else:
    
    print("Here is the Collatz sequence starting at %d:" % num) 
    
    while num != 1: 
        
        if (num % 2 == 0): # even 
           num /= 2 
           Collatz_seq += ", " + str(int(num))  #why is this a float? ??
        else:
            num = 3 * num + 1 
            Collatz_seq += ", " + str(int(num))
        iterator += 1 
            
print(Collatz_seq) #while asks if num not equal to one therefore it computes 
#and gets answer and prints before breaking out of while 
print("It took %d iterations to reach 1" % iterator) 