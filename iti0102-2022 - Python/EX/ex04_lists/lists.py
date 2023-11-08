"""Car inventory."""


def list_of_cars(all_cars: str) -> list:
    """
    Return list of cars.

    The input string contains of car makes and models, separated by comma.
    Both the make and the model do not contain spaces (both are one word).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi A4", "Skoda Superb", "Audi A4"]
    """
    return all_cars.split(",") if all_cars.split(",") != [''] else []


def car_makes(all_cars: str) -> list:
    """
    Return list of unique car makes.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi", "Skoda"]
    """
    final = []

    for x in all_cars.split(","):
        make = x.split(" ")[0]
        if make not in final:
            final.append(make)
    return final if final != [''] else []


def car_models(all_cars: str) -> list:
    """
    Return list of unique car models.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4,Audi A6" => ["A4", "Superb", "A6"]
    """
    final = []
    for x in list_of_cars(all_cars):
        model = (" ".join(x.split(" ")[1:-1]) + " " + x.split(" ")[-1]).strip()
        if model not in final:
            final.append(model)
    return final if final != [''] else []


def search_by_make(all_cars: str, make: str) -> list:
    """Return a list of matches for given make from list of cars."""
    cars = list_of_cars(all_cars)
    matches = []
    if make == "" or len(make.split(" ")) != 1:
        return matches
    for car in cars:
        car_make = car.split(" ")[0]
        if make.lower() == car_make.lower():
            matches.append(car)

    return matches


def search_by_model(all_cars: str, model: str) -> list:
    """Return a list of matches for given model from list of cars."""
    cars = list_of_cars(all_cars)
    matches = []
    if model == "" or len(model.split(" ")) != 1:
        return matches
    for car in cars:
        car_model = (" ".join(car.split(" ")[1:-1]) + " " + car.split(" ")[-1]).strip()
        for word1 in model.lower().split(" "):
            for word2 in car_model.lower().split(" "):
                if word1 == word2:
                    matches.append(car)

    return matches


def car_make_and_models(all_cars: str, final=None) -> list:
    """
    Create a list of structured information about makes and models.

    For each different car make in the input string an element is created in the output list.
    The element itself is a list, where the first position is the name of the make (string),
    the second element is a list of models for the given make (list of strings).

    No duplicate makes or models should be in the output.

    The order of the makes and models should be the same os in the input list (first appearance).

    "Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon Lux,Skoda Superb,Skoda Superb,BMW x5" =>
    [
        ['Audi',
            ['A4']
        ],
        ['Skoda', ['Super', 'Octavia', 'Superb']],
        ['BMW', ['530', 'x5']],
        ['Seat', ['Leon Lux']]
    ]
    """
    if all_cars == "":
        return []
    if final is None:
        final = []
    for car in list_of_cars(all_cars):

        found = False
        car = car.split(" ")
        mark = car[0]
        model = (" ".join(car[1:-1]) + " " + car[-1]).strip()
        if not final:
            final.append([mark, [model]])
        for x in final:
            if x[0] == mark:
                found = True
                if model not in x[1]:
                    final[final.index(x)][1].append(model)
        if not found:
            final.append([mark, [model]])

    return final


def add_cars(car_list: list, all_cars: str) -> list:
    """
    Add cars from the list into the existing car list.

    The first parameter is in the same format as the output of the previous function.
    The second parameter is a string of comma separated cars (as in all the previous functions).
    The task is to add cars from the string into the list.

    Hint: This and car_make_and_models are very similar functions. Try to use one inside another.

    [['Audi', ['A4']], ['Skoda', ['Superb']]]
    and
    "Audi A6,BMW A B C,Audi A4"

    =>

    [['Audi', ['A4', 'A6']], ['Skoda', ['Superb']], ['BMW', ['A B C']]]
    """
    return car_make_and_models(all_cars, car_list)


def number_of_cars(all_cars: str) -> list:
    """
    Create a list of tuples with make quantities.

    The result is a list of tuples.
    Each tuple is in the form: (make_name: str, quantity: int).
    The order of the tuples (makes) is the same as the first appearance in the list.
    """
    if all_cars == "":
        return []
    final = []
    cars = list_of_cars(all_cars)
    for car in cars:
        found = False
        for tupl in final:
            if car.split(" ")[0].lower() == tupl[0].lower():
                found = True
                appension = (tupl[0], tupl[1] + 1)
                final = [(appension if t == tupl else t) for t in final]
        if not found:
            final.append((car.split(" ")[0], 1))
    return final


def car_list_as_string(cars: list) -> str:
    """
    Create a list of cars.

    The input list is in the same format as the result of car_make_and_models function.
    The order of the elements in the string is the same as in the list.
    [['Audi', ['A4']], ['Skoda', ['Superb']]] =>
    "Audi A4,Skoda Superb"
    """
    if not cars:
        return ""

    final = []
    for car in cars:
        for mark in car[1]:
            final.append(f"{car[0]} {mark}")

    return ",".join(final)


if __name__ == '__main__':
    print(number_of_cars("Audi A4,Skoda Superb,Seat Leon,Audi A6"))  # [('Audi', 2), ('Skoda', 1), ('Seat', 1)]

    print(number_of_cars("Mazda 6,Mazda 6,Mazda 6,Mazda 6"))  # [('Mazda', 4)]

    print(number_of_cars(""))  # []

    print(car_list_as_string([['Audi', ['A4', "pidar"]], ['Skoda', ['Superb']]]))  # "Audi A4,Skoda Superb"
