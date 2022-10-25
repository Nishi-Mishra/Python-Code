# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:30:29 2020

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
# Assignment: 4a-3
# Date: 18 September 2020


########## Part A ##########

a = input("Enter True or False for a: ")
b = input("Enter True or False for b: ")
c = input("Enter True or False for c: ")

def getValue (bool_val):

  if (bool_val == "True" or bool_val == "T" or bool_val == "t"):
    return True
  else:
    return False 

A = getValue(a)
B = getValue(b)
C = getValue(c)

########## Part B ##########

print(A and B and C)
print(A or B or C)

########## Part C ##########

'''
Given values for two Boolean variables a and b, the expression evaluates to True if just one of a or b is True, but not if both are True or both are False
''' 

#if a or b is True then answer is True
#if a and b are either both True or both False then answer is False

print((A or B) and not(A and B)) 

#think if a = T & b = T then:
#a or b = True
#a & b = True --> not a & b = False
#therefore overall ans = False  

#think if a = F & b = F then:
#a or b = False
#therefore overall ans = False  

#think if a = T & b = F then:
#a or b = True
#a & b = False --> not a & b = True
#therefore overall ans = True !! 

#all cases work -- yay 

'''
2. Given values for three Boolean variables a, b, and c, the expression evaluates to True if an odd number (i.e. exactly 1 or 3) of the variables a, b, and c is True, and is False otherwise.
'''
#a = False
#b = True   these were the testers 
#c = False 

print ((A and B and C) or (A and not B and not C) or (B and not C and not A) or (C and not A and not B))

# I checked if they are all True or if one was True

#let a = T; b = T; c = T then: 
# a and b and c = True
# therefore overall ans = True 

#let a = T; b = T; c = F then: 
# a and b and c = False
# a and not b and not c --> T and F and T = False 
# b and not c and not a --> T and T and F = False
# c and not a and not b --> F and F and F = False 
# therefore overall ans = False  

#let a = T; b = F; c = F then: 
# a and b and c = False
# a and not b and not c --> T and T and T = True 
# therefore overall ans = True   

#different combinations still hold true (lol far too many T & F) and everything works! 

########## Part D ##########

#a = True
#b = False 
#c = False 

#print((not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b))
print((not (A and not B) or (not C and B)) and (not B) or (not A and B and not C) or (A and not B)) #forgot capitals

'''
To be true:

(a and not b) means that a = T & b = F 
not ^(a and not b)^ means that a = F and b = T 

(not c and b) means that c = F and b = T 

(^not (a and not b)^ or ^(not c and b)^) means either 
  a = F & b = T   or   c = F & b = T 

(^(not (a and not b) or (not c and b))^ and (not b)) means 
  either ( a = F & b = T   or   c = F & b = T ) and  b = F 
* b must be F therefore the entire previous part is impossible!!

(not a and b and not c) means
  a = F & b = T & c = F

(a and not b) means
  a = T & b = F 

(^(not (a and not b) or (not c and b)) and (not b)^  or  ^(not a and b and not c)^  or  ^(a and not b)^)

overall mess: b = F  or  a = F & b = T & c = F  or  a = T & b = F

# for that last one if b = F to get it true then it isn't needed 

smaller mess: b = F  or  a = F & b = T & c = F 

#put into real python below; also know ^ means that I defined the result above, so I don't go cross-eyed and miss something 
'''
#print ((not B) or (not A and B and not C)) #UNCOMMENT !!
#yay the drums are drumming and angels are singing 

#next one; I got thisss

print ((not ((B or not C) and (not A or not C)))  or (not (C or not (B and C))) or (A and not C) and (not A or (A and B and C) or (A and ((B and not C) or (not B)))))

'''
To be true:

(b or not c) means b = T or c = F
(not a or not c) means a = F or c = F 

(^(b or not c)^ and ^(not a or not c)^) means 
  (b = T or c = F) and  (a = F or c = F) 
# c = F cannot be pulled out bc logic 

*(not ^((b or not c) and (not a or not c))^) means 
  either (b = T or c = F)  or  (a = F or c = F) is false or both  
   (b = F and c = T)  or  (a = T and c = T) is True --> I did a T/F switcharoo DeMorgan's theorem  
 
(b and c) means b = T & c = T
not ^(b and c)^ means b = F or c = F 
(c  or  ^not (b and c)^) means 
  c = T   or   b = F & c = F 

*(not ^(c or not (b and c))^) means either
  c = F   and   b = T and c = T 
  #if c = T/F at the same time, it is impossible so the expression is always False 

(a and not c) means a = T & c = F
(a and b and c) means a = T & b = T & c = T
(b and not c) means b = T & c = F 
(not a or ^(a and b and c)^ or (a and (^(b and not c)^ or (not b))))
  (a = F)  or  (a = T & b = T & c = T)  or  (a = T & ((b = T & c = F ) or b = F))
  #nothing reduces? 

*(a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))
  (a = T & c = F) and ((a = F)  or  (a = T & b = T & c = T)  or  (a = T & ((b = T & c = F ) or b = F)))
# if c must be false to even keep going then triple true-& isn't possible! 
  (a = T & c = F) and ((a = F) or  (a = T & ((b = T & c = F ) or b = F)))
# if a must equal T to get in, then a = F is impossible
  (a = T & c = F) and ((a = T & ((b = T & c = F ) or b = F)))
# For the 3rd batch c = F is redundant & a = T is redundant 
  (a = T & c = F) and ((b = T) or b = F)
# Then it turns into b can be T or F so a check isn't even necessary. So just see if a = T & c = F
  (a = T & c = F)

(not ((b or not c) and (not a or not c)))    or     (not (c or not (b and c)))    or     (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))
giant mess: ((b = F and c = T)  or  (a = T and c = T))    or    (a = T & c = F)
#all 'or' are at same level 
smaller mess: b = F and c = T  or  a = T and c = T    or    a = T and c = F
#
smaller mess: c = T and (b = F or a = T) or a = T and c = F

'''
print ((not B) or (not A and B and not C)) #1st expression reduced 
print ((C and (not B or A)) or (A and not C))
