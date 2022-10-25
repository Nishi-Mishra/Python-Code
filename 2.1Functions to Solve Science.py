# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 16:43:05 2020

@author: nishi
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Nishi Mishra
# Section: 543
# Assignment: Lab 2b-1
# Date: 26 August 2020


# Programmer's note!! Please read! I am submitting the same code I wrote before because 
# I already used variables and I wrote a function for reusability
# My previous teacher from 2 years ago drilled it into use to never just hardcode values 
#this is why the code is identical. If you want me to rewrite the first lab's code I can 
#but know that I didn't copy. Aggie's honor  
'''
Program part 1

Calculate the voltage across a conductor with resistance 20 ohms and a current of 5 amperes.
Ohm’s Law states that the current through a conductor between two points is directly
proportional to the voltage across the two points.
'''
import math #not sure how to do tan without importing math but it was also not taught yet...?

#print('What is the voltage across a conductor, if it has a resistance 20 ohms and a current of 5 amps ?')

def findVolt (ohm, amp): #V=IR
    
    volt = amp * ohm
    return str(volt) 

print ("Voltage is " + findVolt(20, 5) + " V")

'''
Calculate the kinetic energy of an object with mass 100 kg and velocity 21 m/s. The Kinetic
Energy of an object is the energy that it possesses due to its motion. The standard unit of kinetic
energy in the SI system is the joule (J).
'''

def findK (m, v):
    k = 1/2 * m * (v**2)
    return str(k)

print ("Kinetic energy is " + findK(100, 21) + " J")

'''
Calculate how much Radon-222 is left after 5 days of radioactive decay given an initial amount
of 3 g and a half-life of 3.8 days. The equation for radioactive decay is
𝑁(𝑡) = 𝑁02^−𝑡/𝑡1/2
where 𝑁0 is the intial amount (units of grams), 𝑡 is the time (units of days), and 𝑡1/2 is the halflife (units of days).
'''

def decay (initial, timepassed, halflife):
    leftover = initial * 2 ** (-timepassed/halflife)
    
    return str(leftover)

print("Radon-222 left is " + decay(3, 5, 3.8) + " g")

'''
Calculate the shear stress when a normal stress of 20 lbf/in^2 is applied to a material with
cohesion 2 lbf/in^2 and angle of internal friction 35 degrees. More generally, the Mohr-Coulomb theory is a
mathematical model that describes the response of brittle materials, like concrete or rubble
piles, to shear stress as well as normal stress. Most of the classical engineering materials

somehow follow this rule in at least a portion of their shear failure envelope. The Mohr-
Coulomb criterion is represented by

τ = σ tan(φ) + c

where τ is the shear stress (units of lbf/in^2), σ is the normal stress (units of lbf/in^2), φ is the
angle of internal friction (units of radians), and c is the cohesion (units lbf/in^2)
                                                                      
'''

def MCFC (deg, o, c): # The Mohr-Coulomb Failure Criterion
   
    rad = deg * math.pi/180 # converting degrees to radians 
    
    r = o * math.tan(rad) + c # formula for sheer stress 
    
    return r

print ("Shear stress is", MCFC(35,20,2),"lbf/in^2")