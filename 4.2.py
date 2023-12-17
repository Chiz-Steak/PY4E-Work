#Exercise 2: Move the last line of this program to the top, so the function call appears before the definitions. 
# Run the program and see what error message you get.

repeat_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


def repeat_lyrics():
    print_lyrics()
    print_lyrics()

# I received the following error:
Traceback (most recent call last):
  File "c:\Users\klein\OneDrive\Desktop\Code\PY4E\Exercises\Chapter 4\4.2.py", line 4, in <module>
    repeat_lyrics()
    ^^^^^^^^^^^^^
NameError: name 'repeat_lyrics' is not defined