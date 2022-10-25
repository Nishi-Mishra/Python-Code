# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 00:02:32 2020

@author: nishi
"""

#By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Nishi Mishra
# Section: 543
# Assignment: 5b-1-c
# Date: 26 September 2020

#find and say if the number is prime or not; count them up between 2 & 100 

primeCount = 0 

def isPrime (num):
    
    if (num == 2 or num == 3 or num == 5 or num == 7):
        return True
    
    if (num % 2 == 0):#this makes sure 
        return False
    elif (num % 3 == 0):
        return False
    elif (num % 5 == 0):
        return False
    elif (num % 7 == 0): 
        return False
    #I stopped at 7 bc 11 * 9 = 99; which is the max 11 can go and that is covered by 3 
    return True 

for x in range (2, 101):
    if (isPrime(x)):
        print("%d is prime" % x)
        primeCount += 1 
    else: 
        print("%d is not prime" % x) 

print("There are %d prime numbers between 2 and 100" % primeCount)