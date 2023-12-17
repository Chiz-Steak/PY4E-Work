# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime. 
# Create a function called computepay which takes two parameters (hours and rate).

# prompt the user for hours worked and rate per hour
hours_worked = float(input("Enter Hours: "))
rate_per_hour = float(input("Enter Rate per Hour: "))
regular_hours = 40
overtime_hours = hours_worked - 40

# define a computepay function that takes two parameters hours and rate
def computepay(hours_worked, rate_per_hour):
    gross_pay = (regular_hours * rate_per_hour) + (overtime_hours * 1.5* rate_per_hour)
    return gross_pay

# print out the computepay function with the inputted hours worked and rate per hour
x = computepay(hours_worked, rate_per_hour)
print(x)