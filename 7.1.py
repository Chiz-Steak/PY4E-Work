# Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case. 
# Executing the program will look as follows:

# python shout.py
# Enter a file name: mbox-short.txt
# FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
# RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
# RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
  #   BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
    #  SAT, 05 JAN 2008 09:14:16 -0500

# Enter the file name as input
file_name = input("Enter a file name:")

# try function to open the input and see if it matches the available files
try:
    with open(file_name, 'r') as file:
        for line in file:
            print(line.upper(), end='') # if the file matches, print the file with all uppercase
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.") # if the file isn't available, return that the file wasn't found
except Exception as e:
    print(f"An error occurred: {e}") # if there was an error, return that an error occured
