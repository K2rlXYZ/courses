"""Robot.py."""

from FollowerBot import FollowerBot


def test_run(robot: FollowerBot):
    """Do a test run for the robot."""
    robot.set_wheels_speed(30)
    robot.sleep(2)
    robot.set_wheels_speed(0)
    robot.done()


def drive_to_line(robot: FollowerBot):
    """
    Make the robot drive until all sensors hit a line.

    'seejärel sõidab edasi 15-30cm.'
    (100px -> 1 meeter)

    1 px = 0.01m = 1cm
    """
    while not min([True if x < 100 else False for x in robot.get_line_sensors()]):
        robot.set_wheels_speed(100)
        robot.sleep(0.01)
    robot.set_wheels_speed(100)
    robot.sleep(0.01 * 20)
    robot.done()


def follow_the_line(robot: FollowerBot, sleep=0.001):
    """Line follower code."""
    robot.set_wheels_speed(100)
    robot.sleep(0.15)
    buffer = []
    while len([x for x in robot.get_line_sensors() if x < 100]) != 0:
        ls = robot.get_line_sensors()
        l3, l2, l1, r1, r2, r3 = ls[0], ls[1], ls[2], ls[3], ls[4], ls[5]

        sharp_turn_check(l3, l2, l1, r1, r2, r3, robot, sleep)

        normal_turn_check(r2, l2, robot, sleep)

        if l1 < 100 or r1 < 100:
            robot.set_wheels_speed(100)
            robot.sleep(sleep)

        buffer.remove(buffer[0]) if len(buffer) > 150 else 0
        if len(buffer) > 99:
            same = True
            for x in buffer:
                if x != ls:
                    same = False
            if same:
                robot.set_wheels_speed(100)
                robot.sleep(sleep)
        buffer.append(ls)

        print(ls)
    robot.set_wheels_speed(100)
    robot.sleep(0.15)
    robot.done()


def sharp_turn_check(l3, l2, l1, r1, r2, r3, robot, sleep):
    """Code for a sharp turn."""
    if l3 > 924 and l2 > 924 and l1 > 924 and r1 > 924 and r2 > 924 and r3 < 100:
        robot.set_wheels_speed(-50)
        robot.set_left_wheel_speed(100)
        robot.sleep(sleep)
    elif l3 < 100 and l2 > 924 and l1 > 924 and r1 > 924 and r2 > 924 and r3 > 924:
        robot.set_wheels_speed(-50)
        robot.set_right_wheel_speed(100)
        robot.sleep(sleep)


def normal_turn_check(r2, l2, robot, sleep):
    """Code for a normal turn."""
    if l2 > 924 and 100 > r2:
        robot.set_wheels_speed(-80)
        robot.set_left_wheel_speed(100)
        robot.sleep(sleep)
    elif r2 > 924 and 100 > l2:
        robot.set_wheels_speed(-80)
        robot.set_right_wheel_speed(100)
        robot.sleep(sleep)


def the_true_follower(robot: FollowerBot, sleep=0.001):
    """More complex version of line follower."""
    robot.set_wheels_speed(100)
    robot.sleep(0.15)
    buffer = []
    do_the_track(robot, sleep, buffer)
    robot.set_wheels_speed(100)
    robot.set_left_wheel_speed(-100)
    robot.sleep(0.29)
    do_the_track(robot, sleep, buffer, gray=False)
    robot.set_wheels_speed(100)
    robot.sleep(0.15)
    robot.done()


def do_the_track(robot, sleep, buffer, l3=0, l2=0, l1=0, r1=0, r2=0, r3=0, gray=True):
    """Run the track with either white check or gray check."""
    if gray:
        checker = gray_check
    else:
        checker = white_check
    while not checker(l3, l2, l1, r1, r2, r3):
        ls = robot.get_line_sensors()
        l3, l2, l1, r1, r2, r3 = ls[0], ls[1], ls[2], ls[3], ls[4], ls[5]

        sharp_turn_check(l3, l2, l1, r1, r2, r3, robot, sleep)

        normal_turn_check(r2, l2, robot, sleep)

        if l1 < 100 or r1 < 100:
            robot.set_wheels_speed(100)
            robot.sleep(sleep)

        buffer.remove(buffer[0]) if len(buffer) > 160 else 0

        jump(ls, robot)
        if len(buffer) > 150:
            same = True
            for x in buffer:
                if x != ls:
                    same = False
            if same:
                robot.set_wheels_speed(100)
                robot.sleep(sleep)
        buffer.append(ls)

        print(ls, robot.time_from_start)


def jump(ls, robot):
    """Jump over holes in the track."""
    if ls == [1024, 0, 1024, 1024, 0, 1024]:
        while ls == [1024, 0, 1024, 1024, 0, 1024]:
            robot.set_wheels_speed(100)
            robot.sleep(0.1)
            ls = robot.get_line_sensors()
    if ls == [0, 0, 1024, 1024, 0, 0]:
        robot.set_wheels_speed(100)
        robot.sleep(0.1)


def gray_check(l3, l2, l1, r1, r2, r3):
    """Check for gray color on all sensors."""
    if 500 < l3 < 650 and 500 < l2 < 650 and 500 < l1 < 650 \
            and 500 < r1 < 650 and 500 < r2 < 650 and 500 < r3 < 650:
        return True
    else:
        return False


def white_check(l3, l2, l1, r1, r2, r3):
    """Check for white on all sensors."""
    if l3 == 1024 and l2 == 1024 and l1 == 1024 and r1 == 1024 and r2 == 1024 and r3 == 1024:
        return True
    else:
        return False


if __name__ == '__main__':
    robot = FollowerBot("track.png", start_x=122, start_y=255, starting_orientation=90)
    # test_run(robot)
    the_true_follower(robot)
