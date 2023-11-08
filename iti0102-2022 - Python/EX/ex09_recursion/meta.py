"""Meta-trees and meta-dragons."""
import time
import turtle
from sys import setrecursionlimit

setrecursionlimit(10000000)


def tree(length, limit: int = 5, depth=0):
    """
    Write a recursive turtle program to draw a binary tree.

    Start with a trunk 200px tall.
    Each new branch should be 3/5 as big as its trunk.
    Minimum branch size is 5px.
    Move turtle with: t.forward(), t.left(), t.right(), tree()

    :param length: height of the trunk or leaf
    """
    if depth == 0:
        t.right(180)
        t.forward(length)
        t.right(180)
        t.forward(length)
    t.right(60)
    t.forward(length)
    if (length * 3 / 5) > limit:
        tree(length * 3 / 5, limit, depth + 1)
    t.right(180)
    t.forward(length)
    t.right(60)
    t.forward(length)
    if (length * 3 / 5) > limit:
        tree(length * 3 / 5, limit, depth + 1)
    t.right(180)
    t.forward(length)
    t.left(120)


def apply_dragon_rules(string):
    """
    Write a recursive function that replaces characters in string.

    Like so:
        "a" -> "aRbFR"
        "b" -> "LFaLb"
    apply_dragon_rules("a") -> "aRbFR"
    apply_dragon_rules("aa") -> "aRbFRaRbFR"
    apply_dragon_rules("FRaFRb") -> "FRaRbFRFRLFaLb"

    :param string: sentence with "a" and "b" characters that need to be replaced
    :return: new sentence with "a" and "b" characters replaced
    """
    if string == "":
        return ""
    if string[0] == "a":
        return "aRbFR" + apply_dragon_rules(string[1:])
    if string[0] == "b":
        return "LFaLb" + apply_dragon_rules(string[1:])
    else:
        return string[0] + apply_dragon_rules(string[1:])


def curve(string, depth, depth_count=0):
    """
    Recursively generate the next depth of rules.

    Calls apply_dragon_rules() function `depth` times.
    curve("Fa", 2) -> "FaRbFRRLFaLbFR"

    :param string: current instruction string
    :param depth: how many times the rules are applied
    :return: instructionset for drawing the dragon at iteration 'depth'
    """
    if depth_count == depth:
        return string
    string = apply_dragon_rules(string)
    return curve(string, depth, depth_count + 1)


def format_curve(string, pos=0):
    """
    Use recursions to remove  a  and  b  symbols from the instruction string.

    format_curve("Fa") -> "F"
    format_curve("FaRbFR") -> "FRFR"

    :param string: instruction string
    :return: clean instructions with only "F", "R", and "L" characters
    """
    if string == "":
        return ""
    if string[pos] == "a" or string[pos] == "b":
        return format_curve(string, pos+1)
    return string[pos] + format_curve(string, pos+1)


def draw_dragon(string, length):
    """Draws the dragon by reading the string recursively.

    Use t.right(), t.left(), t.forward() and draw_dragon() to move turtle.
        L - means turn 90 degrees to left and go forward
        R - means turn 90 degrees to right and go forward
        F - means don't turn just go forward

    :param string: instructions left to process
    :param length: how many pixels to move forward, left or right
    """
    if string == "":
        return
    if string[0] == "L":
        t.left(90)
        t.forward(length)
    if string[0] == "R":
        t.right(90)
        t.forward(length)
    if string[0] == "F":
        t.forward(length)
    return draw_dragon(string[1:], length)


def get_line_length(dragon_width, depth):
    """Return one Turtle step length if the width and depth are known."""
    return dragon_width / (2 ** (1 / 2)) ** depth


def save(t: turtle.Turtle):
    """Save the turtle graphic to file which can be opened with a image editor like GIMP."""
    t.ht()  # hide him
    t.getscreen().getcanvas().postscript(file='tree.ps')


if __name__ == '__main__':
    t = turtle.Turtle()
    t.getscreen().bgcolor("#1c262b")
    t.color("red")
    t.speed(0)
    t.pensize(2)
    t.pencolor("red")
    t.left(90)
    #tree(200)

    turtle.tracer(0, 0)
    s = curve("Fa", 10)
    print(s)
    s = format_curve(s)
    print(s)
    draw_dragon(s, get_line_length(100, 10))

    save(t)
    turtle.update()
    time.sleep(3)
