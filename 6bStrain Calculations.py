# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 18:47:14 2020

@author: nishi
"""

# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Nishi Mishra
# Section: 543
# Assignment: 6b-2
# Date: 30 September 2020

'''

y = 4400x  
w/ 0 <= strain <= 0.01

y = 44 #flatline 
w/ 0.01 < strain <= 0.06

y =  (400/3) (x - 0.18) + 60 ; slope = (60-44) / (0.18 - 0.06) = 400/3; pt used (0.18, 60)
w/ 0.06 < strain <= 0.18

y =  (-125) (x - 0.18) + 60 ; slope = (50-60) / (0.26 - 0.18) = -125; pt used (0.18, 60)
w/ 0.18 < strain <= 0.26


'''

strain_x = float(input("Enter the strain: ")) 
stress_y = 0

#segments 1-4; all my math work is on pdf as opposed to in my comments
if 0 <= strain_x <= 0.26:
    if 0 <= strain_x <= 0.01: 
        stress_y += 4400 * strain_x
    elif 0.01 < strain_x <= 0.06: 
        stress_y += 44
    elif 0.06 < strain_x <= 0.18:
       stress_y += (400/3) * (strain_x - 0.18) + 60
    elif 0.18 < strain_x <= 0.26:
        stress_y += (-125) * (strain_x - 0.18) + 60
    
    print("The stress is approximately {:0.1f}".format(stress_y))
    
else:
    print("Strain is undefined in that region")
    
