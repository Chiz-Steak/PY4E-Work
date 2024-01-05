# Exercise 3: Rewrite the guardian code in the above example without two if statements. 
# Instead, use a compound logical expression using the or logical operator with a single if statement.


try:
    fhand = open('mbox-short.txt')
except FileNotFoundError:
    print("ERROR: 'mbox-short.txt' not found.")
    quit()

count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    
    # rewrite the guardian code without two if statements
    # using the or logica operatr with a single if statement
    # check if the length of words is 0 or the first element is not 'From'
    if len(words) == 0 or words[0] != 'From' : continue
    
    # If the condition is met, print the third element of words
    print(words[2])

