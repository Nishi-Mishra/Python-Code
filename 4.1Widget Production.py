# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 23:43:32 2020

@author: nishi
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Nishi Mishra
# Section: 543
# Assignment: Lab 4b-2
# Date: 12 September 2020

'''
Assume a machine during its initial testing phase produces 10 widgets a day. After 10 days of testing
(starting on day 11), it begins to run at full speed, producing 40 widgets a day. After 50 days at full speed
(days 11-60), it gradually starts becoming less productive, and produces 1 fewer widget per day, (ie. 39
widgets on day 61, etc.) until on day 100 it no longer produces any widgets. 
Write a program named
Lab4b_Act2.py that reads in a day (as a number) from the keyboard and reports the total number of
widgets produced from the initial testing phase up to and including the day entered. For example, entering
3 would report 30 widgets.
'''

'''
First 10 days = 10 widgets per day 
Day 11 to day 60 = 40 widgets per day 
Day 61 till 100 
'''
days = int(input("Please enter a positive value for day: "))
widgets = 0

if(days < 0):
    print("You entered an invalid number!")
else:
    if days >= 100:
        widgets = 2880 #100+2000+800 = 10*10 + 40*50 + 1/2*40*40 
    elif days >= 61:
    #this is a trapezoidal area 1/2 times the amount of widgets produced on 
    #that day + 40 (other base) times the height or difference in days 
        widgets += 1/2 * ((100 - days) + (39)) * (days - 60) #39 bc ... EXPLAIN YO SELF
        widgets += 10*10 + 50*40 
    elif days >= 11:
        widgets += 40 * (days - 10)
        widgets += 10*10
    elif days >= 1:
        widgets += 10 * days 
        
    
    
    print ("The total number of widgets produced on day %d is %d" % (days, widgets))
