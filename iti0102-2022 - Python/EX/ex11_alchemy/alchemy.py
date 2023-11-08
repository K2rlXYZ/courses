"""Alchemy."""
from typing import Tuple


class AlchemicalElement:
    """
    AlchemicalElement class.

    Every element must have a namee.
    """

    def __init__(self, name: str):
        """Initialize the AlchemicalElement class."""
        self.name = name

    def __repr__(self) -> str:
        """
        Representation of the AlchemicalElement class.

        :return: String representation of the AlchemicalElement.
        """
        return f"<AE: {self.name}>"


class AlchemicalStorage:
    """AlchemicalStorage class."""

    def __init__(self):
        """
        Initialize the AlchemicalStorage class.

        You will likely need to add something here, maybe a list?
        """
        self.storage = []

    def add(self, element: AlchemicalElement):
        """
        Add element to storage.

        Check that the element is an instance of AlchemicalElement, if it is not, raise the built-in TypeError exception.

        :param element: Input object to add to storage.
        """
        if isinstance(element, AlchemicalElement):
            self.storage.append(element)
        else:
            raise TypeError

    def pop(self, element_name: str) -> AlchemicalElement or None:
        """
        Remove and return previously added element from storage by its name.

        If there are multiple elements with the same name, remove only the one that was added most recently to the
        storage. If there are no elements with the given name, do not remove anything and return None.

        :param element_name: Name of the element to remove.
        :return: The removed AlchemicalElement object or None.
        """
        self.storage.reverse()
        is_in_storage = False
        found_element = None
        for element in self.storage:
            if is_in_storage:
                break
            if element.name == element_name:
                is_in_storage = True
                self.storage.remove(element)
                found_element = element
                self.storage.reverse()
        if not is_in_storage:
            return None
        return found_element

    def extract(self):
        """
        Return a list of all of the elements from storage and empty the storage itself.

        Order of the list must be the same as the order in which the elements were added.

        Example:
            storage = AlchemicalStorage()
            storage.add(AlchemicalElement('Water'))
            storage.add(AlchemicalElement('Fire'))
            storage.extract() # -> [<AE: Water>, <AE: Fire>]
            storage.extract() # -> []

        In this example, the second time we use .extract() the output list is empty because we already extracted
         everything.

        :return: A list of all of the elements that were previously in the storage.
        """
        storage_copy = self.storage.copy()
        self.storage = []
        return storage_copy

    def get_content(self) -> str:
        """
        Return a string that gives an overview of the contents of the storage.

        Example:
            storage = AlchemicalStorage()
            storage.add(AlchemicalElement('Water'))
            storage.add(AlchemicalElement('Fire'))
            print(storage.get_content())

        Output in console:
            Content:
             * Fire x 1
             * Water x 1

        The elements must be sorted alphabetically by name.

        :return: Content as a string.
        """
        if not self.storage:
            return "Content:\n Empty."
        storage_copy = sorted(self.storage.copy(), key=lambda x: x.name)
        storage_list = {}
        for element in storage_copy:
            if element.name in storage_list.keys():
                storage_list[element.name] += 1
            else:
                storage_list[element.name] = 1
        fin_str = ''
        fin_str += "Content:\n"
        for key, value in storage_list.items():
            fin_str += f" * {key} x {value}\n"
        return fin_str.strip()


class AlchemicalRecipes:
    """AlchemicalRecipes class."""

    def __init__(self):
        """
        Initialize the AlchemicalRecipes class.

        Add whatever you need to make this class function.
        """
        self.recipe_list = {}

    def add_recipe(self, first_component_name: str, second_component_name: str, product_name: str):
        """
        Determine if recipe is valid and then add it to recipes.

        A recipe consists of three strings, two components and their product.
        If any of the parameters are the same, raise the 'DuplicateRecipeNamesException' exception.
        If there already exists a recipe for the given pair of components, raise the 'RecipeOverlapException' exception.

        :param first_component_name: The name of the first component element.
        :param second_component_name: The name of the second component element.
        :param product_name: The name of the product element.
        """
        if first_component_name == second_component_name or first_component_name == product_name or second_component_name == product_name:
            raise DuplicateRecipeNamesException

        if (first_component_name, second_component_name) in self.recipe_list or (
                second_component_name, first_component_name) in self.recipe_list:
            raise RecipeOverlapException
        else:
            self.recipe_list[(first_component_name, second_component_name)] = product_name

    def get_product_name(self, first_component_name: str, second_component_name: str) -> str or None:
        """
        Return the name of the product for the two components.

        The order of the first_component_name and second_component_name is interchangeable, so search for combinations
        of (first_component_name, second_component_name) and (second_component_name, first_component_name).

        If there are no combinations for the two components, return None

        Example:
            recipes = AlchemicalRecipes()
            recipes.add_recipe('Water', 'Wind', 'Ice')
            recipes.get_product_name('Water', 'Wind')  # ->  'Ice'
            recipes.get_product_name('Wind', 'Water')  # ->  'Ice'
            recipes.get_product_name('Fire', 'Water')  # ->  None
            recipes.add_recipe('Water', 'Fire', 'Steam')
            recipes.get_product_name('Fire', 'Water')  # ->  'Steam'

        :param first_component_name: The name of the first component element.
        :param second_component_name: The name of the second component element.
        :return: The name of the product element or None.
        """
        if (first_component_name, second_component_name) in self.recipe_list:
            return self.recipe_list[(first_component_name, second_component_name)]
        elif (second_component_name, first_component_name) in self.recipe_list:
            return self.recipe_list[(second_component_name, first_component_name)]
        else:
            return None

    def get_component_names(self, product_name: str) -> Tuple[str, str] or None:
        """Get the components of a certain product."""
        products = dict([(y, x) for (x, y) in self.recipe_list.items()])
        if product_name not in products.keys():
            return None
        return products[product_name]


class DuplicateRecipeNamesException(Exception):
    """Raised when attempting to add a recipe that has same names for components and product."""


class RecipeOverlapException(Exception):
    """Raised when attempting to add a pair of components that is already used for another existing recipe."""


class Cauldron(AlchemicalStorage):
    """
    Cauldron class.

    Extends the 'AlchemicalStorage' class.
    """

    def __init__(self, recipes: AlchemicalRecipes):
        """Initialize the Cauldron class."""
        super().__init__()
        self.recipes = recipes

    def check_chain_reaction(self):
        """Check whether or not any chain reactions take place."""
        for element in reversed(self.storage):
            self.add(element, True)

    def addition_loop(self, element, reverse, combined, chain_reaction):
        """For loop for the add() function of this class."""
        for elem in self.storage:
            if combined:
                break
            product = self.recipes.get_product_name(elem.name, element.name)
            if product is not None:
                if isinstance(elem, Catalyst):
                    if elem.uses < 1:
                        continue
                    elem.uses -= 1
                else:
                    self.storage.remove(elem)

                if isinstance(element, Catalyst):
                    if element.uses < 1:
                        break
                    element.uses -= 1
                if chain_reaction:
                    self.storage.remove(element)

                combined = True
                self.storage.reverse()
                reverse = False
                if isinstance(element, Catalyst) and not chain_reaction:
                    AlchemicalStorage.add(self, element)
                AlchemicalStorage.add(self, AlchemicalElement(product))
        return reverse, combined, chain_reaction

    def add(self, element: AlchemicalElement, chain_reaction=False):
        """
        Add element to storage and check if it can combine with anything already inside.

        Use the 'recipes' object that was given in the constructor to determine the combinations.

        Example:
            recipes = AlchemicalRecipes()
            recipes.add_recipe('Water', 'Wind', 'Ice')
            cauldron = Cauldron(recipes)
            cauldron.add(AlchemicalElement('Water'))
            cauldron.add(AlchemicalElement('Wind'))
            cauldron.extract() # -> [<AE: Ice>]

        :param element: Input object to add to storage.
        """
        if not isinstance(element, AlchemicalElement):
            raise TypeError

        combined = False
        self.storage.reverse()
        reverse = True
        reverse, combined, chain_reaction = self.addition_loop(element, reverse, combined, chain_reaction)
        if not combined and not chain_reaction:
            if reverse:
                self.storage.reverse()
                reverse = False
            AlchemicalStorage.add(self, element)
        if reverse:
            self.storage.reverse()
        if combined:
            self.check_chain_reaction()


class Catalyst(AlchemicalElement):
    """Catalyst class."""

    def __init__(self, name: str, uses: int):
        """
        Initialize the Catalyst class.

        :param name: The name of the Catalyst.
        :param uses: The number of uses the Catalyst has.
        """
        super().__init__(name)
        self.uses = uses

    def __repr__(self) -> str:
        """
        Representation of the Catalyst class.

        Example:
            catalyst = Catalyst("Philosophers' stone", 3)
            print(catalyst) # -> <C: Philosophers' stone (3)>

        :return: String representation of the Catalyst.
        """
        return f"<C: {self.name} ({self.uses})>"


class Purifier(AlchemicalStorage):
    """
    Purifier class.

    Extends the 'AlchemicalStorage' class.
    """

    def __init__(self, recipes: AlchemicalRecipes):
        """Initialize the Purifier class."""
        super().__init__()
        self.recipes = recipes

    def check_chain_reaction(self):
        """Check whether or not any chain reactions take place."""
        for element in reversed(self.storage):
            self.add(element, True)

    def add(self, element: AlchemicalElement, chain_reaction=False):
        """
        Add element to storage and check if it can be split into anything.

        Use the 'recipes' object that was given in the constructor to determine the combinations.

        Example:
            recipes = AlchemicalRecipes()
            recipes.add_recipe('Water', 'Wind', 'Ice')
            purifier = Purifier(recipes)
            purifier.add(AlchemicalElement('Ice'))
            purifier.extract() # -> [<AE: Water>, <AE: Wind>]   or  [<AE: Wind>, <AE: Water>]

        :param element: Input object to add to storage.
        """
        if not isinstance(element, AlchemicalElement):
            raise TypeError

        broke = False
        components = AlchemicalRecipes.get_component_names(self.recipes, element.name)
        if components is None and not chain_reaction:
            AlchemicalStorage.add(self, element)
        if components is not None:
            broke = True
            if chain_reaction:
                self.storage.remove(element)
            AlchemicalStorage.add(self, AlchemicalElement(components[0]))
            AlchemicalStorage.add(self, AlchemicalElement(components[1]))
        if broke:
            self.check_chain_reaction()


if __name__ == '__main__':
    recipes = AlchemicalRecipes()
    recipes.add_recipe('Earth', 'Fire', 'Iron')
    recipes.add_recipe('Iron', 'Water', 'Rust')

    cauldron = Cauldron(recipes)
    cauldron.add(AlchemicalElement('Fire'))
    cauldron.add(AlchemicalElement('Water'))
    cauldron.add(AlchemicalElement('Earth'))
    print(cauldron.extract())  # -> [<AE: Rust>]
    recipes = AlchemicalRecipes()
    recipes.add_recipe('Earth', 'Fire', 'Iron')
    recipes.add_recipe('Iron', 'Water', 'Rust')

    purifier = Purifier(recipes)
    purifier.add(AlchemicalElement('Rust'))
    print(purifier.extract())  # -> [<AE: Earth>, <AE: Fire>, <AE: Water>] (in any order)
    print()

if __name__ == '__main__':
    philosophers_stone = Catalyst("Philosophers' stone", 2)

    recipes = AlchemicalRecipes()
    recipes.add_recipe("Philosophers' stone", 'Mercury', 'Gold')
    recipes.add_recipe("Fire", 'Earth', 'Iron')

    cauldron = Cauldron(recipes)
    cauldron.add(philosophers_stone)
    cauldron.add(AlchemicalElement('Mercury'))
    print(cauldron.extract())  # -> [<C: Philosophers' stone (1)>, <AE: Gold>]

    cauldron.add(philosophers_stone)
    cauldron.add(AlchemicalElement('Mercury'))
    print(cauldron.extract())  # -> [<C: Philosophers' stone (0)>, <AE: Gold>]

    cauldron.add(philosophers_stone)
    cauldron.add(AlchemicalElement('Mercury'))
    print(cauldron.extract())  # -> [<C: Philosophers' stone (0)>, <AE: Mercury>]

    purifier = Purifier(recipes)
    purifier.add(AlchemicalElement('Iron'))
    print(purifier.extract())  # -> [<AE: Fire>, <AE: Earth>]    or      [<AE: Earth>, <AE: Fire>]
    print()

if __name__ == '__main__':
    recipes = AlchemicalRecipes()
    recipes.add_recipe('Fire', 'Water', 'Steam')
    recipes.add_recipe('Fire', 'Earth', 'Iron')
    recipes.add_recipe('Water', 'Iron', 'Rust')

    print(recipes.get_product_name('Water', 'Fire'))  # -> 'Steam'

    try:
        recipes.add_recipe('Fire', 'Something else', 'Fire')
        print('Did not raise, not working as intended.')

    except DuplicateRecipeNamesException:
        print('Raised DuplicateRecipeNamesException, working as intended!')

    try:
        recipes.add_recipe('Fire', 'Earth', 'Gold')
        print('Did not raise, not working as intended.')

    except RecipeOverlapException:
        print('Raised RecipeOverlapException, working as intended!')

    cauldron = Cauldron(recipes)
    cauldron.add(AlchemicalElement('Earth'))
    cauldron.add(AlchemicalElement('Water'))
    cauldron.add(AlchemicalElement('Fire'))

    print(cauldron.extract())  # -> [<AE: Earth>, <AE: Steam>]

    cauldron.add(AlchemicalElement('Earth'))
    cauldron.add(AlchemicalElement('Earth'))
    cauldron.add(AlchemicalElement('Earth'))
    cauldron.add(AlchemicalElement('Fire'))
    cauldron.add(AlchemicalElement('Fire'))
    cauldron.add(AlchemicalElement('Water'))

    print(cauldron.extract())  # -> [<AE: Earth>, <AE: Iron>, <AE: Rust>]
    print()

if __name__ == '__main__':
    element_one = AlchemicalElement('Fire')
    element_two = AlchemicalElement('Water')
    element_three = AlchemicalElement('Water')
    storage = AlchemicalStorage()

    print(element_one)  # <AE: Fire>
    print(element_two)  # <AE: Water>

    storage.add(element_one)
    storage.add(element_two)

    print(storage.get_content())
    # Content:
    #  * Fire x 1
    #  * Water x 1

    print(storage.extract())  # [<AE: Fire>, <AE: Water>]
    print(storage.get_content())
    # Content:
    #  Empty

    storage.add(element_one)
    storage.add(element_two)
    storage.add(element_three)

    print(storage.pop('Water') == element_three)  # True
    print(storage.pop('Water') == element_two)  # True
