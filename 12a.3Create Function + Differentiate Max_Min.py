# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:          Nishi Mishra 
#                 
# Section:        543
# Assignment:     Lab 12a-1
# Date:           16 November 2020

#user enters a bunch of coefficients in descending order
#get the 1st and second derivative expressions 
#use numpy and pyplot to plot the lines -- look at the previous labs 
#find local max and min by looping through points 
#graph with different colors so people can see 

import numpy as np
import matplotlib.pyplot as plt 
from math import *

def getFunctionYs(x, user_func):
    '''The function takes in a list of x-values and the string given by the user. Then it returns the y-values of the user defined function'''
    eq = eval(user_func)
    return eq

def getDerivative(x, func_Ys):
    ''' 
    This function takes in a list of x-vals and y-vals and gets the derivative y-values 
    by doing delta y over delta x and taking out the last x-value so the number of y-vals 
    and x-vals the function outputs for the derivative is the same. '''
    
    deriv_Ys = []
    x_vals = x[:] #I make a copy for safety reasons 
    
    for i in range(len(x_vals)-1):
        deriv_Ys += [(func_Ys[i] - func_Ys[i+1]) / (x_vals[i] - x_vals[i+1])]
        
    return x_vals[:-1], deriv_Ys #taking off the last x-value to even out the number of points 
    

def getDerivativeYs (x_list, user_func):
    '''
    This function works, but I want a simple function which works for all values 
    and making a derivative out of points is much easier. This function takes in an x list and 
    the user function and does the derivative numerically. I abandoned this approach after thinking about higher degrees 
    '''
    
    list_Ys = []
    
    for x in x_list: 
        
        A, TOL = 0.1, 10**(-6)
        f_plusA = user_func.replace("x", "(x + A)")
        f_minusA = user_func.replace("x", "(x - A)")
    
        # ans1 = (findValFunc(x+A,a,b,c,d) - findValFunc(x-A,a,b,c,d)) / (2*A) #from 5a_Act2
        # A = A/2
        # ans2 = (findValFunc(x+A,a,b,c,d) - findValFunc(x-A,a,b,c,d)) / (2*A) 
        
        ans1 = (eval(f_plusA) - eval(f_minusA)) / (2*A)
        A = A/2
        ans2 = (eval(f_plusA) - eval(f_minusA)) / (2*A)
        
        while (abs(ans1 - ans2) > TOL):
          #print("Ans1:",ans1,"Ans2:", ans2)
          ans1 = ans2 #ans1 has old value 
          A = A / 2
          ans2 = (eval(f_plusA) - eval(f_minusA)) / (2*A) #ans2 is the new value
          
        list_Ys += [ans2]
        
    return list_Ys #should be a list
    
    # dx = x[1]-x[0] #another approach is using this however I do not have the math knowledge necessary 
    # y = func_Ys
    # dydx = np.gradient(y, dx)
    # return dydx

def interpolate (x1, x2, y1, y2, dydx1, dydx2):
    ''' By treating f\' and f" as lines I found where f\' is zero and that is the x for which y-val 
    I found and returned. I returned the x-val making f\' = 0 and the y-val at that point. '''
    
    #TOL = 10**(-6) #I wanted to use the bisect method but I don't have the functions for higher derivatives so I cannot just do f'(4) and get an answer sadly
    
    m = (dydx1 - dydx2) / (x1 - x2) #so this is treating f' and f as lines and at this point they are really close to lines because I am dividing the section count into a 1000 
    
    x = ( -1*dydx1 + m * x1 ) / m #this equation came from rearranging the point slope equation        
    #this is the x value which the derivative function's y is zero. 
    
    m2 = (y1 - y2) / (x1 - x2)
    
    y = m2 * (x - x1) + y1 #again easy slop-intercept equation
    
    return x, y #this function may have been done wrong because it was too easy and I treated these as lines which at this point of zooming they may as well be. 
    

def getCritVals(x, eq, dxeq):
    ''' This takes in  x-value list and y-value list of function and returns the max and min via derivatives'''
    crit_Xs = []
    crit_Ys = []
    for i in range(len(dxeq)-1):
        if dxeq[i] > 0 and dxeq[i+1] < 0: # /\ 
            x_crit,y_crit = interpolate(x[i], x[i+1], eq[i], eq[i+1], dxeq[i], dxeq[i+1])
            crit_Xs += [x_crit]
            crit_Ys += [y_crit]
            #crit_Xs += [x[i]] #delete 
            #crit_Ys += [eq[i]]
            
        elif dxeq[i] < 0 and dxeq[i+1] > 0: # \/ 
            x_crit,y_crit = interpolate(x[i], x[i+1], eq[i], eq[i+1], dxeq[i], dxeq[i+1])
            crit_Xs += [x_crit]
            crit_Ys += [y_crit]
            #crit_Xs += [x[i]] #delete
            #crit_Ys += [eq[i]]
    
    return crit_Xs, crit_Ys


# =============================================================================
                                # MAIN CODE
# =============================================================================
  
#user_func = "2*x**3 + 3*x**2 - 11*x - 6"
#user_func = "np.sin(x)"
# user_x1, user_x2 = int("-5"), int("5")
# user_y1, user_y2 = int("-1"), int("1")

user_func = input("Welcome and enter a function using python syntax. \n\nMath is imported with * (no need for math.pi just pi is fine) \nand numpy is imported as np. Remember ^ and multiplication \nsigns for it to be understood. (I do not handle bad inputs) \n\nEnter function here: ")
user_x1, user_x2 = int(input("Enter a lower x-value for graphing: ")), int(input("Enter an upper x-value for graphing: "))
user_y1, user_y2 = int(input("Enter a lower y-value for graphing: ")), int(input("Enter an upper y-value for graphing: "))

x = np.linspace(user_x1, user_x2, 10000) 

func_Ys = getFunctionYs(x, user_func)
x_vals1, deriv_Ys = getDerivative(x, func_Ys)
x_vals2, deriv2_Ys = getDerivative(x_vals1, deriv_Ys)
x_vals3, deriv3_Ys = getDerivative(x_vals2, deriv2_Ys)


Ys_list = [func_Ys, deriv_Ys, deriv2_Ys, deriv3_Ys]

crit_Xs, crit_Ys = [],[]
for i in range(3):
    crit_Xs += getCritVals(x, Ys_list[i], Ys_list[i+1]) [0]
    crit_Ys += getCritVals(x, Ys_list[i], Ys_list[i+1]) [1]
    

fig, ax = plt.subplots() # let more than one plot exist
ax.plot(x, func_Ys,'b',label = 'f(x)') # define each plot's equation and key label
ax.plot(x_vals1, deriv_Ys,'g--',label = "f'(x)") 
ax.plot(x_vals2, deriv2_Ys,'r:',label = 'f"(x)')
ax.plot(crit_Xs, crit_Ys, "ko", markersize = 4)
plt.axis([user_x1-0.25, user_x2+0.25, user_y1-0.25, user_y2+0.25]) # I added on the edges bit so the graph doesn't look crowded on the sides. Pls don't count off lol 
ax.legend() # create a legend
ax.axhline(0,color='black', alpha = 0.5) # x = 0 
ax.axvline(0,color='black', alpha = 0.5) # y = 0 #alpha makes the lines not as dark 
ax.set_xlabel('x') # label the axis titles
ax.set_ylabel('y') # label the axis titles
ax.set_title("Plots of f(x), f'(x), f\"(x) with local max and min") # name the graph
plt.show()

'''
Instructions:
    
Rather than working only with polynomials, allow your program to work with an arbitrary, user
defined function. (+15 bonus points)

Instead of finding maxima and minima of the main function and the derivative curve by just
searching through a list of points, find roots of the derivative curve (or of the second derivative
curve), which will represent local minima and maxima. (+30 bonus points)

Plot your curves over an arbitrary range of x and y values (you can ask the user, or determine
these automatically) (+10 bonus points)
'''


'''
 Prior to writing code, identify what existing functions you will be making use of both in
the “main” program and from prior programs, what new functions, if any, need to be
written, and what prior functions need to be modified.

    # I need a function handling a user inputted function and getting the y-values. 
    # Another function needs to be created finding the derivative a different way using derivatives instead of the 3-point comparison. 
    # To support the derivative function I need a bisect or interpolate function which narrows the gap between the two points 
    # where the slope changes from + to - or vice versa 

b. After you have implemented the code, reflect: How, if at all, would you have designed
prior parts of your program differently to allow for this expansion? If it was very easy to
add in a new piece of code, your answer might be that your prior design worked well
and was easy to expand in this way

    # well the previous code created as a group was definitely not flexible. The derivative function only worked 
    # with polynomials as well as the getFunction() which returned the y-vals of the function. The critical value function 
    # we used was with 3-pt comparison. The second function I made in the previous lab was using the derivative and that 
    # actually worked very well. I copied and pasted and only slightly changed that one. x/y values being picked by the user 
    # only required a slight modification to the np.linspace definition of x and the plotting. I add 0.5 and subtract 0.5 to the values so everything fits better on the page and it looks less crowded on the edges. Purely for aestic reasons.  
    # if I had known before I would be expanding in this way, I would have calculated the derivative not using the power rule. But everything else would be the same... 
'''