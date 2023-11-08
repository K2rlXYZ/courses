"""Dungeons and Pythons."""


class Adventurer:
    """Adventurer class."""

    def __init__(self, name: str, class_type: str, power: int, experience: int = 0):
        """Adventurer class constructor."""
        self.name = name

        if class_type not in ["Fighter", "Druid", "Wizard", "Paladin"]:
            self.class_type = "Fighter"
        else:
            self.class_type = class_type

        if power > 99:
            self.power = 10
        else:
            self.power = power

        self.experience = max(0, experience)

    def __repr__(self):
        """Return string representation of the Adventurer class."""
        return f"{self.name}, the {self.class_type}, Power: {self.power}, Experience: {self.experience}."

    def add_power(self, power: int):
        """Add power to adventurer."""
        self.power += power

    def add_experience(self, exp: int):
        """Add experience to adventurer."""
        if exp > 0:
            self.experience += exp
            if self.experience > 99:
                self.add_power(self.experience // 10)
                self.experience = 0


class Monster:
    """Monster class."""

    def __init__(self, name: str, type: str, power: int):
        """Monster class constructor."""
        if type == "Zombie":
            name = "Undead " + name
        self.name = name
        self.type = type
        self.power = power

    def __repr__(self):
        """Return string representation of the Monster class."""
        return f"{self.name} of type {self.type}, Power: {self.power}."


def adventurer_of_class(class_type, lst):
    """Filter list for adventurer of class type."""
    return list([x for x in lst if x.class_type == class_type])


class World:
    """World class."""

    def __init__(self, python_master):
        """World class constructor."""
        self.python_master = python_master
        self.adventurer_list = []
        self.monster_list = []
        self.graveyard = []
        self.are_necromancers_active = False
        self.active_adventurers = []
        self.active_monsters = []

    def get_python_master(self):
        """Return the python_master of the world."""
        return self.python_master

    def get_monster_list(self):
        """Get the monster_list of the world."""
        return [x for x in self.monster_list if x not in self.active_monsters]

    def get_adventurer_list(self):
        """Get the adventurer_list of the world."""
        return [x for x in self.adventurer_list if x not in self.active_adventurers]

    def add_adventurer(self, adventurer):
        """Add adventurer to world."""
        if isinstance(adventurer, Adventurer):
            self.adventurer_list.append(adventurer)

    def add_monster(self, monster):
        """Add monster to world."""
        if isinstance(monster, Monster):
            self.monster_list.append(monster)

    def get_graveyard(self):
        """Get the graveyard of the world."""
        return self.graveyard

    def remove_character(self, name):
        """Either move character to graveyard or remove them based on where they are."""
        if name in list(map(lambda x: x.name, self.adventurer_list)):
            move = [x for x in self.adventurer_list if x.name == name][0]
            self.adventurer_list.remove(move)
            self.graveyard.append(move)
        elif name in list(map(lambda x: x.name, self.monster_list)):
            move = [x for x in self.monster_list if x.name == name][0]
            self.monster_list.remove(move)
            self.graveyard.append(move)
        elif name in list(map(lambda x: x.name, self.graveyard)):
            remove = [x for x in self.graveyard if x.name == name][0]
            self.graveyard.remove(remove)

    def necromancers_active(self, boolean):
        """Change the state of necromancers."""
        self.are_necromancers_active = boolean

    def revive_graveyard(self):
        """Revive the whole graveyard as zombies into monster_list."""
        if self.are_necromancers_active:
            for being in self.graveyard:
                if isinstance(being, Monster):
                    if being.name[0:7] != "Undead ":
                        being.name = "Undead " + being.name
                    being.type = "Zombie"
                    self.add_monster(being)
                if isinstance(being, Adventurer):
                    undead_adventurer = Monster("Undead " + being.name, "Zombie " + being.class_type, being.power)
                    self.add_monster(undead_adventurer)
            self.graveyard = []
            self.are_necromancers_active = False

    def make_adventurer_active_from_list(self, lst: list):
        """Make an adventurer active."""
        for adventurer in lst:
            if adventurer not in self.active_adventurers:
                self.active_adventurers.append(adventurer)
                break

    def get_active_adventurers(self):
        """Get active adventures from world's active_adventurers list."""
        return sorted(self.active_adventurers, key=lambda x: x.experience, reverse=True)

    def add_strongest_adventurer(self, class_type: str):
        """Add strongest adventurer of class to world's active_adventurers list."""
        most_powerful_of_class = sorted(adventurer_of_class(class_type, self.adventurer_list),
                                        key=lambda adven: adven.power, reverse=True)
        self.make_adventurer_active_from_list(most_powerful_of_class)

    def add_weakest_adventurer(self, class_type: str):
        """Add weakest adventurer of class to world's active_adventurers list."""
        weakest_of_class = sorted(adventurer_of_class(class_type, self.adventurer_list),
                                  key=lambda adven: adven.power)
        self.make_adventurer_active_from_list(weakest_of_class)

    def add_most_experienced_adventurer(self, class_type: str):
        """Add most experienced adventurer of class to world's active_adventurers list."""
        most_experienced_of_class = sorted(adventurer_of_class(class_type, self.adventurer_list),
                                           key=lambda adven: adven.experience, reverse=True)
        self.make_adventurer_active_from_list(most_experienced_of_class)

    def add_least_experienced_adventurer(self, class_type: str):
        """Add least experienced adventurer of class to world's active_adventurers list."""
        least_experienced_of_class = sorted(adventurer_of_class(class_type, self.adventurer_list),
                                            key=lambda adven: adven.experience)
        self.make_adventurer_active_from_list(least_experienced_of_class)

    def add_adventurer_by_name(self, name: str):
        """Add adventurer by name to world's active_adventurers list."""
        lst = [x for x in self.adventurer_list if x.name == name]
        if len(lst) != 0 and lst[0] not in self.active_adventurers:
            self.active_adventurers.append(lst[0])

    def add_all_adventurers_of_class_type(self, class_type: str):
        """Add all adventurers of class to world's active_adventurers list."""
        all_of_class = adventurer_of_class(class_type, self.adventurer_list)
        for adventurer in all_of_class:
            if adventurer not in self.active_adventurers:
                self.active_adventurers.append(adventurer)

    def add_all_adventurers(self):
        """Add all adventurers to world's active_adventurers list."""
        for adventurer in self.adventurer_list:
            if adventurer not in self.active_adventurers:
                self.active_adventurers.append(adventurer)

    def get_active_monsters(self):
        """Get active monster's from world's active_monsters list sorted by power."""
        return sorted(self.active_monsters, key=lambda x: x.power, reverse=True)

    def add_monster_by_name(self, name: str):
        """Add monster to active_monsters list based on the monster's name."""
        lst = [x for x in self.monster_list if x.name == name]
        if len(lst) != 0 and lst[0] not in self.active_monsters:
            self.active_monsters.append(lst[0])

    def add_strongest_monster(self):
        """Add the strongest monster to the active_monster list."""
        most_powerful = sorted(self.monster_list, key=lambda monster: monster.power, reverse=True)
        for monster in most_powerful:
            if monster not in self.active_monsters:
                self.active_monsters.append(monster)
                break

    def add_weakest_monster(self):
        """Add the weakest monster to the active_monster list."""
        most_powerful = sorted(self.monster_list, key=lambda monster: monster.power)
        for monster in most_powerful:
            if monster not in self.active_monsters:
                self.active_monsters.append(monster)
                break

    def add_all_monsters_of_type(self, type: str):
        """Add all monsters of type to the active_monster list."""
        for monster in self.monster_list:
            if monster.type == type and monster not in self.active_monsters:
                self.active_monsters.append(monster)

    def add_all_monsters(self):
        """Add all monsters to the active_monster list."""
        for monster in self.monster_list:
            if monster not in self.active_monsters:
                self.active_monsters.append(monster)

    def go_adventure_friendly(self, adventurers_power, monsters_power):
        """Friendly adventure.."""
        copy_self_active_adventurers = self.active_adventurers.copy()
        if adventurers_power > monsters_power:  # win friendly
            for adventurer in copy_self_active_adventurers:
                adventurer.add_experience((monsters_power // len(copy_self_active_adventurers)))
        elif monsters_power == adventurers_power:  # tie friendly
            for adventurer in copy_self_active_adventurers:
                adventurer.add_experience((monsters_power // len(copy_self_active_adventurers)) // 2)
        for monster in self.active_monsters.copy():
            self.active_monsters.remove(monster)
        for adventurer in copy_self_active_adventurers:
            self.active_adventurers.remove(adventurer)

    def go_adventure_deadly(self, adventurers_power, monsters_power):
        """Deadly adventure."""
        copy_self_active_adventurers = self.active_adventurers.copy()
        if adventurers_power > monsters_power:  # win deadly
            for monster in self.active_monsters.copy():
                self.active_monsters.remove(monster)
                self.remove_character(monster.name)
            for adventurer in copy_self_active_adventurers:
                adventurer.add_experience(2 * (monsters_power // len(copy_self_active_adventurers)))
                self.active_adventurers.remove(adventurer)
        elif adventurers_power < monsters_power:  # loss deadly
            for adventurer in copy_self_active_adventurers:
                self.active_adventurers.remove(adventurer)
                self.remove_character(adventurer.name)
            for monster in self.active_monsters.copy():
                self.active_monsters.remove(monster)
        else:  # tie deadly
            for monster in self.active_monsters.copy():
                self.active_monsters.remove(monster)
            for adventurer in copy_self_active_adventurers:
                adventurer.add_experience((monsters_power // len(copy_self_active_adventurers)) // 2)
                self.active_adventurers.remove(adventurer)

    def go_adventure(self, deadly: bool = False):
        """Simulate an adventure."""
        animals_and_ents = [x for x in self.active_monsters if x.type == "Animal" or x.type == "Ent"]
        if len(animals_and_ents) != 0 and "Druid" in [x.class_type for x in self.active_adventurers]:
            for being in animals_and_ents:
                self.active_monsters.remove(being)

        zombies = [x for x in self.active_monsters if x.type in
                   ["Zombie", "Zombie Fighter", "Zombie Druid", "Zombie Paladin",
                    "Zombie Wizard"]]
        if len(zombies) != 0:
            paladins = adventurer_of_class("Paladin", self.active_adventurers)
            for paladin in paladins:
                paladin.power = paladin.power * 2

        adventurers_power = sum([x.power for x in self.active_adventurers])
        monsters_power = sum([x.power for x in self.active_monsters])

        if len(zombies) != 0:
            paladins = adventurer_of_class("Paladin", self.active_adventurers)
            for paladin in paladins:
                paladin.power = paladin.power // 2

        if deadly:
            self.go_adventure_deadly(adventurers_power, monsters_power)
        else:
            self.go_adventure_friendly(adventurers_power, monsters_power)
