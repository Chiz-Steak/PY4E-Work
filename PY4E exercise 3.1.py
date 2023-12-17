# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

# prompt the user for hours worked and rate per hour
hours_worked = float(input("Enter Hours: "))
rate_per_hour = float(input("Enter Rate per Hour: "))

# Calculate gross pay with overtime consideration
if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - 40
    gross_pay = (regular_hours * rate_per_hour) + (overtime_hours * 1.5 * rate_per_hour)
else:
    gross_pay = hours_worked * rate_per_hour

# Display results
print("Pay:", gross_pay)
