# By submitting this assignment, I agree to the following:
#     "Aggies do not lie, cheat, or steal, or tolerate those who do."
#     "I have not given or received any unauthorized aid on this assignment."
#
# Names:          Lindsey Wilkin 
#                 Charlie Simpson 
#                 Nishi Mishra
#                 Kai Brown
# Section:        543
# Assignment:     Lab 12a-2
# Date:           05 11 2020

# import the proper packages for computation
import numpy as np

# output the polynomial options to  the user
print('Which polynomial would you like to test?')
print('1: x^3 + 1')
print('2: 3x^3 + 2x^2 - 6x + 5')
print('3: 2x^3 - x^2 + 3x - 2')
user_num = int(input('Enter the number: '))

lowerbound = float(input('\nEnter the lower value for the interval: '))
upperbound = float(input('Enter the upper value for the interval: '))

# define the functions for the equations
def func1(x):
  return x**3 + 1

def func2(x):
  return 3*x**3 + 2*x**2 - 6*x + 5

def func3(x):
  return 2*x**3 - x**2 + 3*x - 2


#lowerbound, upperbound = 10, 20 #test values 
def findAreaConvergence(func, intervals):

  x = np.linspace(lowerbound, upperbound, intervals)
  dx = x[1] - x[0]

  # calculate with left intervals
  left_area = 0
  for i in range(len(x)-1):
    left_area += dx * func(x[i])

  # calculate with right intervals
  right_area = 0
  for i in range(1,len(x)):
    right_area += dx * func(x[i])
  
  # calculated with midpoint
  midpoint_area = 0
  for i in range(len(x)- 1):
    midpoint_area += dx * func((x[i] + x[i+1]) / 2)

  # calculate with trapazoid
  trap_area = 0
  for i in range(len(x) - 1):
    trap_area += dx * ((func(x[i]) + func(x[i+1])) * (1/2))
  
  # return the functions
  return left_area, right_area, midpoint_area, trap_area


# use if statements to set the equations equal to the variable func for calculations
if user_num == 1:
  func = func1
elif user_num == 2:
  func = func2
elif user_num == 3:
  func = func3

# define the tolerance  
TOL = 0.000001
# set the interval for computing tolerance
numIntervals = 10
left_area, right_area, midpoint_area, trap_area = findAreaConvergence(func, numIntervals)
found = False 

# create a while loop to go through the functions until the tolerance is met
while TOL < abs(findAreaConvergence(func, numIntervals)[0] - findAreaConvergence(func, numIntervals+1)[0]): 
    numIntervals += 10


left_area, right_area, midpoint_area, trap_area = findAreaConvergence(func, numIntervals)
  
# output the values
print('\nShape 1 area: %.3f' % left_area)
print('Shape 2 area: %.3f' % right_area)
print('Shape 3 area: %.3f' % midpoint_area)
print('Shape 4 area: %.3f' % trap_area)