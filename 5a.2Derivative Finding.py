# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 10:57:47 2020

@author: nishi
"""

# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Nishi Mishra
#        Presley Smith
#        Rachel Spacek  
# Section: 543
# Assignment: 5a-2
# Date: 25 September 2020

########################## Part A ########################

a = float(input("Enter the coefficient A: "))
b = float(input("Enter the coefficient B: "))
c = float(input("Enter the coefficient C: "))
d = float(input("Enter the coefficient D: "))

x = float(input("Enter a value for x: "))

def findValFunc (val,a,b,c,d): #gets an upper bound or lower bound in val; and coefficients a,b,c,d and returns value of f(val)
  
  #𝑓(𝑥) = 𝐴𝑥^3 + 𝐵𝑥^2 + 𝐶𝑥 + D 
  ans = a*(val)**3 + b*(val)**2 + c*(val) + d 

  return ans

val_at_x = findValFunc(x,a,b,c,d) #f(x) = 3x^2 --> f'(x) = 3*2*(x)^2

print("f(%.1f) is " % (x) + str(val_at_x))

########################## Part B ########################

derivative_x = 3 * a * x ** 2 + 2 * b * x + c
print("f'(%0.1f) analytically is " % (x) + str(derivative_x) )

########################## Part C ########################

A = 0.1 #variable on denominator of definition of derivative (limit) NOT coefficient 
TOL = 10**(-6)

ans1 = (findValFunc(x+A,a,b,c,d) - findValFunc(x,a,b,c,d)) / A 
A = A/2
ans2 = (findValFunc(x+A,a,b,c,d) - findValFunc(x,a,b,c,d)) / A 

while (abs(ans1 - ans2) > TOL):

  ans1 = ans2 #ans1 has old value 
  A = A / 2
  ans2 = (findValFunc(x+A,a,b,c,d) - findValFunc(x,a,b,c,d)) / A #ans2 is the new value

print("f'(%0.1f) numerically is %f" % (x,ans2))


A = 0.1
ans1 = (findValFunc(x,a,b,c,d) - findValFunc(x-A,a,b,c,d)) / A 
A = A/2
ans2 = (findValFunc(x,a,b,c,d) - findValFunc(x-A,a,b,c,d)) / A 

while (abs(ans1 - ans2) > TOL):

  ans1 = ans2 #ans1 has old value 
  A = A / 2
  ans2 = (findValFunc(x,a,b,c,d) - findValFunc(x-A,a,b,c,d)) / A #ans2 is the new value

print("f'(%0.1f) numerically is %f" % (x,ans2))


A = 0.1
ans1 = (findValFunc(x+A,a,b,c,d) - findValFunc(x-A,a,b,c,d)) / (2*A) 
A = A/2
ans2 = (findValFunc(x+A,a,b,c,d) - findValFunc(x-A,a,b,c,d)) / (2*A) 

while (abs(ans1 - ans2) > TOL):

  ans1 = ans2 #ans1 has old value 
  A = A / 2
  ans2 = (findValFunc(x+A,a,b,c,d) - findValFunc(x-A,a,b,c,d)) / (2*A) #ans2 is the new value

print("f'(%0.1f) numerically is %f" % (x,ans2))

