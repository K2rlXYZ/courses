"""EX05 - Hobbies."""


def create_dictionary(data: str) -> dict:
    """
    Create dictionary about people and their hobbies ie. {name1: [hobby1, hobby2, ...], name2: [...]}.

    There should be no duplicate hobbies on 1 person.

    :param data: given string from database
    :return: dictionary where keys are people and values are lists of hobbies
    """
    final = {}
    for element in data.split("\n"):
        element = element.split(":")
        person = element[0]
        hobby = element[1]
        if person not in final.keys():
            final[person] = [hobby]
        else:
            if hobby not in final[person]:
                final[person].append(hobby)
    return final


def sort_dictionary(dic: dict) -> dict:
    """
    Sort dictionary values alphabetically.

    The order of keys is not important.

    sort_dictionary({"b":[], "a":[], "c": []})  => {"b":[], "a":[], "c": []}
    sort_dictionary({"": ["a", "f", "d"]})  => {"": ["a", "d", "f"]}
    sort_dictionary({"b":["d", "a"], "a":["c", "f"]})  => {"b":["a", "d"], "a":["c", "f"]}
    sort_dictionary({"Jack": ["swimming", "hiking"], "Charlie": ["games", "yoga"]})
        => {"Jack": ["hiking", "swimming"], "Charlie": ["games", "yoga"]}

    :param dic: dictionary to sort
    :return: sorted dictionary
    """
    for element in dic.keys():
        dic[element] = sorted(dic[element])
    return dic


def create_dictionary_with_hobbies(data: str) -> dict:
    """
    Create dictionary about hobbies and their hobbyists ie. {hobby1: [name1, name2, ...], hobby2: [...]}.

    :param data: given string from database
    :return: dictionary, where keys are hobbies and values are lists of people. Values are sorted alphabetically
    """
    final = {}
    for element in data.split("\n"):
        element = element.split(":")
        person = element[0]
        hobby = element[1]
        if hobby not in final.keys():
            final[hobby] = [person]
        else:
            if person not in final[hobby]:
                final[hobby].append(person)
    return sort_dictionary(final)


def find_people_with_most_hobbies(data: str):
    """
    Find the people who have the most hobbies.

    :param data: given string from database
    :return: list of people with most hobbies. Sorted alphabetically.
    """
    temp = create_dictionary(data)
    for element in temp.keys():
        temp[element] = len(temp[element])
    temp = sorted(temp.items(), key=lambda x: x[1], reverse=True)
    numb = temp[0][1]
    final = []
    for element in temp:
        if element[1] == numb:
            final.append(element[0])
    return sorted(final)


def find_least_popular_hobbies(data: str) -> list:
    """
    Find the least popular hobbies.

    :param data: given string from database
    :return: list of least popular hobbies. Sorted alphabetically.
    """
    temp = create_dictionary_with_hobbies(data)
    for element in temp.keys():
        temp[element] = len(temp[element])
    temp = sorted(temp.items(), key=lambda x: x[1])
    numb = temp[0][1]
    final = []
    for element in temp:
        if element[1] == numb:
            final.append(element[0])
    return sorted(final)


def sort_names_and_hobbies(data: str) -> tuple:
    """
    Create a tuple of sorted names and their hobbies.

    The structure of the tuple is as follows:
    (
        (name1, (hobby1, hobby2)),
        (name2, (hobby1, hobby2)),
         ...
    )

    For each person, there is a tuple, where the first element is the name (string)
    and the second element is an ordered tuple of hobbies (ordered alphabetically).
    All those person-tuples are ordered by the name of the person and are inside a tuple.
    """
    final = create_dictionary(data)
    final = sort_dictionary(final)
    final = sorted(final.items(), key=lambda x: x[0])
    for n, element in enumerate(final):
        final[n] = (element[0], tuple(element[1]))
    return tuple(final)


def find_people_with_hobbies(data: str, hobbies: list) -> set:
    r"""
    Find all the different people with certain hobbies.

    It is recommended to use set here.

    Example:
        data="John:running\nMary:running\nJohn:dancing\nJack:dancing\nJack:painting\nSmith:painting"
        hobbies=["running", "dancing"]
    Result:
        {"John", "Mary", "Jack"}
    """
    temp = create_dictionary(data)
    final = set()
    for name in temp.keys():
        for hobby in hobbies:
            if hobby in temp[name]:
                final.add(name)
    return final


def list_of_commonalities_and_differences(dic: dict) -> list:
    """
    Return a list containing the pairs of people, their commonalities and differences given a dictionary.

    :param dic: given dictionary
    :return: list containing the pairs of people
    """
    lst = []
    for person1 in dic.keys():
        for person2 in dic.keys():
            hobbies1 = set(dic[person1])
            hobbies2 = set(dic[person2])
            commonalities = len(hobbies1.union(hobbies2))
            differences = len((hobbies1.difference(hobbies2)).union(hobbies2.difference(hobbies1)))
            found = False
            for pair in lst:
                if pair[0] == (person1, person2) or pair[0] == (person2, person1):
                    found = True
            if not found and person1 != person2:
                if differences != 0 and commonalities != 0:
                    lst.append([(person1, person2), (commonalities / differences)])
                elif differences == 0:
                    lst.append([(person1, person2), f"c{commonalities}"])
                elif commonalities == 0:
                    lst.append([(person1, person2), f"d{differences}"])
    return lst


def find_two_people_with_most_common_hobbies(data: str) -> tuple:
    """
    Find a pair of people who have the highest ratio of common to different hobbies.

    Common hobbies are the ones that both people have.
    Different hobbies are the ones that only one person has.

    Example:
    John has:
        running
        walking
    Mary has:
        dancing
        running
    Nora has:
        running
        singing
        dancing

    Pairs and corresponding common and different hobbies; ratio
    John and Mary; common: running; diff: walking, dancing; ratio: 1/2
    John and Nora; common: running; diff: walking, singing, dancing; ratio: 1/3
    Mary and Nora; common: running, dancing; diff: singing; ratio: 2/1

    So the best result is Mary and Nora. It doesn't matter in which order the names are returned.

    If multiple pairs have the same best ratio, it doesn't matter which pair is returned.

    The exception is when multiple pairs share all of their hobbies, in which case the pair with
    the most shared hobbies is returned.

    A pair with only common hobbies is better than any other pair with at least 1 different hobby.

    Example:
    John has:
        running
        walking
    Mary has:
        running
        walking
    Nora has:
        running
    Oprah has:
        running
    Albert has:
        tennis
        basketball
        football
    Xena has:
        tennis
        basketball
        football
        dancing

    John and Mary have 2 common, 0 different. Ratio 2/0
    Nora and Mary (also Nora and John, Oprah and John, Oprah and Mary) have 1 common, 1 different. Ratio 1/1
    Nora and Oprah have 1 common, 0 different. Ratio 1/0
    Albert and Xena have 3 common, 1 different. Ratio 3/1

    In that case the best pair is John and Mary. If the number of different hobbies is 0,
    then this is better than any pair with at least 1 different hobby.
    Out of the pairs with 0 different hobbies, the one with the highest number
    of common hobbies is the best.
    If there are multiple pairs with the highes number of common hobbies,
    any pair (and in any order) is accepted.

    If there are less than 2 people in the input, return None.
    """
    lst = []
    dic = create_dictionary(data)
    if len(dic.keys()) == 1:
        return None
    lst = list_of_commonalities_and_differences(dic)
    if len(lst) == 0:
        return None

    dif0 = list(set([(x[0], int(x[1][1:])) if (type(x[1]) == str and x[1][0] == 'c') else None for x in lst]))
    if None in dif0:
        dif0.remove(None)
    dif0 = sorted(dif0, key=lambda x: x[1], reverse=True)

    com_and_dif = list(set([tuple(x) if type(x[1]) != str else None for x in lst]))
    if None in com_and_dif:
        com_and_dif.remove(None)
    com_and_dif = sorted(com_and_dif, key=lambda x: x[1], reverse=True)

    com0 = list(set([(x[0], int(x[1][1:])) if (type(x[1]) == str and x[1][0] == 'd') else None for x in lst]))
    if None in com0:
        com0.remove(None)
    com0 = sorted(com0, key=lambda x: x[1], reverse=True)

    lst = dif0 + com_and_dif + com0
    return lst[0][0]


if __name__ == '__main__':
    sample_data = """Jack:crafting\nPeter:hiking\nWendy:gaming\nMonica:tennis\nChris:origami\nSophie:sport\nMonica:design\nCarmen:sport\nChris:sport\nMonica:skateboarding\nCarmen:cooking\nWendy:photography\nMonica:tennis\nCooper:yoga\nWendy:sport\nCooper:movies\nMonica:theatre\nCooper:yoga\nChris:gaming\nMolly:fishing\nJack:skateboarding\nWendy:fishing\nJack:drawing\nMonica:baking\nSophie:baking\nAlfred:driving\nAlfred:shopping\nAlfred:crafting\nJack:drawing\nCarmen:shopping\nCarmen:driving\nPeter:drawing\nCarmen:shopping\nWendy:fitness\nAlfred:travel\nJack:origami\nSophie:design\nJack:pets\nCarmen:dance\nAlfred:baking\nSophie:sport\nPeter:gaming\nJack:skateboarding\nCooper:football\nAlfred:sport\nCooper:fitness\nChris:yoga\nWendy:football\nMolly:design\nJack:hiking\nMonica:pets\nCarmen:photography\nJack:baking\nPeter:driving\nChris:driving\nCarmen:driving\nPeter:theatre\nMolly:hiking\nWendy:puzzles\nJack:crafting\nPeter:photography\nCarmen:theatre\nSophie:crafting\nCarmen:cooking\nAlfred:gaming\nPeter:theatre\nCooper:hiking\nChris:football\nChris:pets\nJack:football\nMonica:skateboarding\nChris:driving\nCarmen:pets\nCooper:gaming\nChris:hiking\nJack:cooking\nPeter:fishing\nJack:gaming\nPeter:origami\nCarmen:movies\nSophie:driving\nJack:sport\nCarmen:theatre\nWendy:shopping\nCarmen:pets\nWendy:gaming\nSophie:football\nWendy:theatre\nCarmen:football\nMolly:theatre\nPeter:theatre\nMonica:flowers\nMolly:skateboarding\nPeter:driving\nSophie:travel\nMonica:photography\nCooper:cooking\nJack:fitness\nPeter:cooking\nChris:gaming"""

    sort_result = sort_names_and_hobbies(sample_data)
    # if the condition after assert is False, error will be thrown
    assert isinstance(sort_result, tuple)
    assert len(sort_result) == 10
    assert sort_result[0][0] == 'Alfred'
    assert len(sort_result[0][1]) == 7
    assert sort_result[-1] == (
        'Wendy', ('fishing', 'fitness', 'football', 'gaming', 'photography', 'puzzles', 'shopping', 'sport', 'theatre'))
    # if you see this line below, then everything seems to be ok!
    print("sorting works!")

    sample_data = """Jack:painting\nPeter:painting\nJack:running\nMary:running\nSmith:walking"""
    print(find_people_with_hobbies(sample_data, ["running", "painting"]))
    print(find_people_with_hobbies(
        "John:running\nMary:running\nJohn:dancing\nJack:dancing\nJack:painting\nSmith:painting",
        ["running", "dancing"]
    ))  # {"John", "Mary", "Jack"}

    sample_data = """John:running\nJohn:walking\nMary:dancing\nMary:running\nNora:running\nNora:singing\nNora:dancing"""
    print(find_two_people_with_most_common_hobbies(sample_data))  # ('Mary', 'Nora')
