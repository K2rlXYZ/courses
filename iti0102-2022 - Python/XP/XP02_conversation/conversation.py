"""Conversation."""
import re
import math


class Student:
    """Student class which interacts with the server."""

    def __init__(self, biggest_number: int):
        """
        Constructor.

        save biggest number into a variable that is attainable later on.
        Create a collection of all possible results [possible_answers] <- don't rename that (can be a list or a set)
        :param biggest_number: biggest possible number(inclusive) to guess
        NB: calculating using sets is much faster compared to lists
        """
        self.biggest_number = biggest_number
        self.possible_answers = set([all_possible_answers for all_possible_answers in range(biggest_number + 1)])

    def decision_branch(self, sentence: str):
        """
        Regex can and should be used here.

        :param sentence: sentence to solve
        call one of the functions bellow (within this class) and return either one of the following strings:
        f"Possible answers are {sorted_list_of_possible_answers_in_growing_sequence)}." if there are multiple
        possibilities
        f"The number I needed to guess was {final_answer}." if the result is certain
        """
        if len(self.possible_answers) == 1:
            return f"The number I needed to guess was {list(self.possible_answers)[0]}."
        else:
            return f"Possible answers are {sorted(self.possible_answers)}."

    def intersect_possible_answers(self, update: list):
        """
        Logical AND between two sets.

        :param update: new list to be put into conjunction with self.possible_answers
        conjunction between self.possible_answers and update
        https://en.wikipedia.org/wiki/Logical_conjunction
        """
        return self.possible_answers.union(set(update))

    def exclude_possible_answers(self, update: list):
        """
        Logical SUBTRACTION between two sets.

        :param update: new list to be excluded from self.possible_answers
        update excluded from self.possible_answers
        """
        return self.possible_answers - (set(update))

    def deal_with_number_of_zeroes(self, amount_of_zeroes: int):
        """
        Filter possible_answers to match the amount of zeroes in its binary form.

        :param amount_of_zeroes: number of zeroes in the correct number's binary form
        """
        pass

    def deal_with_number_of_ones(self, amount_of_ones: int):
        """
        Filter possible answers to match the amount of ones in its binary form.

        :param amount_of_ones: number of zeroes in the correct number's binary form
        """
        pass

    def deal_with_primes(self, is_prime: bool):
        """
        Filter possible answers to either keep or remove all primes.

        Call find_primes_in_range to get all composite numbers in range.
        :param is_prime: boolean whether the number is prime or not
        """
        primes = find_primes_in_range(self.biggest_number)
        if is_prime:
            self.possible_answers = self.possible_answers & primes
        else:
            self.possible_answers = self.possible_answers - primes

    def deal_with_composites(self, is_composite: bool):
        """
        Filter possible answers to either keep or remove all composites.

        Call find_composites_in_range to get all composite numbers in range.
        :param is_composite: boolean whether the number is composite or not
        """
        composites = find_composites_in_range(self.biggest_number)
        if is_composite:
            self.possible_answers = self.possible_answers & composites
        else:
            self.possible_answers = self.possible_answers - composites

    def deal_with_dec_value(self, decimal_value: str):
        """
        Filter possible answers to remove all numbers that doesn't have the decimal_value in them.

        :param decimal_value: decimal value within the number like 9 in 192
        """
        numbers = set()
        for number in list(self.possible_answers):
            if decimal_value in str(number):
                numbers.add(number)
        self.possible_answers = numbers

    def deal_with_hex_value(self, hex_value: str):
        """
        Filter possible answers to remove all numbers that doesn't have the decimal_value in them.

        :param hex_value: hex value within the number like e in fe2
        """
        numbers = set()
        for number in list(self.possible_answers):
            if hex_value in hex(number):
                numbers.add(number)
        self.possible_answers = numbers

    def deal_with_quadratic_equation(self, equation: str, to_multiply: bool, multiplicative: float, is_bigger: bool):
        """
        Filter possible answers to remove all numbers that doesn't have the decimal_value in them.

        Regex can be used here.
        Call quadratic_equation_solver with variables a, b, c.
        deal_with_dec_value should be called.
        :param equation: the quadratic equation
        :param to_multiply: whether it is necessary to multiply or divide with a given multiplicative
        :param multiplicative: the multiplicative to multiply or divide with
        :param is_bigger: to use the bigger or smaller result of the quadratic equation(min or max from [x1, x2])
        """
        pass

    def deal_with_fibonacci_sequence(self, is_in: bool):
        """
        Filter possible answers to either keep or remove all fibonacci numbers.

        Call find_fibonacci_numbers to get all fibonacci numbers in range.
        :param is_in: boolean whether the number is in fibonacci sequence or not
        """
        fib = find_fibonacci_numbers(self.biggest_number)
        if is_in:
            self.possible_answers = self.possible_answers & fib
        else:
            self.possible_answers = self.possible_answers - fib

    def deal_with_catalan_sequence(self, is_in: bool):
        """
        Filter possible answers to either keep or remove all catalan numbers.

        Call find_catalan_numbers to get all catalan numbers in range.
        :param is_in: boolean whether the number is in catalan sequence or not
        """
        catalan = find_catalan_numbers(self.biggest_number)
        if is_in:
            self.possible_answers = self.possible_answers & catalan
        else:
            self.possible_answers = self.possible_answers - catalan

    def deal_with_number_order(self, increasing: bool, to_be: bool):
        """
        Filter possible answers to either keep or remove all numbers with wrong order.

        :param increasing: boolean whether to check is in increasing or decreasing order
        :param to_be: boolean whether the number is indeed in that order
        """
        pass


def normalize_quadratic_equation(equation: str):
    """
    Normalize the quadratic equation.

    normalize_quadratic_equation("x2 + 2x = 3") => "x2 + 2x - 3 = 0"
    normalize_quadratic_equation("0 = 3 + 1x2") => "x2 + 3 = 0"
    normalize_quadratic_equation("2x + 2 = 2x2") => "2x2 - 2x - 2 = 0"
    normalize_quadratic_equation("0x2 - 2x = 1") => "2x + 1 = 0"
    normalize_quadratic_equation("0x2 - 2x = 1") => "2x + 1 = 0"
    normalize_quadratic_equation("2x2 + 3x - 4 + 0x2 - x1 + 0x1 + 12 - 12x2 = 4x2 + x1 - 2") => "14x2 - x - 10 = 0"

    :param equation: quadratic equation to be normalized
    https://en.wikipedia.org/wiki/Quadratic_formula
    :return: normalized equation
    """
    equation = " " + equation + " "
    equation = equation.split("=")
    left_quad = re.findall(regex_a, equation[0])
    left_linear = re.findall(regex_b, equation[0])
    left_constant = re.findall(regex_c, equation[0])
    right_quad = re.findall(regex_a, equation[1])
    right_linear = re.findall(regex_b, equation[1])
    right_constant = re.findall(regex_c, equation[1])

    quad = 0
    linear = 0
    constant = 0

    for x in left_quad:
        if x[0] != '':
            quad += int(x[0].replace(" ", ""))
            break
        else:
            quad += 1
    for x in right_quad:
        if x[0] != '':
            quad -= int(x[0].replace(" ", ""))
            break
        else:
            quad -= 1

    for x in left_linear:
        if x[0] != '':
            linear += int(x[0].replace(" ", ""))
            break
        else:
            linear += 1
    for x in right_linear:
        if x[0] != '':
            linear -= int(x[0].replace(" ", ""))
            break
        else:
            linear -= 1

    for x in left_constant:
        if x[0] != '':
            constant += int(x[0].replace(" ", ""))
            break
        else:
            constant += 1
    for x in right_constant:
        if x[0] != '':
            constant -= int(x[0].replace(" ", ""))
            break
        else:
            constant -= 1

    if quad < 0 or quad == 0 and linear < 0:
        quad = -quad
        linear = -linear
        constant = -constant

    constant = f"{'+' if constant > 0 else ''}{constant if constant != 0 else ''}"
    linear = f"{'+' if linear > 0 and quad != 0 and linear != 0 else ''}{linear if linear != 1 and linear != 0 else ''}{'x' if linear != 0 else ''}"
    quad = f"{quad if quad != 1 and quad != 0 else ''}{'x2' if quad != 0 else ''}"

    return f"{quad}{linear}{constant}=0"

regex_a = r'((- \d*)|(\d*))(?:x2) '
regex_b = r' ((- \d*)|(\d*))(?:x) '
regex_c = r' ((- \d*)|(\d*)) '


def quadratic_equation_solver(equation: str):
    """
    Solve the normalized quadratic equation.
    x2 + 2x - 3 = 0
    :param equation: quadratic equation
    https://en.wikipedia.org/wiki/Quadratic_formula
    :return:
    if there are no solutions, return None.
    if there is exactly 1 solution, return it.
    if there are 2 solutions, return them in a tuple, where smaller is first
    all numbers are returned as floats.
    """
    equation += " "
    quad_coefficient = re.search(regex_a, equation)
    linear_coefficient = re.search(regex_b, equation)
    constant_coefficient = re.search(regex_c, equation)

    temp = [quad_coefficient,
            linear_coefficient,
            constant_coefficient]
    [print(x.group(0)) for x in temp]
    temp = [0 if x is None
            else
            1 if x.group(1) == ''
            else
            -1 if x.group(1) == '- '
            else
            int(x.group(1).replace(" ", ""))
            for x in temp]
    print(temp)
    equation = temp

    if equation[0] == 0:
        return -equation[2] / equation[1]
    # Quadratic formula x1,2 = (-b+-(sqrt(b**2-4ac)))/(2a)
    if equation[1] ** 2 - 4 * equation[0] * equation[2] < 0:
        return None
    d = (equation[1] ** 2 - 4 * equation[0] * equation[2])
    x1 = (-equation[1] + (math.sqrt(d))) / (2 * equation[0])
    x2 = (-equation[1] - (math.sqrt(d))) / (2 * equation[0])
    return (min(x1, x2), max(x1, x2))


def find_primes_in_range(biggest_number: int):
    """
    Find all primes in range(end inclusive).

    :param biggest_number: all primes in range of biggest_number(included)
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    :return: list of primes
    """
    primes = []
    biggest_number += 1
    a = [True for _ in range(0, biggest_number)]
    for i in range(2, biggest_number):
        if i < math.sqrt(biggest_number):
            if a[i]:
                for j in range(0, biggest_number):
                    if i ** 2 + j * i < biggest_number:
                        a[i ** 2 + j * i] = False
                    else:
                        break
        else:
            break
    for i in range(2, biggest_number):
        if a[i]:
            primes.append(i)
    return primes


def find_composites_in_range(biggest_number: int):
    """
    Find all composites in range(end inclusive).

    Call find_primes_in_range from this method to get all composites
    :return: list of composites
    :param biggest_number: all composites in range of biggest_number(included)
    """
    primes = find_primes_in_range(biggest_number)
    composites = []
    for i in primes:
        for j in primes:
            if i * j <= biggest_number and i * j not in composites:
                composites.append(i * j)
            elif i * j > biggest_number:
                break
    return composites


def find_fibonacci_numbers(biggest_number: int):
    """
    Find all Fibonacci numbers in range(end inclusive).

    Can be solved using recursion.
    :param biggest_number: all fibonacci numbers in range of biggest_number(included)
    https://en.wikipedia.org/wiki/Fibonacci_number
    :return: list of fibonacci numbers
    """
    fib = [1, 1]
    while fib[-1] + fib[-2] < biggest_number:
        fib.append(fib[-1] + fib[-2])
    return fib


def find_catalan_numbers(biggest_number: int):
    """
    Find all Catalan numbers in range(end inclusive).

    Can be solved using recursion.
    :param biggest_number: all catalan numbers in range of biggest_number(included)
    https://en.wikipedia.org/wiki/Catalan_number
    :return: list of catalan numbers
    """
    catalans = []
    n = 1
    last_catalan = 1
    while last_catalan <= biggest_number:
        catalans.append(int(last_catalan))
        last_catalan = (math.factorial(2 * n)) / (math.factorial(n + 1) * math.factorial(n))
        n += 1

    return catalans


if __name__ == '__main__':
    def print_regex_results(regex, f):
        for match in re.finditer(regex, f):
            print(match.group(1))


    f = "3x2 - 4x + 1 = 0"

    print_regex_results(regex_a, f)  # 3
    print_regex_results(regex_b, f)  # - 4
    print_regex_results(regex_c, f)  # 1

    f2 = "3x2 + 4x + 5 - 2x2 - 7x + 4 "

    print("x2")
    print_regex_results(regex_a, f2)  # 3, - 2
    print("x")
    print_regex_results(regex_b, f2)  # 4, - 7
    print("c")
    print_regex_results(regex_c, f2)  # 5, 4
    print(normalize_quadratic_equation("x2 + 2x = 3"))  # = > "x2 + 2x - 3 = 0"
    print(normalize_quadratic_equation("0 = 3 + 1x2"))  # = > "x2 + 3 = 0"
    print(normalize_quadratic_equation("2x + 2 = 2x2"))  # = > "2x2 - 2x - 2 = 0"
    print(normalize_quadratic_equation("0x2 - 2x = 1"))  # = > "2x + 1 = 0"
    print(normalize_quadratic_equation("0x2 - 2x = 1"))  # = > "2x + 1 = 0"
    print(normalize_quadratic_equation("2x2 + 3x - 4 + 0x2 - x1 + 0x1 + 12 - 12x2 = 4x2 + x1 - 2"))
    # = > "14x2 - x - 10 = 0"
