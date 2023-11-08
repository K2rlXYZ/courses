"""XP01 janguru."""
import math


def simulate(start, stop, step, pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    """Simulate the jangurus jumping in a certain area from start to stop.

    @:param start: point of time to start the sim
    @:param stop: point of time to stop the sim
    @:param step: how many seconds to move per iteration

    @:param pos1: position of first janguru
    @:param jump_distance1: jump distance of first janguru
    @:param sleep1: sleep time of first janguru

    @:param pos2: position of second janguru
    @:param jump_distance2: jump distance of second janguru
    @:param sleep2: sleep time of second janguru

    @:return positions where jangurus meet

    """
    for x in range(start, stop, step):
        if x % sleep1 == 0 and x % sleep2 != 0:
            if pos1 + jump_distance1 == pos2:
                return pos2

        if x % sleep2 == 0 and x % sleep1 != 0:
            if pos2 + jump_distance2 == pos1:
                return pos1

        if x % sleep1 == 0:
            pos1 += jump_distance1

        if x % sleep2 == 0:
            pos2 += jump_distance2

        if pos1 == pos2:
            return pos1
    # If they don't meet return -1
    return -1


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2) -> int:
    """Calculate the meeting position of 2 jangurus.

    @:param pos1: position of first janguru
    @:param jump_distance1: jump distance of first janguru
    @:param sleep1: sleep time of first janguru
    @:param pos2: position of second janguru
    @:param jump_distance2: jump distance of second janguru
    @:param sleep2: sleep time of second janguru

    @:return positions where jangurus first meet

    """
    # If the variables of both jangurus are equal they will only have to do one jump
    if (pos1 == pos2 and jump_distance1 == jump_distance2 and sleep1 == sleep2) or (
            pos1 + jump_distance1 == pos2 + jump_distance2 and (sleep1 / sleep2 <= 2 or sleep2 / sleep1 <= 2)):
        return pos1 + jump_distance1

    # Define jangurus speeds
    speed1 = jump_distance1 / sleep1
    speed2 = jump_distance2 / sleep2

    step = math.gcd(sleep1, sleep2)

    # Zero division check
    if speed1 - speed2 == 0:
        return simulate(0, 100, step, pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2)

    # Find the front and back intersection points (the time of their intersection) of the line of lower points of one
    # jangurus speeds and the line of upper points of the other janguru
    intersection_1 = (pos1 - jump_distance1 - pos2) / (speed2 - speed1)
    intersection_2 = (pos2 - jump_distance2 - pos1) / (speed1 - speed2)
    intersection_front = math.ceil(max(intersection_1, intersection_2))
    if intersection_front < 0:
        return -1
    intersection_back = math.floor(min(intersection_1, intersection_2))
    intersection_back = min(intersection_back - intersection_back % sleep1,
                            intersection_back - intersection_back % sleep2)
    intersection_back = max(0, intersection_back)

    # Find what position the janguru would be at given it was past or on the back intersection
    test_pos_1 = round(intersection_back / sleep1) * jump_distance1 + pos1
    test_pos_2 = round(intersection_back / sleep2) * jump_distance2 + pos2

    # Find where in the intersection area the jangurus meet
    return simulate(intersection_back, intersection_front, step, test_pos_1, jump_distance1, sleep1, test_pos_2,
                    jump_distance2, sleep2)


if __name__ == "__main__":
    print(meet_me(1, 2, 1, 2, 1, 1))  # => 3
    print(meet_me(1, 2, 1, 2, 1, 1))  # => 3
    print(meet_me(0, 2, 1, 2, 1, 1))  # => 4
    print(meet_me(1, 6, 1, 14, 5, 1))  # => 79
    print(meet_me(10, 7, 7, 5, 8, 6))  # => 45
    print(meet_me(1, 3, 2, 1, 2, 1))  # => 7
    print(meet_me(0, 15, 6, 5, 5, 3))  # => 15
    print(meet_me(1, 2, 1, 2, 1, 1))  # => 3
    print(meet_me(1, 2, 1, 2, 1, 1))  # => 3
    print(meet_me(1, 2, 1, 2, 1, 1))  # => 3
    print(meet_me(100000, 21, 2, 0, 11, 1))  # => 2200000
    print(meet_me(0, 3, 1, 20000000, 2, 1))  # => 60000000
    print(meet_me(15930, 69, 54, 926361, 55, 44))  # => 41894376
    print(meet_me(931345, 7621, 6346, 80624, 7778, 6339))  # => -1
    print(meet_me(0, 1, 1, 1, 1, 1))  # => -1
    print(meet_me(1, 1000000000000000000, 1, 1000000000000000000, 1, 2))  # => 1000000000000000001
    print(meet_me(1, 2, 1, 2, 1, 1))  # => 3
    print(meet_me(10, 7, 7, 5, 8, 6))  # => 45
    print(meet_me(100, 7, 4, 300, 8, 6))  # => 940
    print(meet_me(1, 7, 1, 15, 5, 1))  # => 50
    print(meet_me(1, 1, 1, 1, 1, 1))  # => 2
    print(meet_me(1, 1, 1000, 10, 1, 9000))  # => 12
    print(meet_me(1, 1, 1000, 10, 1, 9001))  # => 11
    print(meet_me(1, 2, 3, 4, 5, 5))  # => -1
    print(meet_me(0, 1, 1, 1, 1, 1))  # => -1
    print(meet_me(1, 2, 1, 1, 3, 1))  # => -1
    print(meet_me(3, 5, 10, 4, 1, 2))  # => 8
    print(meet_me(4662, 94, 4611, 4978, 12, 3375))  # => 5038
    print()
    print(meet_me(3576, 73, 6152, 17230, 10, 3069))  # => 22410
    print()
    print(meet_me(9550, 34, 7262, 10874, 14, 3003))  # => 313204
    print(meet_me(46017, 333, 1084, 933597, 900, 5047))  # => 2163897
