"""EX01 Hello."""

"""
1. Print Hello
Example output:

What is your name? Jaan
Hello, Jaan! Enter a random number: 4
Great! Now enter a second random number: 7
4 + 7 is 11
"""

# Ask for user's name
name = input("What is your name? ")
# Greet the user and ask for the first number
first_number = int(input(f"Hello, {name}! Enter a random number: "))
# Ask for the second number
second_number = int(input("Great! Now enter a second random number: "))
# Print the sum of the numbers
print(f"{first_number} + {second_number} is {first_number + second_number}")
