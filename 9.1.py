# Exercise 1: Download a copy of the file

# www.py4e.com/code3/words.txt

# Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
# It doesn’t matter what the values are. 
# Then you can use the in operator as a fast way to check whether a string is in the dictionary.
word_dict={}

with open("words.txt", "r") as file:
    for line in file:
        # Remove newline characters and convert to lowercase for case-insensitive matching
        word = line.strip().lower()
        word_dict[word] = None

# Input string to check in the dictoinary
check_string = input("Enter a string to check in the dictionary: ").lower()

# check whether the string is in the dictionary
if check_string in word_dict:
    print(f"'{check_string}' is in the dictionary.")
else:
    print(f"' {check_string}' is NOT in the dictionary")

