# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 10:55:45 2020

@author: nishi
"""

# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Nishi Mishra  
# Section: 543
# Assignment: 10b-1
# Date: 31 October 2020

import numpy as np 
import matplotlib.pyplot as plt 

Xs = [] 
Ys = []


start_point = np.array([[1],[0]])
arr = np.array([[1.00583, -0.087156], [0.087156, 1.00583]])
#arr_of_Xs.append(start_point[1][0])


current_point =  arr @ start_point 
Xs.append(current_point[0][0])
Ys.append(current_point[1][0])

for i in range (250):
    current_point = arr @ current_point 
    Xs.append(current_point[0][0])
    Ys.append(current_point[1][0])
    

plt.plot(Xs,Ys, "b*-")
plt.suptitle("Spirals")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()



    
    