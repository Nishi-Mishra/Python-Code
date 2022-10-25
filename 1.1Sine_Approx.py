# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 10:02:16 2020

@author: nishi
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Nishi Mishra
# Section: 543
# Assignment: Lab 1b-3
# Date: 20 August 2020



import math

# find the value of sin(x)/x as an approximation as x goes to zero

def sinApprox ():
    print("This shows the evaluation of sin(x)/x evaluated close to x=0")
    print("My guess is 1")
    
    x = 1
    
    for i in range(8):
        
        ans = math.sin(x)/x
        print(ans)
        x=x/10
        
    print("\nMy guess was dead on perfect (used L'Hop)")
        
        
sinApprox()