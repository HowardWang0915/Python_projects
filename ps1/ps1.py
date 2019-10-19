## Problem 1
"""     
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
current_savings = 0.0
monthly_salary = annual_salary / 12
month = 0
while current_savings < (total_cost * 0.25):
    current_savings += (current_savings * 0.04 / 12) + (monthly_salary * portion_saved)
    month += 1
print("Number of months: ", month)
"""
## Problem 2
"""
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
current_savings = 0.0
monthly_salary = annual_salary / 12
month = 0
while current_savings < (total_cost * 0.25):
    current_savings += (current_savings * 0.04 / 12) + (monthly_salary * portion_saved)
    month += 1
    if month % 6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise
print("Number of months: ", month)
"""
## Problem 3
import math

annual_salary = int(input("Enter the starting salary: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
current_savings = 0.0
monthly_salary = annual_salary / 12
epsilon = 0.0001
month = 0
high = 1.0
low = 0.0
guess = (high + low) / 2

while abs(current_savings - total_cost * 0.25) >= epsilon and month != 36:
    guess = (high + low) / 2
    month = 0
    current_savings = 0
    monthly_salary = annual_salary / 12
    while current_savings < (total_cost * 0.25):
        current_savings += (current_savings * 0.04 / 12) + (monthly_salary * guess)
        month += 1
        if month % 6 == 0:
            monthly_salary += monthly_salary * semi_annual_raise
    if month < 36:
        high = guess
    else:
        low = guess
print("Best saving rate:", guess)