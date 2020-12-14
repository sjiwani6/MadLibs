""" 
This is a simple implementation of a MadLibs program. 
Here, we have 4 variables of type string that we read in from the user. 
"""

# input reads in user input. In parentheses, we pass in the prompt that will be shown to the user in the console.
adjective = input("Enter an adjective: ")
noun = input("Enter a plural noun: ")
color = input("Enter a color: ")
place = input("Enter a place: ")

print("-------------------------------------------------------------------")
print("Roses are", adjective)
print(noun, "are", color)
print("Welcome to", place)
print("It's great to have you here!")
