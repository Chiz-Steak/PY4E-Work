# Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475

def extract_confidence(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('X-DSPAM-Confidence:'):
                    # Extract the numerical value from the line
                    confidence_value = float(line.split(':')[1])
                    print(confidence_value)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_name = input("Enter a file name: ")
    extract_confidence(file_name)

if __name__ == "__main__":
    main()
