# Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program. 
# Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name “na na boo boo”. 
# The program should behave normally for all other files which exist and don’t exist. Here is a sample execution of the program:

# python egg.py
# Enter the file name: mbox.txt
# There were 1797 subject lines in mbox.txt

# python egg.py
# Enter the file name: missing.tyxt
# File cannot be opened: missing.tyxt

# python egg.py
# Enter the file name: na na boo boo
# NA NA BOO BOO TO YOU - You have been punk'd!

# Enter the file name as the input
# Define count as 0
file_name = input("Enter a file name:")
count = 0

# try function to open the input and see if it matches the available files
try:
    with open(file_name) as file:
        for line in file:
            count += 1
        print('Line Count: ', count) # if the file matches, print the number of lines in the file
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.") # if the file isn't available, return that the file wasn't found
except Exception as e:
    print(f"An error occurred: {e}") # if there was an error, return that an error occured

if file_name == "mbox-short.txt":
    print("Na Na Boo Boo!")