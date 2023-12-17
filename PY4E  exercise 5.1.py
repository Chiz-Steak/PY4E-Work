# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. 
# Once “done” is entered, print out the total, count, and average of the numbers. 
# If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.


total = 0
count = 0
my_list = [] #creates the user list with inputs

while True:
    user_input = input("Enter a number (type 'done' to finish): ")

    if user_input.lower() == 'done':
        break # Exit the loop if th euser enters 'done'

    try:
        # Try to convert the input to a float
        number = float(user_input)

        # If successful, update total and count
        total += number
        count += 1
    
    except ValueError:
        print("invalid input. Please only enter valid numbers")

# Calculate and display the total, count, and average
if count > 0:
    average = total / count
    print(f"\nTotal: {total}\nCount: {count}\nAverage: {round(average, 2)}")
else:
    print("\nNo Valid numbers entered")






    
    



