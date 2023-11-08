"""EX01 Poem."""

"""
2. Poem
Example output:

Roses are red,
Bozos are blue,
I love to workout
And so will you!

"""
# Ask for a color
color = input("What is your favorite color? ")
# Ask for an object that rhymes with roses
objects = input("What is an object that rhymes with roses: ")
# Ask for an activity
activity = input("What do you love to do? ")

print(f"\nRoses are {color},")
print(f"{objects} are blue,")
print(f"I love to {activity}")
print("And so will you!")
