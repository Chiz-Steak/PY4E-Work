# Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. 
# Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

# define the list
list_one = ['a', 'b', 'c', 'd', 'e']

# define the function that modifies the list to remove the first and last elements
def chop(t):
    del t[0]
    del t[-1]

chopped = chop(list_one)
print(chopped)

# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements

original_list = ['f', 'g', 'h', 'i', 'j']

def middle(x):
    if len(x) >= 2:
        return x[1:-1]
    else:
        return []
    
new_list = middle(original_list)
print(new_list) 
