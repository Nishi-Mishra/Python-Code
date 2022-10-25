# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 12:12:30 2020

@author: nishi
"""
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Nishi Mishra
# Section: 543
# Assignment: Lab 4b-4
# Date: 15 September 2020

from math import *

#take input for coefficients of quadratic equation 
a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))  
c = int(input("Please enter the coefficient C: "))

#this is from act3 so it can format the quadform nicely 

ans = ""

arr = [c,b,a] #starts with zeroeth exponent; so the index corresponds with the exponent; 
#used arr so it could extend potentially to bigger polynomials  

def formatTerm(coeff, exp): #takes in the coefficient and whatever exponent goes along with that term
    
    ans = ""
    
    if coeff < 0: # handles neg coeff
        ans += "- "
    
    if coeff != 0: #we have a number for the coeff 
        if ( exp == 0) or (abs(coeff) != 1 and exp != 0): #either the term is c 
        #then the coeff is printed or if the term isn't c and coeff isn't 1 then printed  
            ans += str(abs(coeff))   
        
        if exp == 2:   # takes care of the x terms 
            ans += "x^2"
        elif exp == 1:
            ans += "x"

    return ans 


isFirstTerm = True #this makes sure a plus sign isn't added to the first term 

for i in reversed(range(len(arr))): #this goes from highest exp to low and index = exp 
    
    term = formatTerm(arr[i], i) #calls function 
    
    if term != "": #term is not zero 
        if isFirstTerm:
            isFirstTerm = False 
        else:
            ans += " "
            if arr[i] > 0:
                ans += "+ " 
        
        ans += term #if there exists a term, something will be printed 
        
ans += " = 0"        

#print("The quadratic equation is " + ans + " = 0")

#ACTUALLY SOLVING
#QuadForm: x = -b + sqrt(b^2 - 4ac) / 2a 

#if a & b = 0 then c should also be zero, if not then this is an invalid combination of coefficients  
if a == 0 and b == 0 and c != 0:
    print("You entered an invalid combination of coefficients")
#check if A=0 then there is a single answer;  bx + c = 0
elif a == 0:
    x = -1 * c/b
    print("The root of the equation",ans,"is x =", x)
elif (b**2 - 4*a*c) == 0 : #go through all possiblilites of what can be under the radical 
    x = -b / (2*a)
    print("The root of the equation",ans,"is x =",x)
elif (b**2 - 4*a*c) > 0 :
    x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a) 
    x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a) 
    print("The roots of the equation",ans,"are x =",x1,"and x =", x2)
elif (b**2 - 4*a*c) < 0 : #this deals with the mystical and imaginary (just adding an i)
    imaginary = sqrt(abs(b**2 - 4*a*c)) / (2*a) #we aren't rounding..hopefully that is ok 
    real = - b/(2*a)
    print ("The roots of the equation",ans,"are x =",real,"+",str(imaginary) + "i and x =",real,"-",str(imaginary) + "i")
    
#did I cover all the possibilities?? Maybe..