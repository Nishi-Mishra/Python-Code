# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 00:20:13 2020

@author: nishi
"""

#By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Nishi Mishra
# Section: 543
# Assignment: 5b-2
# Date: 27 September 2020

#find the Golden ratio: Fn+1 / Fn 
#each Fibonacci number is the sum of the previous two numbers 

# 0 1 1 2 3 5 etc 

term_count = int(input("Please enter an integer: "))

num1 = 0
num2 = 1 
 
print("The first %d estimates of the Golden ratio are:" % term_count)

num3 = num1 + num2 # 1 

num1 = num2 #order of assignment is important 1
num2 = num3 # 1

golden_ratio = num2 / num1 
golden_termlist = "%0.3f" % golden_ratio


while term_count-1 > 0:
    
    num3 = num1 + num2 # 1 

    num1 = num2 #order of assignment is important 1
    num2 = num3 # 1
    
    golden_ratio = num2 / num1 
    golden_termlist += ", %0.3f" % golden_ratio 
    
    term_count -= 1 
    
print(golden_termlist)