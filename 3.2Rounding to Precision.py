# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 19:59:30 2020

@author: nishi
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Nishi Mishra
# Section: 543
# Assignment: Lab 3b-challenge
# Date: 12 September 2020

'''
Using only the commands we have covered in class so far, write a program that asks a user for a number
of digits of precision, and prints the value 2/7 rounded to that many digits of precision. 
'''

#sorry the variable names could have been better, I just can't think of better names right now 

digits = int(input("Please enter the number of digits of precision for 2/7: "))
ans2_7 = 2/7
 
first_num = int(2 // 7) #if the numbers were 7/2 then this would matter 
mult = (ans2_7 - first_num) * 10**digits # 28571.42857 gets num digits by multiplying to move decimals; 
#ans - first num is bc if it was 3.5 it would be 3.5 - 3 = 0.5 to only get the decimal part then move the decimal after 

digits_after = int(mult + 0.5) #this forces mult to become an int to get digits after 
#the plus 0.5 is so 4.1 will be 4.6 which will be int(4.6) = 4 & 4.5 will be 5.0 which will be int(5.0) = 5 
#basically the plus 0.5 takes care of rounding without an if statement 

'''
left = mult - (digits_after) # 0.42857 this is decimal after the number of digits we want 

if left >= 0.5: #sees if the last digit needs rounding  #commented out bc 'if' isn't allowed 
    digits_after+=1
'''

print("The value of 2/7 to " + str(digits) +" digits is: " + str(first_num) + "." + str(digits_after)) #this pieces the answer together in terms of strings 

#print("The value of 2/7 to 5 digits is: %0.5f" % ans2_7) #this was to compare with the 'real answer'