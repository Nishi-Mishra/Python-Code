5.6# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 19:42:45 2020

@author: nishi
"""

# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Nishi Rachel Presley 
# Section: 543
# Assignment: 7a-1
# Date: 30 September 2020

##################### Part A #####################

#string_input = '1.00 23.45 345.56 ' #my tester
string_input = input("Enter three or more stock prices separated by spaces: ")
list_of_nums = string_input.split()

#for price in list_of_nums: #this works but I am told I need a list of floats. 
#    price = float (price)  #I have a list of strings 
#    print("$%7.2f" % price)

for i in range(len(list_of_nums)):  
    list_of_nums[i] = float (list_of_nums[i]) #creates the float list
    price = list_of_nums[i] #takes the newly converted float
    print("$%7.2f" % price)


##################### Part B #####################

char_separator = input("\nEnter a two-character separator: ")
#char_separator = "->"

for i in range(len(list_of_nums) - 1):
    print(("%0.2f "+ char_separator + " ") % list_of_nums[i], end = "") #successfully uses the 'end' part of function 
print("%0.2f" % list_of_nums[-1]) #takes care of last term