# Exercise 4: Find all unique words in a file

#Shakespeare used over 20,000 words in his works. But how would you determine that? How would you produce the list of all the words that Shakespeare used? 
# Would you download all his work, read it and track all unique words by hand?

# Let’s use Python to achieve that instead. 
# List all unique words, sorted in alphabetical order, that are stored in a file romeo.txt containing a subset of Shakespeare’s work.

# To get started, download a copy of the file www.py4e.com/code3/romeo.txt. 
# Create a list of unique words, which will contain the final result. 
# Write a program to open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split function. 
# For each word, check to see if the word is already in the list of unique words. 
# If the word is not in the list of unique words, add it to the list. 
# When the program completes, sort and print the list of unique words in alphabetical order.

file_content = ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window','with', 'yonder']

file_name = r'C:\Users\klein\OneDrive\Desktop\Code\PY4E\Exercises\Chapter 8\romeo.txt' # name the file that I want to open

unique_set = set() # empty list of unique words which will not contain the final result

with open(file_name) as file: # open and close the file and resolve any errors.
      for rows in file: # this iterates through all rows in the file
            words = rows.split() # get a list of words in each row for word in words:
            for word in words:
                  unique_set.add(word) # add the word, duplicates are discarded for word in unique:

unique_list = sorted(list(unique_set)) # Combine set and sorting in one line
print(unique_list) # prints the list of unique words

if unique_list == file_content:
      print("LISTS ARE EQUAL") # checks to see if both lists are equal
else:
      print("ERROR: LISTS ARE NOT EQUAL") # if they aren't, it will say 'ERROR'
