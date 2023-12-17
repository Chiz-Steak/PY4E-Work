# Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string.
# Print each letter on a separate line, except backwards.

# define the fruit
fruit = 'mango'

# write the string
length = len(fruit)
index = length - 1 #start at the last character

while index >= 0:
    letter = fruit[index]
    print(letter)
    index = index - 1

