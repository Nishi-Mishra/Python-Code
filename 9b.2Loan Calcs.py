# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 14:12:43 2020

@author: nishi
"""

# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Nishi Mishra  
# Section: 543
# Assignment: 9b-2
# Date: 27 October 2020

'''
Prompt the user for an output file name for the data
Prompt the user for the amount of the loan (𝑃), the number of months (𝑁) over which the loan
will be repaid, and the annual interest rate (𝑖). (Note that 𝑖 should be a decimal number, not a
percentage: 0.025 not 2.5%)
'''

filename = input("Enter output file: ")
P = float(input("Enter principal amount: "))
N = int(input("Enter term length (months): "))
i = float(input("Enter annual interest rate: "))

#P = 100000
#N = 60
#i = 0.025 
J = i/12

M = (P * J) / (1 - (1 / (1+J))**N)

#filename = "out.csv"


output_file = open(filename, "w")

loan_balance = P
accrued_interest = 0
total_interest = 0  
month = 0 

output_file.write("Month,Total Accrued Interest,Loan Balance\n")

for month in range(N+1):
    if loan_balance < 0.01:
        output_file.write("{:d},${:.2f},${:s}\n".format(month,total_interest,"0.00"))
    else:
        output_file.write("{:d},${:.2f},${:.2f}\n".format(month,total_interest,loan_balance))
    
    accrued_interest = loan_balance * J
    total_interest += accrued_interest 
    loan_balance += accrued_interest - M 
    
    
#output_file.write("{:d},${:.2f},${:s}\n".format(month,total_interest,"0.00"))
    
    
    
    
output_file.close()




