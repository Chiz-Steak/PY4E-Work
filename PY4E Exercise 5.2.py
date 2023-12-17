# Exercise 2: Write another program that prompts for a list of numbers as above (answers from exercise 5.1) and at the end prints out both the maximum and minimum of the numbers instead of the average.

total = 0
count = 0

my_list = [] #creates the user list with inputs

while True: # Creates an infinite loop that continues until I decide to exit explicitly
    user_input = input("Enter a number (type 'done' to finish): ")

    if user_input.lower() == 'done':
        break # Exit the loop if I input 'done'

    try:
        # Try to convert the input to a float
        number = float(user_input)

        # If successful, update total and count
        total += number
        count += 1
        my_list.append(number)
    
    except ValueError:
        print("invalid input. Please only enter valid numbers")

# Calculate and display the total and count (if the count is not zero)

if count > 0:
    maximum = max(my_list)
    minimum = min(my_list)

    print(f"\nTotal: {total}\nCount: {count}\nMaximum: {maximum}\nMinimum: {minimum}")
else:
    print("\nNo Valid numbers entered")




