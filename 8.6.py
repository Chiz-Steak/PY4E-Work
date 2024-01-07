# Exercise 6:

# Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”. 
# Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

# Enter a number: 6
# Enter a number: 2
# Enter a number: 9
# Enter a number: 3
# Enter a number: 5
# Enter a number: done
# Maximum: 9.0
# Minimum: 2.0

count = 0

my_list = [] #creates the user list with inputs

while True: # Creates an infinite loop that continues until I decide to exit explicitly
    user_input = input("Enter a number (type 'done' to finish): ")

    if user_input.lower() == 'done':
        break # Exit the loop if I input 'done'

    try:
        # Try to convert the input to a float
        number = float(user_input)
        count = count + 1
        my_list.append(number) # This snippet adds the number (user's input that's now a float) to the original list (my_list)
    
    except ValueError:
        print("invalid input. Please only enter valid numbers") # This snippet suggests that the user only input valid numbers

# Calculate and display the total and count (if the count is not zero)

if count > 0:
    maximum = max(my_list)
    minimum = min(my_list)
    print(f"\nCount: {count}\nMaximum: {maximum}\nMinimum: {minimum}")
else:
    print("\nNo Valid numbers entered")
