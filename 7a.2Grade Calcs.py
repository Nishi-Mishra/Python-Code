# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 20:21:23 2020

@author: nishi
"""

# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Nishi Rachel Presley 
# Section: 543
# Assignment: 7a-2
# Date: 30 September 2020

from math import * 

gradeData=[69,99,73,59,67,65,52,99,57,58,67,88,72,69,41,74,53,90,63,66,92,54,61,59,48,71,83,89,100,69,66,39,48,41,99,68,52,78,77,73,40,65,77,87,96,44,54,60,89,72]

####################### Part A #######################

#find grade average
sum_grades = 0
grade_count = 0
for grade in gradeData:
    sum_grades += grade
    grade_count += 1

mean = sum_grades / grade_count 
print("The mean is %0.2f" % mean)

####################### Part B #######################
#find standard deviation https://www.mathsisfun.com/data/standard-deviation-formulas.html

# do grade minus avg and square it 
# add all the squares together
# divide by the num of grades
# sqrt the lot of it and yay? 

sum_squares = 0

for grade in gradeData:
    sum_squares += (grade - mean) ** 2 

standard_deviation = sqrt(sum_squares / grade_count) #does the equation 

print("The standard deviation is %0.4f" % standard_deviation)

####################### Part C #######################

#find min/max grades

min_grade = gradeData[0] #initialized with the first terms equal to both min and max
max_grade = gradeData[0]

for grade in gradeData: #finds both min and max in the same loop bc efficiency 
    
    if grade < min_grade:
        min_grade = grade
    elif grade > max_grade:
        max_grade = grade
    
print("The min is %d" % min_grade)
print("The max is %d" % max_grade)
