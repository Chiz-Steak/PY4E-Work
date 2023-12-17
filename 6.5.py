# Exercise 5: Take the following Python code that stores a string:

# str = 'X-DSPAM-Confidence:0.8475'

# Use find and string slicing to extract the portion of the string after the colon character.
# Then use the float function to convert the extracted string into a floating point number.

# find the location of the colon
str = 'X-DSPAM-Confidence:0.8475'
str_colon_position = str.find(':')

# find the portion of the string after the colon
extracted_str = str[str_colon_position + 1:]

# convert the extracted string to a floating point number
converted_str = float(extracted_str)

print(converted_str)
