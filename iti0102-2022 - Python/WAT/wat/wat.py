"""Wat."""


def function_a(arg):
    """
    Wat.

    6166 -> 4
    10346 -> 4
    """
    return 4


def function_b(arg):
    """
    Wat.

    17496 -> 17502
    4396 -> 4402
    """
    return arg + 6


def function_c(arg):
    """
    Wat.

    4584 -> 1
    12665 -> 1
    """
    return 1


def function_d(arg):
    """
    Wat.

    1216 -> 44359680
    13609 -> 5556146430
    9587 -> 2757317070
    6901 -> 1428714030
    """
    return (arg ** 2) * 30


def function_e(arg):
    """
    Wat.

    3328 -> 1916928
    12163 -> 7005888
    7348 -> 4232448
    14245 -> 8205120
    """
    return arg * 576


def function_f(arg):
    """
    Wat.

    2550 -> 1309
    6979 -> 3542
    9919 -> 5082
    10040 -> 5082
    10671 -> 5467
    13743 -> 7007
    14838 -> 7546
    17034 -> 8701
    17697 -> 9009
    18024 -> 9240
    2973 -> 1463
    """
    return int(5236 / 2579 + (7931 * arg) / 15474)


def g(arg):
    """
    Wat.

    2550 -> 68
    6979 -> 105
    9919 -> 245
    10040 -> 124
    10671 -> 263
    13743 -> 271
    14838 -> 254
    17034 -> 368
    17697 -> 321
    18024 -> 456
    """
    return arg / 67 + h(arg) / 67


def h(arg):
    return -arg / 230 + i(arg) / 230


def i(arg):
    return arg


def function_g(arg):
    """
    Wat.

    12168 -> -12168
    """
    return -arg


def function_h(arg):
    """
    Wat.

    6110 -> 2832935239413890
    18490 -> 25943471792595740
    10553 -> 8450962798195571
    """
    return 0


if __name__ == '__main__':
    print(function_f(2550), 1309)
    print(function_f(6979), 3542)
    print(function_f(9919), 5082)
    print(function_f(10040), 5082)
    print(function_f(10671), 5467)
    print(function_f(13743), 7007)
    print(function_f(14838), 7546)
    print(function_f(17034), 8701)
    print(function_f(17697), 9009)
    print(function_f(18024), 9240)
