"""KT4."""


def two_digits_into_list(nr: int) -> list:
    """
    Return list of digits of 2-digit number.

    two_digits_into_list(11) => [1, 1]
    two_digits_into_list(71) => [7, 1]

    :param nr: 2-digit number
    :return: list of length 2
    """
    return list([int(x) for x in list(str(nr))])


def sum_elements_around_last_three(nums: list) -> int:
    """
    Find sum of elements before and after last 3 in the list.

    If there is no 3 in the list or list is too short
    or there is no element before or after last 3 return 0.

    Note if 3 is last element in the list you must return
    sum of elements before and after 3 which is before last.


    sum_elements_around_last_three([1, 3, 7]) -> 8
    sum_elements_around_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 4, 5, 6]) -> 9
    sum_elements_around_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 3, 2, 3]) -> 5
    sum_elements_around_last_three([1, 2, 3]) -> 0

    :param nums: given list of ints
    :return: sum of elements before and after last 3
    """
    nums.reverse()
    if len(nums) == 2:
        return 0
    for n, x in enumerate(nums):
        if len(nums) == n + 1:
            break
        if n == 0 and x == 3:
            continue
        if x == 3:
            return nums[n - 1] + nums[n + 1]
    return 0


def max_block(s: str) -> int:
    """
    Given a string, return the length of the largest "block" in the string.

    A block is a run of adjacent chars that are the same.

    max_block("hoopla") => 2
    max_block("abbCCCddBBBxx") => 3
    max_block("") => 0
    """
    if s == "":
        return 0
    blocks = []
    start_of_block = 0
    for n, x in enumerate(s):
        if len(s) == n + 1:
            blocks.append(s[start_of_block:n + 1])
            break
        if s[n + 1] != x:
            blocks.append(s[start_of_block:n + 1])
            start_of_block = n + 1
    return max([len(x) for x in blocks])


def create_dictionary_from_directed_string_pairs(pairs: list) -> dict:
    """
    Create dictionary from directed string pairs.

    One pair consists of two strings and "direction" symbol ("<" or ">").
    The key is the string which is on the "larger" side,
    the value is the string which is on the "smaller" side.

    For example:
    ab>cd => "ab" is the key, "cd" is the value
    kl<mn => "mn" is the key, "kl" is the value

    The input consists of list of such strings.
    The output is a dictionary, where values are lists.
    Each key cannot contain duplicate elements.
    The order of the elements in the values should be
    the same as they appear in the input list.

    create_dictionary_from_directed_string_pairs([]) => {}

    create_dictionary_from_directed_string_pairs(["a>b", "a>c"]) =>
    {"a": ["b", "c"]}

    create_dictionary_from_directed_string_pairs(["a>b", "a<b"]) =>
    {"a": ["b"], "b": ["a"]}

    create_dictionary_from_directed_string_pairs(["1>1", "1>2", "1>1"]) =>
    {"1": ["1", "2"]}
    """
    if not pairs:
        return {}
    dict = {}
    for pair in pairs:
        if ">" in pair:
            temp = pair.split(">")
            if temp[0] not in dict.keys():
                dict[temp[0]] = []
            dict[temp[0]].append(temp[1]) if temp[1] not in dict[temp[0]] else 0
        elif "<" in pair:
            temp = pair.split("<")
            if temp[1] not in dict.keys():
                dict[temp[1]] = []
            dict[temp[1]].append(temp[0]) if temp[0] not in dict[temp[1]] else 0
    return dict


if __name__ == '__main__':
    print(two_digits_into_list(22))
    print(sum_elements_around_last_three([1, 3, 7]))
    print(sum_elements_around_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 4, 5, 6]))
    print(sum_elements_around_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 3, 2, 3]))
    print(sum_elements_around_last_three([1, 2, 3]))
    print(max_block("abbCCCddBBBxx"))
    print(create_dictionary_from_directed_string_pairs(["a>b", "a<b"]))
    print(create_dictionary_from_directed_string_pairs(["1>1", "1>2", "1>1"]))
