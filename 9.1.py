# Exercise 1: Download a copy of the file

# www.py4e.com/code3/words.txt

# Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
# It doesn’t matter what the values are. 
# Then you can use the in operator as a fast way to check whether a string is in the dictionary.

file_name = input("Enter a file name:") # input the file 
count = 0 # initialize the count

example_dictionary = dict() # create a new dictionary with no items

# try function to open the input and see if it matches the available files
try:
    fhand = open(file_name)
except FileNotFoundError:
    print(f"ERROR: {file_name} not found.")
    quit()


for line in fhand:
    
    # read the words in words.txt and stores them as keys in a dictionary
    words = line.strip()
    example_dictionary[line] = 'keys'

    # print the dictionary
    print(example_dictionary)

# Input string to check in the dictoinary
check_string = input("Enter a string to check in the dictionary: ")

# check whether the string is in the dictionary
if check_string in example_dictionary:
    print(f"'{check_string}' is in the dictionary.")
else:
    print(f"' {check_string}' is NOT in the dictionary")

