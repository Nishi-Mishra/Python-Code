# By submitting this assignment, I agree to the following:
#     "Aggies do not lie, cheat, or steal, or tolerate those who do."
#     "I have not given or received any unauthorized aid on this assignment."
#
# Names:          Lindsey Wilkin 
#                 Charlie Simpson 
#                 Nishi Mishra
#                 Kai Brown
# Section:        543
# Assignment:     Lab 11a-1-challenge
# Date:           01 11 2020


#CHANGE THIS SO THIS WORKS WITH THE CHALLENGE FILE
#goal is to get approximations of root 

#create a function
#real function for submission:  𝑓(𝑥) = ln(1 / (𝑥^2 + 1))sin(𝑥)

from math import * 
import numpy as np 

# test cases f(x) = x^2 - 9, 5x + 11, 4x^3 + 3x ^ 2 + 2x + 1, sin(x), and x^2 + 8x + 16

def F(x): #this function works 
  #y_val = x ** 2 - 1
  return np.log(1 / (x**2 + 1)) * sin(x) #infinite answers -- it looks like a squiggle 

def G(x):
    return x**2 + 3*x - 2 #two answers

def H(x):
    return x**4 * (x - 2) * (x + 1) + 9 #imaginary only 

def I(x):
    return x**(1/2) #no roots; imaginary only 

def J(x):
    return sin(1 + 4*cos(2*x)) + 0.5 #also an erratic squiggle -- many answers

#print("Ans:", H(3)) # all the functions get the right answers 

#find derivative 
#𝑓′(𝑥) ≅ (𝑓(𝑥+𝑎)−𝑓(𝑥)) / 𝑎
#𝑎 = 0.001
def deriv (x, myFunc): #x must be a float or int 
  a = 0.001
  return (myFunc(x+a) - myFunc(x)) / a 

#print(deriv(4)) #deriv works 

def newton_step (xi, myFunc):
  # should take in as input a guess at a root, 𝑥𝑖, and should return a new guess for the root, 𝑥𝑖+1 
  #𝑥𝑖+1 = 𝑥𝑖 − 𝑓(𝑥𝑖) / 𝑓′(𝑥𝑖)
  xi_plus1 = xi - myFunc(xi) / deriv(xi, myFunc)
  #print("%0.6f" % xi_plus1, end= ' -> ')
  return xi - myFunc(xi) / deriv(xi, myFunc) 

#print(newton_step(3))


def newton (x0, myFunc):
  #newton step is the root approx so now we need multiple 
  TOL = 10**-6
  list_of_approx = []
  
  first_step = newton_step(x0, myFunc) #"%0.6f" % x
  list_of_approx += [first_step]
  second_step = newton_step(first_step, myFunc)
  list_of_approx += [second_step]
  
  count = 0
  
  while TOL < (abs(second_step - first_step)) and count < 50:
    first_step = second_step
    second_step = newton_step(first_step, myFunc) 
    list_of_approx += [second_step]
    count += 1
    #print(second_step)
    
  if count == 50:
      return -1
  #after the tol is fulfilled return
  return list_of_approx

def getFunction(function_text): #ignore function..not needed, nor called. I misinterpretted directions 
  function_text = list(function_text)
  print(function_text)
  alpabet = "abcdefghijklmnopqrstuvwxyz" 
  numbers = "1233456678890"
  formatted_func = ""
  
  for i in range(len(function_text)): #replace if x
      
      if function_text[i].lower() in alpabet:
         function_text[i] = "x"
         
      if(function_text[i].lower() == "x" and function_text[i-1] in numbers and i != 0): #3x --> 3*x #i != 0 is because negative index will loop to the end of the line -- not good 
         function_text[i] = "*x"
         
      elif function_text[i] == "^":
         function_text[i] = "**"
    
      formatted_func += function_text[i]
      print(formatted_func)
      
  formatted_func = formatted_func.replace("x", "2")
  
  print(eval(formatted_func))

#getFunction("(3U) ^ 2") #this function works. But is not what the instructions called for 



# asks a user for an initial guess of a root, and prints the set of root approximations that Newton’s method computes from that initial guess using 6 decimal places. Format your output as shown below.

#MAIN CODE 
# take in a value x as an estimation for the function f(x)
myFunc = input("Functions: \nF(x) = log(1 / (x^2 + 1)) * sin(x) \nG(x) = x^2 + 3x - 2 \nH(x) = x^4 * (x - 2) * (x + 1) + 9 \nI(x) = x^(1/2) \nJ(x) = sin(1 + 4cos(2x)) + 0.5 \n\nAnswer in the form F, J etc. Choose a function: ")
x = float(input("Enter an initial guess for a root of "+ myFunc + "(x) : ")) 


if myFunc == "F":
    myFunc = F
elif myFunc == "G":
    myFunc = G
elif myFunc == "H":
    myFunc = H
elif myFunc == "I":
    myFunc = I
elif myFunc == "J":
    myFunc = J

listApprox = newton(x, myFunc)

if listApprox == -1:
    print("Imaginary solutions only")
else: 
    print("\nThe root approximations are:")
    print("%0.6f" % x, end=" -> ")

    for i in range(len(listApprox) - 1):
        print("%0.6f -> " % listApprox[i], end="")
    print("%0.6f" % listApprox[-1], end="")

#"3.000000 -> 3.147994 -> 3.141604 -> 3.141593 -> 3.141593"'''


##change in the other file!! 