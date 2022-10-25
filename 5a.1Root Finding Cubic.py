# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Nishi Mishra
# Section: 543
# Assignment: 5a-1
# Date: 25 September 2020

#𝑓(𝑥) = 𝐴𝑥^3 + 𝐵𝑥^2 + 𝐶𝑥 + D  

#TEST CASES: 
#f(x) = x^3 + x^2 + x + 1 
#A=1 B=1 C=1 D=1; root: x = -1; with bounds of x = -2 & 2 and bounds of x = -1.5 & 0.1

#f(x) = 2x^3 + 5x^2 + x - 2 
#A=2 B=5 C=1 D=-2; roots: x = -2, -1, 0.5; with bounds of x = -2.5 & -1.5 and  x = -1.5 & 0 and x = 0 & 5 and x = 0 & 0.5

#f(x) = 2x^3 + 5x^2 + x - 3
#A=2 B=5 C=1 D=-3; root: x = 0.618 with bounds of x = 0 & 1

#f(x) = -x^3 + 3x^2 + x - 1
#A=-1 B=3 C=1 D=-1; roots: x = -0.675, 0.461, 3.214 with bounds of x= 2 & 4 and x = -5 & -0.1

#f(x) = -x^3 - 4x^2 + x + 0
#A=-1 B=-4 C=1 D=0; root: x=-4.236 with bounds of x = -5 & -3

#for test cases use desmos https://www.desmos.com/calculator/v3hgzjtpo5

'''
Take as input from the user the coefficients of the cubic polynomial via the keyboard
• Take as input from the user the lower (𝑎) and upper (𝑏) bounds of an interval on 𝑥 that includes one single root of the cubic polynomial
• Determine the value of that root to within 10-6 tolerance
• Print the value of the root found (use the average of the interval bounds) to three (3) decimal places
• Print out how many iterations it took to find that root
• Also, as stated above, include the detail of your five test cases in comments just under the header information
• Use the output format on doc 
'''

#input statements / inititializers 

a = float(input("Enter the coefficient A: "))
b = float(input("Enter the coefficient B: "))
c = float(input("Enter the coefficient C: "))
d = float(input("Enter the coefficient D: "))

lower_bound = float(input("Enter the lower bound of the interval: "))
upper_bound = float(input("Enter the upper bound of the interval: "))

TOL = 10**(-6) #given in problem 

def findValFunc (val,a,b,c,d): #gets an upper bound or lower bound in val; and coefficients a,b,c,d and returns value of f(val)
  
  #𝑓(𝑥) = 𝐴𝑥^3 + 𝐵𝑥^2 + 𝐶𝑥 + D 
  ans = a*(val)**3 + b*(val)**2 + c*(val) + d 

  return ans

#see if f(a) or f(b) are the roots themselves 
if(findValFunc(upper_bound,a,b,c,d) == 0):
  print("Root is at x = %.3f" % upper_bound)
elif(findValFunc(lower_bound,a,b,c,d) == 0):
  print("Root is at x = %.3f" % lower_bound)

else: #the roots aren't the bounds so check if the interval even contains a root first 

  #see if the input is possible f(a) and f(b) have different signs #add this under a nested else -- done 
  if( ((findValFunc(upper_bound,a,b,c,d) > 0) and (findValFunc(lower_bound,a,b,c,d) > 0)) or \
      ((findValFunc(upper_bound,a,b,c,d) < 0) and (findValFunc(lower_bound,a,b,c,d) < 0)) ): 
    #this looks long but this just checks if the value of f(a) and f(b) are either both (+) or both (-) 
    print("These bounds are invalid and do not contain a root")

  found = False #this sees we already found the root and do not need to reprint possibly wrong answer  

  #handle two cases 
  #if f(low) is (-) then graph looks like '/'

  if(findValFunc(lower_bound,a,b,c,d) < 0):
    #maybe have a while loop with the condition checking the tolerance bounds
    #then get 'p' or the bisected number between upper and lower bounds; replace original (override bc that info is no longer needed)
    #have an iterator to see how many bisections happened; 
    #when tolerance is below specified amount, then print any bound as the root/answer overall  
    iterator = 0

    while ((upper_bound - lower_bound) > TOL): #while interval is too big bisect and replace 
      bisect_val = (upper_bound - lower_bound) / 2 + lower_bound #p = bisect_val 

      if(findValFunc(bisect_val,a,b,c,d) <= 0): #if p is (-) then since graph looks like '/' p should replace the lower bound 
        lower_bound = bisect_val
      elif(findValFunc(bisect_val,a,b,c,d) > 0): #the opposite 
        upper_bound = bisect_val 
      else:
        print("The root is at x = %.3f" % bisect_val) # f(p) must be zero 
        found = True
        break #this gets out of neverending while 

      iterator += 1


  #if f(low) is (+) then graph is '\' 

  elif(findValFunc(lower_bound,a,b,c,d) > 0): #this 2nd if sequence is nearly identical to the one above, but everything is backwards 

    iterator = 0

    while ((upper_bound - lower_bound) > TOL): #while interval is too big bisect and replace and abs is needed bc answer is negative 
      bisect_val = (lower_bound - upper_bound) / 2 + upper_bound #p = bisect_val 

      if(findValFunc(bisect_val,a,b,c,d) >= 0): #if p is (+) then since graph looks like '\' p should replace the lower bound 
        lower_bound = bisect_val
      elif(findValFunc(bisect_val,a,b,c,d) < 0): #the opposite 
        upper_bound = bisect_val 
      else:
        print("The root is at x = %.3f" % bisect_val) #if f(p) is not (+) nor (-)then must be zero and that is a root 
        found = True
        break #this gets out of neverending while 
      
      iterator += 1

  if(not found):
    print("The root is at x = %.3f" % lower_bound) #you can choose any bound because this went through both cases and their respective while loops 
  #so the bounds are close enough together that any bound is good 

  print("It took %d iterations to find the root" % iterator)