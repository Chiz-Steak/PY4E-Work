# Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.


def count(input_string, target_letter):
    count = 0
    for letter in input_string:
        if letter == target_letter:
            count += 1
    return count

# Example Usage
word = 'canada'
letter_to_count = 'a'
result = count(word, letter_to_count)
print(f"The letter '{letter_to_count}' appears {result} times in the word '{word}'.")
 
    