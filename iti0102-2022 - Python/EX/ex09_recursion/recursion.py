"""If you're going to perform recursion, you need to use recursion."""


def loop_reverse(s: str) -> str:
    """
    Reverse a string using a loop.

    loop_reverse("hey") => "yeh"
    loop_reverse("aaa") => "aaa"
    loop_reverse("") => ""
    loop_reverse("1") => "1"

    :param s: input string
    :return: reversed input string
    """
    return s[::-1]


def recursive_reverse(s: str, index=-1) -> str:
    """
    Reverse a string using recursion.

    recursive_reverse("hey") => "yeh"
    recursive_reverse("aaa") => "aaa"
    recursive_reverse("") => ""
    recursive_reverse("1") => "1"

    :param s: input string
    :return: reversed input string
    """
    if index > -len(s) - 1:
        return s[index] + recursive_reverse(s, index - 1)
    return ""


def loop_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using a loop.

    loop_sum(0) => 0
    loop_sum(3) => 6
    loop_sum(5) => 15

    :param n: the last number to add to the sum
    :return: sum
    """
    return sum(range(n + 1))


def recursive_sum(n: int, i=0) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using recursion.

    recursive_sum(0) => 0
    recursive_sum(3) => 6
    recursive_sum(5) => 15

    :param n: the last number to add to the sum
    :return: sum
    """
    if i < n + 1:
        return recursive_sum(n, i + 1) + i
    return 0


def countdown(n: int):
    """
    Write a simple recursive function that returns a list of numbers that count down from n.

    countdown(5) -> [5, 4, 3, 2, 1, 0]
    countdown(8) -> [8, 7, 6, 5, 4, 3, 2, 1, 0]
    countdown(-1) -> []

    :param n: start
    :return: countdown sequence
    """
    if n > -1:
        return [n] + countdown(n - 1)
    return []


def add_commas(n: int, index=-1, depth=0):
    """
    Add commas into a number.

    In representing large numbers, from the right side to the left,
    English texts usually use commas to separate each group of three digits in front of the decimal.

    Your challenge is to output a number n formatted with commas.

    add_commas(1245) -> '1,245'
    add_commas(123456789) -> '123,456,789'
    add_commas(1011) -> '1,011'

    :param n: int
    :return: string of the formatted int
    """
    if index > -len(str(n)) - 1:
        if depth == 0:
            if (index + 1) % 3 == 0:
                return (add_commas(n, index - 1, depth + 1) + str(n)[index] + ",").strip(",")
            else:
                return (add_commas(n, index - 1, depth + 1) + str(n)[index]).strip(",")
        if (index + 1) % 3 == 0:
            return add_commas(n, index - 1, depth + 1) + str(n)[index] + ","
        else:
            return add_commas(n, index - 1, depth + 1) + str(n)[index]
    return ""


def sum_digits_recursive(number: int, index=0) -> int:
    """
    Return the sum of the digits in number.

    Given a non-negative int n, return the sum of its digits recursively (no loops).

    sum_digits_recursive(123) => 6
    sum_digits_recursive(1) => 1
    sum_digits_recursive(0) => 0
    sum_digits_recursive(999) => 27

    Hint: turn the number into string and take one digit at a time.

    :param: number: non-negative number
    :return: sum of digits in the number
    """
    if index < len(str(number)):
        return sum_digits_recursive(number, index + 1) + int(str(number)[index])
    return 0


def pair_star_recursive(s: str, index=0) -> str:
    """
    Add star between identical adjacent chars.

    Given a string, compute recursively a new string
    where identical chars that are adjacent in the original string
    are separated from each other by a "*".

    pair_star_recursive("abc") => "abc"
    pair_star_recursive("aa") => "a*a"
    pair_star_recursive("aaa") => "a*a*a"
    pair_star_recursive("") => ""

    :param s: input string
    :return: string with stars between identical chars.
    """
    if index < len(s):
        if index == len(s) - 1:
            return s[index]
        return s[index] + "*" + pair_star_recursive(s, index + 1) \
            if s[index] == s[index + 1] \
            else s[index] + pair_star_recursive(s, index + 1)
    return ""


def stonks(coins: float, rate: float, years: int) -> int:
    """
    Each year your crypto-investment grows.

    Write a recursive function that calculates the net worth of coins after some years.
    Rate is in percents.
    Round the answer down to the nearest integer.

    stonks(1000, 10, 10) -> 2593
    stonks(100000, 12, 3) -> 140492

    :param coins: starting amount (0-10000)
    :param rate: rate percentage (0-100)
    :param years: number of years (0-50)
    :return: coins after years
    """
    if years == 0:
        return coins
    else:
        return int(stonks(coins * ((100 + rate) / 100), rate, years - 1))


def quic_mafs(a: int, b: int) -> list:
    """
    Write a recursive function that applies the following operations.

    i) If a = 0 or b = 0, return [a,b]. Otherwise, go to step (ii);
    ii) If a >= 2*b, set a = a - 2*b, and repeat step (i). Otherwise, go to step (iii);
    iii) If b >= 2*a, set b = b - 2*a, and repeat step (i). Otherwise, return [a,b].

    quic_mafs(6, 19) -> [6, 7]
    quic_mafs(2, 1) -> [0, 1]
    quic_mafs(22, 5) -> [0, 1]
    quic_mafs(8796203,7556) -> [1019,1442]

    :param a: int
    :param b: int
    :return: result
    """
    if a == 0 or b == 0:
        return [a, b]
    if a >= 2 * b:
        return quic_mafs(a - 2 * b, b)
    if b >= 2 * a:
        return quic_mafs(a, b - 2 * a)
    return [a, b]


if __name__ == "__main__":
    print(loop_reverse("hello"))  # -> "olleh"
    print(loop_reverse(""))  # -> ""
    print(loop_reverse("123"))  # -> "321"

    print(recursive_reverse("hello"))  # -> "olleh"
    print(recursive_reverse(""))  # -> ""
    print(recursive_reverse("123"))  # -> "321"

    print(loop_sum(0))  # -> 0
    print(loop_sum(3))  # -> 6
    print(loop_sum(10))  # -> 55

    print(recursive_sum(0))  # -> 0
    print(recursive_sum(3))  # -> 6
    print(recursive_sum(10))  # -> 55

    print(countdown(5))  # -> [5, 4, 3, 2, 1, 0]
    print(countdown(8))  # -> [8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(countdown(-1))  # -> []

    print(add_commas(1245))  # -> '1,245'
    print(add_commas(123456789))  # -> '123,456,789'
    print(add_commas(1011))  # -> '1,011'
    print(add_commas(1238125120581235943205123))

    print(sum_digits_recursive(123))  # -> 6
    print(sum_digits_recursive(0))  # -> 0
    print(sum_digits_recursive(1000000000000000))  # -> 1

    print(pair_star_recursive("abc"))  # -> "abc"
    print(pair_star_recursive("aaa"))  # -> a*a*a
    print(pair_star_recursive(""))  # -> ""

    print(stonks(1000, 10, 10))  # -> 2593
    print(stonks(100000, 12, 3))  # -> 140492

    print(quic_mafs(6, 19))  # -> [6, 7]
    print(quic_mafs(2, 1))  # -> [0, 1]
    print(quic_mafs(22, 5))  # -> [0, 1]
    print(quic_mafs(8796203, 7556))  # -> [1019,1442]
