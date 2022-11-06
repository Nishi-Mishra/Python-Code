# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:17:45 2020

@author: nishi
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Nishi Mishra 
# Section: 543
# Assignment: 7b-3
# Date: 12 OCtober 2020

#sort values via the min() function, get value and add it to new list
#delete the value you just found 
#keep going until original list is empty 

input_list = input("Enter a list of values: ")  

orign_list = list(map(float, input_list.split())) #explained in act 2
#basically casts each value of split_list as a float and creates a list

####### Sorted List Part A #######

sorted_list = []

while len(orign_list) != 0: #haven't ever used this method, 
#usually it is a whole mess of moving elements around until the entire thing is sorted..a bunch more difficult
#or even worse it is a whole comparison thing of bisecting the array and finding max/mins   
    min_val = min(orign_list)
    sorted_list.append(min_val)
    orign_list.remove(min_val)
    
#print(sorted_list)

####### Median Part B #######

if len(sorted_list) % 2 == 1:
    median_ind = len(sorted_list) // 2 #if len = 5  5//2 = 2 plus 1 is 3 which is the middle val #however value 3 is index 2
    median = sorted_list[median_ind]
else:
    high_ind = len(sorted_list) // 2 #if len = 4   4/2 = 2 & so the two nums to avg are @ 2 & 3 #however 2 is index 1 & 2
    low_ind = high_ind - 1 
    median = (sorted_list[low_ind] + sorted_list[high_ind]) / 2
    
####### Print Statements #######

print("The minimum value is %.1f" % sorted_list[0])
print("The maximum value is %.1f" % sorted_list[-1])
print("The median is %.1f" % median)
