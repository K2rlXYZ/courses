"""EX01 Greetings."""

"""
3. Greetings
Example output:

Hi michael! Hi michael! Hi michael! Hi michael!

"""
# Ask how to greet
greeting = input("Enter a greeting: ")
# Ask who to greet
recipient = input("Enter a recipient: ")
# Ask how many times to repeat the greeting
recurrence = int(input("How many times to repeat: "))

print(f"{greeting.capitalize()} {recipient}! " * recurrence)
