# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 18:41:22 2020

@author: nishi
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Nishi Mishra
# Section: 543
# Assignment: Lab 3b-2
# Date: 12 September 2020

from math import * 

#find the angle in degrees from the point of a random observer. Imagine a 
#frisbee doing a rebound from point a to b and observer is curious what 
#angle did it sweep through

#1st take two points and observer 

A_x = int( input ("Enter the x position of the observer: "))
A_y = int( input ("Enter the y position of the observer: "))
A_z = int( input ("Enter the z position of the observer: "))
B_x = int( input ("Enter the x position of point 1: "))
B_y = int( input ("Enter the y position of point 1: "))
B_z = int( input ("Enter the z position of point 1: "))
C_x = int( input ("Enter the x position of point 2: "))
C_y = int( input ("Enter the y position of point 2: "))
C_z = int( input ("Enter the z position of point 2: "))

#2nd find vectors AB and AC with A as the observer 

vector_AB_x = B_x - A_x 
vector_AB_y = B_y - A_y
vector_AB_z = B_z - A_z  

vector_AC_x = C_x - A_x 
vector_AC_y = C_y - A_y
vector_AC_z = C_z - A_z

#3rd find the unit vectors for each 

AB_mag = sqrt(vector_AB_x**2 + vector_AB_y**2 + vector_AB_z**2)
AC_mag = sqrt(vector_AC_x**2 + vector_AC_y**2 + vector_AC_z**2)

unit_vector_AB_x = vector_AB_x / AB_mag 
unit_vector_AB_y = vector_AB_y / AB_mag 
unit_vector_AB_z = vector_AB_z / AB_mag   

unit_vector_AC_x = vector_AC_x / AC_mag 
unit_vector_AC_y = vector_AC_y / AC_mag 
unit_vector_AC_z = vector_AC_z / AC_mag

#4th dot product and cos inverse to get angle/convert to degrees 

dot_product = unit_vector_AB_x * unit_vector_AC_x + unit_vector_AB_y * unit_vector_AC_y + unit_vector_AB_z * unit_vector_AC_z   

ans_degrees = degrees(acos(dot_product)) #finall returns degrees between the two vectors AB & AC

print("\nObserver location is x= %d y= %d z= %d" % (A_x, A_y, A_z))
print(" Point 1 location is x= %d y= %d z= %d" % (B_x, B_y, B_z))
print(" Point 2 location is x= %d y= %d z= %d" % (C_x, C_y, C_z))
print("\nThe angle between the points is% 0.3f degrees" % ans_degrees)