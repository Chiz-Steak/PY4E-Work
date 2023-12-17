# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. 
# If the score is out of range, print an error message. 
# If the score is between 0.0 and 1.0, print a grade using the following table:

# Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
#  < 0.6     F

# create the input variable
try: 
    user_score = float(input('Enter the score: '))

# create the if statement to determine the score and subsequent grade
    # check if the score is within rang
    if user_score < 0.0 or user_score > 1.0:
        print('bad score')
    else:
        # determine the grade based on the score
        if user_score < 1 and user_score >= 0.9:
            print('A')
        elif user_score < 0.9 and user_score >= 0.8:
            print('B')
        elif user_score < 0.8 and user_score >= 0.7:
            print('C')
        elif user_score < 0.7 and user_score >= 0.6:
            print('D')
        elif user_score < 0.6:
            print('F')

except ValueError:
    print('bad score')


