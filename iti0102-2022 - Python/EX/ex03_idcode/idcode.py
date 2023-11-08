"""EX03 ID code."""


def find_id_code(text: str) -> str:
    """
    Find ID-code from given text.

    Given string may include any number of numbers, characters and other symbols mixed together.
    The numbers of ID-code may be between other symbols - they must be found and concatenated.
    ID-code contains of exactly 11 numbers. If there are not enough numbers, return 'Not enough numbers!',
    if there are too many numbers, return 'Too many numbers!' If ID-code can be found, return that code.
    You don't have to validate the ID-code here. If it has 11 numbers, then it is enough for now.

    :param text: string
    :return: string
    """
    numbers = "1234567890"
    id = ""
    for symbol in text:
        if symbol in numbers:
            id += symbol
    if len(id) > 11:
        return "Too many numbers!"
    elif len(id) == 11:
        return id
    elif len(id) < 11:
        return "Not enough numbers!"
    return "Not enough numbers!"


def the_first_control_number_algorithm(text: str) -> str:
    """
    Check if given value is correct for control number in ID code only with the first algorithm.

    The first algorithm can be calculated with ID code's first 10 numbers.
    Each number must be multiplied with its corresponding digit
    (in this task, corresponding digits are: 1 2 3 4 5 6 7 8 9 1), after which all the values are summarized
    and divided by 11. The remainder of calculation should be the control number.

    If the remainder is less than 10 and equal to the last number of ID code,
    then that's the correct control number and the function should return the ID code.
    Otherwise, the control number is either incorrect or the second algorithm should be used.
    In this case, return "Needs the second algorithm!".

    If the string contains more or less than 11 numbers, return "Incorrect ID code!".
    In other case use the previous algorithm to get the code number out of the string
    and find out, whether its control number is correct.

    :param text: string
    :return: string
    """
    id = find_id_code(text)
    if not id.isnumeric() or id == "":
        return "Incorrect ID code!"
    sum = 0
    for x in range(10):
        sum += ((x % 9) + 1) * int(id[x])
    if sum % 11 == int(id[-1]):
        return id
    elif sum % 11 >= 10:
        return "Needs the second algorithm!"
    return "Incorrect ID code!"


def the_second_control_number_algorithm(text: str) -> str:
    """
    Check if given value is correct for control number in ID code with the algorithm.

    :param text: string
    :return: string
    """
    id = find_id_code(text)
    if not id.isnumeric() or id == "":
        return "Incorrect ID code!"
    sum = 0
    for x in range(10):
        sum += (((x + 2) % 9) + 1) * int(id[x])
    if sum % 11 == int(id[-1]):
        return id
    elif sum % 11 >= 10:
        if int(id[-1]) == 0:
            return id
        else:
            return "Incorrect ID code!"
    return "Incorrect ID code!"


def is_valid_year_number(year_number: int) -> bool:
    """Check if given value is correct for year number in ID code."""
    if year_number > 99 or year_number < 0:
        return False
    return True


def is_valid_month_number(month_number: int) -> bool:
    """Check if given value is correct for month number in ID code."""
    if month_number > 12 or month_number < 1:
        return False
    return True


def is_valid_birth_number(birth_number: int) -> bool:
    """Check if given value is correct for birth number in ID code."""
    if birth_number > 999 or birth_number < 1:
        return False
    return True


def is_valid_gender_number(gender_number: int) -> bool:
    """Check if given value is correct for gender number in ID code."""
    if gender_number > 6 or gender_number < 1:
        return False
    return True


def get_gender(gender_number: int) -> str:
    """Return the gender given an ID code."""
    if gender_number % 2 == 0:
        return "female"
    return "male"


def get_full_year(gender_number: int, year_number: int) -> int:
    """Define the 4-digit year when given person was born."""
    dic = {1: 18, 2: 18, 3: 19, 4: 19, 5: 20, 6: 20}
    if year_number < 10:
        year_number = "0" + str(year_number)
    return int(str(dic[gender_number]) + str(year_number))


def get_birth_place(birth_number: int) -> str:
    """Find the place where the person was born."""
    if not is_valid_birth_number(birth_number):
        return "Wrong input!"
    if 0 < birth_number < 11:
        return "Kuressaare"
    elif 10 < birth_number < 21:
        return "Tartu"
    elif 20 < birth_number < 221:
        return "Tallinn"
    elif 220 < birth_number < 271:
        return "Kohtla-Järve"
    elif 270 < birth_number < 371:
        return "Tartu"
    elif 370 < birth_number < 421:
        return "Narva"
    elif 420 < birth_number < 471:
        return "Pärnu"
    elif 470 < birth_number < 711:
        return "Tallinn"
    return "undefined"


def is_leap_year(year_number: int) -> bool:
    """Check if given year is a leap year or not."""
    if year_number % 400 == 0:
        return True
    elif year_number % 100 == 0:
        return False
    if year_number % 4 == 0:
        return True
    return False


def is_valid_control_number(id_code: str) -> bool:
    """Check if given value is correct for control number in ID code."""
    first_algo = the_first_control_number_algorithm(id_code)
    if len(first_algo) == 11:
        return True
    if first_algo == "Needs the second algorithm!" and len(the_second_control_number_algorithm(id_code)) == 11:
        return True
    return False


def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int) -> bool:
    """Check if given value is correct for day number in ID code."""
    if not is_valid_gender_number(gender_number):
        return False

    if not is_valid_year_number(year_number):
        return False

    if not is_valid_month_number(month_number):
        return False

    if day_number > 31 or day_number < 1:
        return False

    year = get_full_year(gender_number, year_number)
    if month_number == 2:
        if is_leap_year(year):
            if day_number > 29:
                return False
        else:
            if day_number > 28:
                return False
    if month_number in [4, 6, 9, 11] and day_number > 30:
        return False
    return True


def is_id_valid(id_code: str) -> bool:
    """Check if given ID code is valid and return the result (True or False)."""
    id_code = find_id_code(id_code)
    if not id_code.isnumeric() or id_code == "":
        return False
    if not is_valid_day_number(int(id_code[0]), int(id_code[1:3]), int(id_code[3:5]), int(id_code[5:7])):
        return False
    if not is_valid_birth_number(int(id_code[7:10])):
        return False
    if not is_valid_control_number(id_code):
        return False
    return True


def get_data_from_id(id_code: str) -> str:
    """Get possible information about the person."""
    if not is_id_valid(id_code):
        return "Given invalid ID code!"
    gender = get_gender(int(id_code[0]))
    month = int(id_code[3:5])
    if month < 10:
        month = "0" + str(month)
    day = int(id_code[5:7])
    if day < 10:
        day = "0" + str(day)
    birth_date = f"{day}.{month}.{get_full_year(int(id_code[0]), int(id_code[1:3]))}"  # DD.MM.YYYY
    location = get_birth_place(int(id_code[7:10]))
    return f"This is a {gender} born on {birth_date} in {location}."


if __name__ == '__main__':
    print(find_id_code(""))
    print(get_data_from_id(""))
    print(is_id_valid(""))
    print(the_first_control_number_algorithm(""))
    print(the_second_control_number_algorithm(""))
    print(is_valid_year_number(50302264926))
    print(is_valid_month_number(50302264926))
    print(is_valid_birth_number(50302264926))
    print(is_valid_gender_number(50302264926))
    print(get_gender(50302264926))
    print(get_full_year(2, 88))
    print(get_birth_place(444))
    print(is_leap_year(5555))
