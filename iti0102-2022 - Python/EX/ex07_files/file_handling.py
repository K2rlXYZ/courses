"""EX07 Files."""
import re
from datetime import datetime
import datetime as dt
from os import listdir


def read_file_contents(filename: str) -> str:
    """
    Read file contents into string.

    In this exercise, we can assume the file exists.

    :param filename: File to read.
    :return: File contents as string.
    """
    with open(filename, "r", encoding="UTF-8") as file:
        text = file.read()
        return text


def read_file_contents_to_list(filename: str) -> list:
    r"""
    Read file contents into list of lines.

    In this exercise, we can assume the file exists.
    Each line from the file should be a separate element.
    The order of the list should be the same as in the file.

    List elements should not contain new line (\n).

    :param filename: File to read.
    :return: List of lines.
    """
    var = read_file_contents(filename).split("\n")
    if var == ['']:
        return []
    return var


def read_csv_file(filename: str) -> list:
    """
    Read CSV file into list of rows.

    Each row is also a list of "columns" or fields.

    CSV (Comma-separated values) example:
    name,age
    john,12
    mary,14

    Should become:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Use csv module.

    :param filename: File to read.
    :return: List of lists.
    """
    var = read_file_contents_to_list(filename)
    if not var:
        return []
    return [x.split(",") for x in var]


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to file.

    If the file does not exist, create it.

    :param filename: File to write to.
    :param contents: Content to write to.
    :return: None
    """
    with open(filename, "w", encoding="UTF-8") as file:
        file.write(contents)


def write_lines_to_file(filename: str, lines: list) -> None:
    """
    Write lines to file.

    Lines is a list of strings, each represents a separate line in the file.

    There should be no new line in the end of the file.
    Unless the last element itself ends with the new line.

    :param filename: File to write to.
    :param lines: List of string to write to the file.
    :return: None
    """
    write_contents_to_file(filename, "\n".join(lines))


def write_csv_file(filename: str, data: list) -> None:
    """
    Write data into CSV file.

    Data is a list of lists.
    List represents lines.
    Each element (which is list itself) represents columns in a line.

    [["name", "age"], ["john", "11"], ["mary", "15"]]
    Will result in csv file:

    name,age
    john,11
    mary,15

    Use csv module here.

    :param filename: Name of the file.
    :param data: List of lists to write to the file.
    :return: None
    """
    write_contents_to_file(filename, "".join([x + "\n" for x in [",".join(x) for x in data]]))


def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    """
    Merge information from two files into one CSV file.

    Dates file contains names and dates. Separated by colon.
    john:01.01.2001
    mary:06.03.2016

    You don't have to validate the date.
    Every line contains name, colon and date.

    Towns file contains names and towns. Separated by colon.
    john:london
    mary:new york

    Every line contains name, colon and town name.
    There are no headers in the input files.

    Those two files should be merged by names.
    The result should be a csv file:

    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be "-" in the output file.

    The order of the lines should follow the order in dates input file.
    Names which are missing in dates input file, will follow the order
    in towns input file.
    The order of the fields is: name,town,date

    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Hint: try to reuse csv reading and writing functions.
    When reading csv, delimiter can be specified.

    :param dates_filename: Input file with names and dates.
    :param towns_filename: Input file with names and towns.
    :param csv_output_filename: Output CSV-file with names, towns and dates.
    :return: None
    """
    with open(dates_filename, "r", encoding="UTF-8") as dates_file:
        with open(towns_filename, "r", encoding="UTF-8") as towns_file:
            with open(csv_output_filename, "w", encoding="UTF-8") as output_file:
                dates = dates_file.read().split("\n")
                towns = towns_file.read().split("\n")

                dic = {}
                for x in dates:
                    date_list = x.split(":")
                    if date_list[0] not in dic.keys():
                        dic[date_list[0]] = ["-", date_list[1]]
                for x in towns:
                    town = x.split(":")
                    if town[0] not in dic.keys():
                        dic[town[0]] = [town[1], "-"]
                    else:
                        dic[town[0]][0] = town[1]

                text = "name,town,date\n"
                for key in dic.keys():
                    temp = f"{key},{dic[key][0]},{dic[key][1]}\n"
                    text += temp
                text = text.strip()

                output_file.write(text)


def check_if_num(lst: list):
    """Check if row in dict list is numerical."""
    for key in lst[0].keys():
        all_num = True
        for dic in lst:
            val = dic[key]
            if val is not None and not val.isnumeric():
                all_num = False
        if all_num:
            for dic in lst:
                if dic[key] is not None:
                    dic[key] = int(dic[key])


def check_if_date(lst):
    """Check if row in dict list is all dates."""
    for key in lst[0].keys():
        all_date = True
        for dic in lst:
            val = dic[key]
            if val is not None and not is_date(val):
                all_date = False
        if all_date:
            for dic in lst:
                if dic[key] is not None:
                    dic[key] = is_date(dic[key])


def read_csv_file_into_list_of_dicts(filename: str, consider_datatypes: bool = False) -> list:
    """
    Read csv file into list of dictionaries.

    Header line will be used for dict keys.
    Each line after header line will result in a dict inside the result list.
    Every line contains the same number of fields.

    Example:
    name,age,sex
    John,12,M
    Mary,13,F

    Header line will be used as keys for each content line.
    The result:
    [
      {"name": "John", "age": "12", "sex": "M"},
      {"name": "Mary", "age": "13", "sex": "F"},
    ]

    If there are only header or no rows in the CSV-file,
    the result is an empty list.

    The order of the elements in the list should be the same
    as the lines in the file (the first line becomes the first element etc.)

    :param filename: CSV-file to read.
    :return: List of dictionaries where keys are taken from the header.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        first_line = file.readline()
        if first_line == '':
            return []
        keys = [x.strip() for x in first_line.split(",")]
        lst = []
        for line in file.read().strip().split("\n"):
            if line == '':
                continue
            line = line.split(",")
            dic = {}
            for key in keys:
                dic[key] = line[keys.index(key)]
            lst.append(dic)
        if not lst:
            return []
        if consider_datatypes:
            for dic in lst:
                for key in dic.keys():
                    if dic[key] == '-':
                        dic[key] = None
            check_if_num(lst)
            check_if_date(lst)
        return lst


def get_keys_from_list_of_dicts(lst: list):
    """Return list of all keys from a list of dictionaries."""
    keys = []
    for dat in lst:
        for key in dat.keys():
            if key not in keys:
                keys.append(key)
    return keys


def write_list_of_dicts_to_csv_file(filename: str, data: list, null_value="") -> None:
    """
    Write list of dicts into csv file.

    Data contains a list of dictionaries.
    Dictionary key represents the field.

    Example data:
    [
      {"name": "john", "age": "23"}
      {"name": "mary", "age": "44"}
    ]
    Will become:
    name,age
    john,23
    mary,44

    The order of fields/headers is not important.
    The order of lines is important (the same as in the list).

    Example:
    [
      {"name": "john", "age": "12"},
      {"name": "mary", "town": "London"}
    ]
    Will become:
    name,age,town
    john,12,
    mary,,London

    Fields which are not present in one line will be empty.

    The order of the lines in the file should be the same
    as the order of elements in the list.

    :param filename: File to write to.
    :param data: List of dictionaries to write to the file.
    :return: None
    """
    with open(filename, 'w', encoding="utf-8") as file:
        if not data:
            return
        file.write(",".join(get_keys_from_list_of_dicts(data)) + "\n")
        for dic in data:
            line = ''
            for key in get_keys_from_list_of_dicts(data):
                added = False
                for value in dic.items():
                    if value[0] == key and value[1] is not None:
                        added = True
                        if isinstance(value[1], dt.date):
                            line += f"{value[1].strftime('%d.%m.%Y')},"
                            continue
                        line += f"{value[1]},"
                if not added:
                    line += f"{null_value},"
            line = line[:-1] + "\n"
            file.write(line)


def is_date(date_str: str):
    """
    Return date if it is a valid date.

    :param date_str: string of date
    :return: bool or date
    """
    try:
        date_str = re.sub('[-.:/]', ".", date_str)
        return datetime.strptime(date_str.strip(), "%d.%m.%Y").date()
    except ValueError:
        return False
    except TypeError:
        return False


def read_csv_file_into_list_of_dicts_using_datatypes(filename: str) -> list:
    """
    Read data from file and cast values into different datatypes.

    If a field contains only numbers, turn this into int.
    If a field contains only dates (in format dd.mm.yyyy), turn this into date.
    Otherwise the datatype is string (default by csv reader).

    Example:
    name,age
    john,11
    mary,14

    Becomes ('age' is int):
    [
      {'name': 'john', 'age': 11},
      {'name': 'mary', 'age': 14}
    ]

    But if all the fields cannot be cast to int, the field is left to string.
    Example:
    name,age
    john,11
    mary,14
    ago,unknown

    Becomes ('age' cannot be cast to int because of "ago"):
    [
      {'name': 'john', 'age': '11'},
      {'name': 'mary', 'age': '14'},
      {'name': 'ago', 'age': 'unknown'}
    ]

    Example:
    name,date
    john,01.01.2020
    mary,07.09.2021

    Becomes:
    [
      {'name': 'john', 'date': datetime.date(2020, 1, 1)},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    Example:
    name,date
    john,01.01.2020
    mary,late 2021

    Becomes:
    [
      {'name': 'john', 'date': "01.01.2020"},
      {'name': 'mary', 'date': "late 2021"},
    ]

    Value "-" indicates missing value and should be None in the result
    Example:
    name,date
    john,-
    mary,07.09.2021

    Becomes:
    [
      {'name': 'john', 'date': None},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    None value also doesn't affect the data type
    (the column will have the type based on the existing values).

    The order of the elements in the list should be the same
    as the lines in the file.

    For date, strptime can be used:
    https://docs.python.org/3/library/datetime.html#examples-of-usage-date
    """
    return read_csv_file_into_list_of_dicts(filename, True)


def read_people_data(directory: str) -> dict:
    """
    Read people data from files.

    Files are inside directory. Read all *.csv files.
    Each file has an int field "id" which should be used to merge information.

    The result should be one dict where the key is id (int) and value is
    a dict of all the different values across the the files.
    Missing keys should be in every dictionary.
    Missing value is represented as None.

    File: a.csv
    id,name
    1,john
    2,mary
    3,john

    File: births.csv
    id,birth
    1,01.01.2001
    2,05.06.1990

    File: deaths.csv
    id,death
    2,01.02.2020
    1,-

    Becomes:
    {
        1: {"id": 1, "name": "john", "birth": datetime.date(2001, 1, 1), "death": None},
        2: {"id": 2, "name": "mary", "birth": datetime.date(1990, 6, 5),
            "death": datetime.date(2020, 2, 1)},
        3: {"id": 3, "name": "john", "birth": None, "death": None},
    }


    :param directory: Directory where the csv files are.
    :return: Dictionary with id as keys and data dictionaries as values.
    """
    files = [x for x in listdir(directory) if x.endswith(".csv")]
    data = [read_csv_file_into_list_of_dicts_using_datatypes(directory + r'/' + x) for x in files]
    people = {}
    for file_data in data:
        for temp_dic in file_data:
            if temp_dic["id"] not in people.keys():
                people[temp_dic["id"]] = {}
            for key in temp_dic.keys():
                if key != "id":
                    people[temp_dic["id"]][key] = temp_dic[key]

    temp_people = people.copy()
    people = {}
    for key, val in temp_people.items():
        new_val = {"id": key}
        for key2 in val.keys():
            new_val[key2] = val[key2]
        people[key] = new_val

    return people


def fill_empty_squares_with_none(dic: dict):
    """Based on keys in dicts if a key isn't in a dictionary then fill it with None."""
    all_keys = get_keys_from_list_of_dicts(list(dic.values()))
    for person_id in dic.keys():
        for key1 in all_keys:
            if key1 not in dic[person_id].keys():
                dic[person_id][key1] = None
    return dic


def sort_report(people: list):
    """Sort list of people based on age(inc), birth(dec), name(inc) and then id(inc)."""
    people = sorted(people, key=lambda item: item["id"])

    names = [False if "name" not in x.keys() else True for x in people]
    names = False if True not in names else True
    if names:
        nameless_people = [x for x in people if x["name"] is None]
        people = [x for x in people if x["name"] is not None]
        people = sorted(people, key=lambda item: item["name"])
        people = people + nameless_people

    birthless_people = [x for x in people if x["birth"] is None]
    people = [x for x in people if x["birth"] is not None]
    people = sorted(people, key=lambda item: item["birth"], reverse=True)
    people = people + birthless_people

    ages = [False if "age" not in x.keys() else True for x in people]
    ages = False if True not in ages else True
    if ages:
        ageless_people = [x for x in people if x["age"] == -1]
        people = [x for x in people if x["age"] != -1]
        people = sorted(people, key=lambda item: item["age"])
        people = people + ageless_people

    return people


def generate_people_report(person_data_directory: str, report_filename: str) -> None:
    """
    Generate report about people data.

    Data should be read using read_people_data().

    The input files contain fields "birth" and "death" which are dates. Those can be in different files. There are no duplicate headers in the files (except for the "id").

    The report is a CSV file where all the fields are written to
    (along with the headers).
    In addition, there should be two fields:
    - "status" this is either "dead" or "alive" depending on whether
    there is a death date
    - "age" - current age or the age when dying.
    The age is calculated as full years.
    Birth 01.01.1940, death 01.01.2020 - age: 80
    Birth 02.01.1940, death 01.01.2020 - age: 79

    If there is no birth date, then the age is -1.

    When calculating age, dates can be compared.

    The lines in the files should be ordered:
    - first by the age ascending (younger before older);
      if the age cannot be calculated, then those lines will come last
    - if the age is the same, then those lines should be ordered
      by birthdate descending (newer birth before older birth)
    - if both the age and birth date are the same,
      then by name ascending (a before b). If name is not available, use "" (people with missing name should be before people with  name)
    - if the names are the same or name field is missing,
      order by id ascending.

    Dates in the report should in the format: dd.mm.yyyy
    (2-digit day, 2-digit month, 4-digit year).

    :param person_data_directory: Directory of input data.
    :param report_filename: Output file.
    :return: None
    """
    people = read_people_data(person_data_directory)
    people = fill_empty_squares_with_none(people)

    temp_people = people.copy()
    for _, val in temp_people.items():
        val["status"] = "alive"
        if "birth" in val.keys():
            if "death" in val.keys() and val["death"] is not None and val["birth"] is not None:
                val["status"] = "dead"
                age = int(val["death"].year) - int(val["birth"].year) - 1
                birthday = dt.date(val["death"].year, val["birth"].month, val["birth"].day)
                if birthday <= val["death"]:
                    age += 1
                val["age"] = age
            elif "birth" in val.keys() and val["birth"] is not None:
                age = int(datetime.now().year) - int(val["birth"].year) - 1
                birthday = dt.date(datetime.now().year, val["birth"].month, val["birth"].day)
                if birthday <= datetime.now().date():
                    age += 1
                val["age"] = age
        if "age" not in val.keys():
            val["age"] = -1

    people = sort_report(list(people.values()))

    write_list_of_dicts_to_csv_file(report_filename, people, "-")


if __name__ == '__main__':
    # [print(x) for x in read_people_data(r"C:\Users\Karl\PycharmProjects\iti0102-2022\EX\ex07_files")]
    generate_people_report(r"C:\Users\Karl\PycharmProjects\iti0102-2022\EX\ex07_files", "out.csv")
    # [print(x) for x in [{'id': '1', 'name': 'tere', 'int2date': None, 'date2int': None, 'date': '06.09.2021'}, {'id': None, 'name': 'tere2', 'int2date': '2', 'date2int': '02.02.2021', 'date': None}, {'id': None, 'name': 'tere3', 'int2date': None, 'date2int': '3', 'date': '06.09.2021'}, {'id': '4', 'name': None, 'int2date': '02.02.2021', 'date2int': None, 'date': '06.09.2021'}]]
    # [print(x) for x in [{'id': 1, 'name': 'tere', 'int2date': None, 'date2int': None, 'date': datetime.date(2021, 9, 6)}, {'id': None, 'name': 'tere2', 'int2date': '2', 'date2int': '02.02.2021', 'date': None}, {'id': None, 'name': 'tere3', 'int2date': None, 'date2int': '3', 'date': datetime.date(2021, 9, 6)}, {'id': 4, 'name': None, 'int2date': '02.02.2021', 'date2int': None, 'date': datetime.date(2021, 9, 6)}]]
