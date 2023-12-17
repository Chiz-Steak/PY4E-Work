# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. 
# The following shows two executions of the program:

# 1)
    # Enter Hours: 20
    # Enter Rate: nine
    # Error, please enter numeric input

# 2)
    # Enter Hours: forty
    # Error, please enter numeric input

# insitute a try and except mechanism for this:
try:

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

except ValueError:
    print("please enter numeric input")

