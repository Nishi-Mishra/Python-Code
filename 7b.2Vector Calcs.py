# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 08:46:26 2020

@author: nishi
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Nishi Mishra 
# Section: 543
# Assignment: 7b-2
# Date: 12 OCtober 2020

from math import *

vectorA_input = input("Enter the elements for vector A: ")
vectorB_input = input("Enter the elements for vector B: ")

#this was from zybooks 
#this is splitting the list and then casting each element in the list as a float
#this is what the map() function does
#then the map needs to put the results somewhere so I cast it as a list because idk how to work with a map 

vectorA = list(map(float,vectorA_input.split())) #explained above ^
vectorB = list(map(float,vectorB_input.split())) 

#### Magnitude ####
magA = 0
magB = 0

for value in vectorA:
    magA += value**2
magA = sqrt(magA)

for value in vectorB:
    magB += value**2
magB = sqrt(magB)

#### A + B ####
sumVector = []
for ind in range(len(vectorA)): #we hope both vector A & B have the same amount of dimensions 
    sumVector.append(vectorA[ind] + vectorB[ind])

#### A - B ####
subVector = []
for ind in range(len(vectorA)):
    subVector.append(vectorA[ind] - vectorB[ind])

#### A * B ####
dot_product = 0 
for ind in range(len(vectorA)):
    dot_product += vectorA[ind] * vectorB[ind]

#### Print Statements ####
print("The magnitude of vector A is %.5f" % magA)
print("The magnitude of vector B is %.5f" % magB)
print("A + B is {}".format(sumVector))
print("A - B is {}".format(subVector))
print("The dot product is " + str(dot_product))
