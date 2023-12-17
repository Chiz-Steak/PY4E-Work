# Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.

# Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
#  < 0.6     F

# define the user_score
user_score = float(input("Enter score: "))

#define a function with parameters based on the grading range
def computegrade(user_score):
        if user_score < 1 and user_score >= 0.9:
            return('A')
        elif user_score < 0.9 and user_score >= 0.8:
            return('B')
        elif user_score < 0.8 and user_score >= 0.7:
            return('C')
        elif user_score < 0.7 and user_score >= 0.6:
            return('D')
        elif user_score < 0.6:
            return('F')
# return the computegrade function with the user_score
x = computegrade(user_score)
print(x)