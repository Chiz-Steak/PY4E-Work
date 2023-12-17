# Exercise 6: Read the documentation of the string methods at https://docs.python.org/library/stdtypes.html#string-methods. 
# You might want to experiment with some of them to make sure you understand how they work. 
# strip and replace are particularly useful.

# The documentation uses a syntax that might be confusing. 
# For example, in find(sub[, start[, end]]), the brackets indicate optional arguments. 
# So sub is required, but start is optional, and if you include start, then end is optional.

gen_str = "two households, both alike in dignity, In fair Verona, where we lay our scene."

x = str.capitalize(gen_str)
print(x)

y = str.find('households', 'l')
print(y)

z = str.center('households', 10)
print(z)

