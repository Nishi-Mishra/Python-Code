# By submitting this assignment, I agree to the following:
#     "Aggies do not lie, cheat, or steal, or tolerate those who do."
#     "I have not given or received any unauthorized aid on this assignment."
#
# Names:          Lindsey Wilkin 
#                 Charlie Simpson 
#                 Nishi Mishra
#                 Kai Brown
# Section:        543
# Assignment:     Lab 12a-1
# Date:           05 11 2020

#user enters a bunch of coefficients in descending order
#get the 1st and second derivative expressions 
#use numpy and pyplot to plot the lines -- look at the previous labs 
#find local max and min by looping through points 
#graph with different colors so people can see 

import numpy as np
import matplotlib.pyplot as plt 

#need to create an input statement and add docstrings everywhere!! 
user_entry = str(input("Enter a list of coefficents separated by a space: ")) #2 3 -11 -6

coeff_list = list(map(int, user_entry.split())) #makes the input from a string into a list of ints

#need to get 5x^4 + 7x^3 + 3x^2 + 4x + 2  -- works 

def getFunction(x, coeff_list):
    '''This function takes in x-values and the coefficents entered by user and returns the y-values of the function'''
    #get the function!! 
    eq = 0
    for i in range(len(coeff_list) -1): 
        eq += coeff_list[i]* x ** (len(coeff_list) - i - 1)
    eq += (coeff_list[-1])
    
    return eq 


def getDerivative(x, coeff_list): 
    '''This takes in x-value np array and coefficient list and returns the function's derivative y-values'''
    #deriv2 function has been removed and this function now returns a coefficient list of the derivative 
    eq = 0
    new_coeff_list = []
    for i in range(len(coeff_list) -1): 
        eq += coeff_list[i] * (len(coeff_list) - i - 1) * x ** (len(coeff_list) - i - 1 - 1)
        new_coeff_list += [coeff_list[i] * (len(coeff_list) - i - 1)]
    
    return eq, new_coeff_list 


def getCriticalvalues(x, eq): #takes in eq which is a list of float y-values (regular function); dxeq is the derivative y-vals 
    ''' This takes in  x-value list and y-value list of function and returns the max and min via a three point comparison'''
    #max/min and derivative = 0 
    ValsX = []
    ValsY = []
    for i in range(1,len(eq)-1):
        if eq[i] > eq[i-1] and eq[i] > eq[i+1]: #this is a max
            ValsX.append(x[i])
            ValsY.append(eq[i]) 
        elif eq[i] < eq[i-1] and eq[i] < eq[i+1]: #this is a min 
            ValsX.append(x[i])
            ValsY.append(eq[i])  
    
    return(ValsX, ValsY) 

def getMax_Mins(x, eq, dxeq):#this one is the black points 
    ''' This takes in  x-value list and y-value list of function and returns the max and min via derivatives'''
    crit_Xs = []
    crit_Ys = []
    for i in range(len(eq)-1):
        if dxeq[i] > 0 and dxeq[i+1] < 0: # /\ 
            crit_Xs += [x[i]]
            crit_Ys += [eq[i]]
        elif dxeq[i] < 0 and dxeq[i+1] > 0: # \/ 
            crit_Xs += [x[i]]
            crit_Ys += [eq[i]]
    
    return crit_Xs, crit_Ys


x = np.linspace(-5,5,100) 

#this will get the derivative!!  #implement this for the derivative function! 

func_Ys = getFunction(x, coeff_list)

''' #this block can be used for the extra credit? 
#this will get the derivative!!  #implement this for the derivative function! 
dx = x[1]-x[0] 
y = func_Ys
dydx = np.gradient(y, dx) #what does this function do?? 
'''

#all these function calls return tuples and I am unpackaging them via double assignments 
deriv_Ys, deriv_coeffs = getDerivative(x, coeff_list)
deriv2_Ys, deriv2_coeffs = getDerivative(x, deriv_coeffs)
deriv3_Ys, deriv3_coeffs = getDerivative(x, deriv2_coeffs)

Ys_list = [func_Ys, deriv_Ys, deriv2_Ys, deriv3_Ys]

crit_Xs1, crit_Ys1 = [],[]
for i in range(3):
    crit_Xs1 += getCriticalvalues(x, Ys_list[i]) [0]
    crit_Ys1 += getCriticalvalues(x, Ys_list[i]) [1]
''''
crit_Xs, crit_Ys = [],[]
for i in range(3): 
    crit_Xs += getMax_Mins(x, Ys_list[i], Ys_list[i+1]) [0]
    crit_Ys += getMax_Mins(x, Ys_list[i], Ys_list[i+1]) [1]
'''
fig, ax = plt.subplots() # let more than one plot exist
ax.axhline(0,color='black', alpha = 0.5) # x = 0
ax.axvline(0,color='black', alpha = 0.5) # y = 0
ax.plot(x, func_Ys,'b',label = 'f(x)') # define each plot's equation and key label
ax.plot(x, deriv_Ys,'g--',label = "f'(x)") 
ax.plot(x, deriv2_Ys,'r:',label = 'f"(x)')
ax.plot(crit_Xs1, crit_Ys1, "ko", markersize = 7) #using 3 point comparison
#ax.plot(crit_Xs, crit_Ys, "ko", markersize = 10) #using derivatives 

ax.legend() # create a legend
ax.set_xlabel('x') # label the axis titles
ax.set_ylabel('y') # label the axis titles
ax.set_title("Plots of f(x), f'(x), f\"(x) with local max and min") # name the graph
plt.show()