"""Adventure.py test."""
from adventure import World, Adventurer, Monster, adventurer_of_class


def test_world_python_master():
    """Test world python master."""
    world = World("Cool")
    assert world.get_python_master() == "Cool"


def test_adventurer_constructor():
    """Test adventurer constructor."""
    adv = Adventurer("Peep", "Druid", 33, 20)
    assert adv.name == "Peep"
    assert adv.class_type == "Druid"
    assert adv.power == 33
    assert adv.experience == 20


def test_adventurer_constructor_wrong_class():
    """Test adventurer constructor wrong class."""
    adv = Adventurer("Peep", "eeee", 33, 20)
    assert adv.class_type == "Fighter"


def test_adventurer_constructor_wrong_power():
    """Test adventurer constructor wrong power."""
    """Test adventurer constructor wrong power"""
    adv = Adventurer("Peep", "Druid", 100, 20)
    assert adv.power == 10


def test_adventurer_constructor_negative_exp():
    """Test adventurer constructor negative exp."""
    adv = Adventurer("Peep", "Druid", 33, -20)
    assert adv.experience == 0


def test_adventurer_repr():
    """Test adventurer repr."""
    adv = Adventurer("Peep", "Druid", 33, 20)
    assert adv.__repr__() == "Peep, the Druid, Power: 33, Experience: 20."


def test_adventurer_add_power():
    """Test adventurer add power."""
    adv = Adventurer("Peep", "Druid", 33, 20)
    adv.add_power(20)
    assert adv.power == 53


def test_adventurer_add_experience():
    """Test adventurer add experience."""
    adv = Adventurer("Peep", "Druid", 33, 20)
    adv.add_experience(30)
    assert adv.experience == 50
    adv.add_experience(50)
    assert adv.power == 43
    assert adv.experience == 0


def test_monster_constructor():
    """Test monster constructor."""
    mons = Monster("Name", "Type", 99)
    assert mons.name == "Name"
    assert mons.type == "Type"
    assert mons.power == 99


def test_monster_constructor_zombie():
    """Test monster constructor zombie."""
    mons = Monster("Name", "Zombie", 99)
    assert mons.name == "Undead Name"


def test_monster_repr():
    """Test monster repr."""
    mons = Monster("Name", "Type", 99)
    assert mons.__repr__() == "Name of type Type, Power: 99."


def test_adventurer_of_class():
    """Test adventurer of class."""
    hero = Adventurer("Sander", "Paladin", 50)
    friend = Adventurer("Peep", "Druid", 99)
    another_friend = Adventurer("Toots", "Wizard", 40)
    annoying_friend = Adventurer("XxX_Eepiline_Sõdalane_XxX", "Tulevikurändaja ja ninja", 999999)
    assert adventurer_of_class("Druid", [hero, friend, another_friend, annoying_friend]) == [friend]


def test_world_add_monster():
    """Test world add monster."""
    world = World("Sõber")
    goblin_spear = Monster("Goblin Spearman", "Goblin", 95)
    friend = Adventurer("Peep", "Druid", 99)
    world.add_monster(friend)
    assert world.monster_list == []
    world.add_monster(goblin_spear)
    assert world.get_monster_list() == [goblin_spear]


def test_world_add_adventurer():
    """Test world add adventurer."""
    world = World("Sõber")
    goblin_spear = Monster("Goblin Spearman", "Goblin", 95)
    friend = Adventurer("Peep", "Druid", 99)
    world.add_adventurer(goblin_spear)
    assert world.get_adventurer_list() == []
    world.add_adventurer(friend)
    assert world.get_adventurer_list() == [friend]


def test_world_get_monster_list():
    """Test world get monster list."""
    world = World("Sõber")
    goblin_spear = Monster("Goblin Spearman", "Goblin", 95)
    gargantuan_badger = Monster("Massive Badger", "Animal", 1590)
    world.add_monster(goblin_spear)
    assert world.get_monster_list() == [goblin_spear]
    world.add_monster(gargantuan_badger)
    assert world.get_monster_list() == [goblin_spear, gargantuan_badger]
    world.add_strongest_monster()
    assert world.get_monster_list() == [goblin_spear]


def test_world_get_adventurer_list():
    """Test world get adventurer list."""
    world = World("Sõber")
    hero = Adventurer("Sander", "Paladin", 50)
    friend = Adventurer("Peep", "Druid", 99)
    another_friend = Adventurer("Toots", "Wizard", 40)
    annoying_friend = Adventurer("XxX_Eepiline_Sõdalane_XxX", "Tulevikurändaja ja ninja", 999999)
    world.add_adventurer(hero)
    world.add_adventurer(friend)
    world.add_adventurer(another_friend)
    assert world.get_adventurer_list() == [hero, friend, another_friend]
    world.add_adventurer(annoying_friend)
    assert world.get_adventurer_list() == [hero, friend, another_friend, annoying_friend]
    world.add_strongest_adventurer("Druid")
    assert world.get_adventurer_list() == [hero, another_friend, annoying_friend]


def test_world_get_graveyard():
    """Test world get graveyard."""
    world = World("Sõber")
    hero = Adventurer("Sander", "Paladin", 50)
    friend = Adventurer("Peep", "Druid", 99)
    world.add_adventurer(hero)
    world.add_adventurer(friend)
    assert world.get_graveyard() == []
    world.remove_character(hero.name)
    assert world.get_graveyard() == [hero]


def test_world_remove_chracter():
    """Test world remove chracter."""
    world = World("Sõber")
    hero = Adventurer("Sander", "Paladin", 50)
    friend = Adventurer("Peep", "Druid", 99)
    world.add_adventurer(hero)
    world.add_adventurer(friend)
    world.remove_character(hero.name)
    assert hero not in world.get_adventurer_list()
    assert hero in world.get_graveyard()
    world.remove_character(hero.name)
    assert hero not in world.get_graveyard()
    world.remove_character(friend.name)
    assert friend not in world.get_adventurer_list()
    assert friend in world.get_graveyard()


def test_world_necromancers_active():
    """Test world necromancers active."""
    world = World("Sõber")
    assert not world.are_necromancers_active
    world.necromancers_active(True)
    assert world.are_necromancers_active


def test_revive_graveyard():
    """Test revive graveyard."""
    world = World("Sõber")
    hero = Adventurer("Sander", "Paladin", 50)
    friend = Adventurer("Peep", "Druid", 99)
    world.add_adventurer(hero)
    world.add_adventurer(friend)
    goblin_spear = Monster("Goblin Spearman", "Goblin", 95)
    gargantuan_badger = Monster("Massive Badger", "Animal", 1590)
    world.add_monster(goblin_spear)
    world.add_monster(gargantuan_badger)
    world.remove_character(goblin_spear.name)
    world.remove_character(hero.name)
    assert hero in world.get_graveyard() and goblin_spear in world.get_graveyard()
    world.necromancers_active(True)
    world.revive_graveyard()
    assert goblin_spear in world.get_monster_list()
    assert goblin_spear.type == "Zombie"
    assert goblin_spear.name == "Undead Goblin Spearman"
    assert hero not in world.get_graveyard()
    undead = [x for x in world.get_monster_list() if x.type == "Zombie Paladin"][0]
    assert undead is not None
    assert undead.name == "Undead Sander"
    assert undead.type == "Zombie Paladin"


def test_make_adventurer_active_from_list():
    """Test make adventurer active from list."""
    world = World("Sõber")
    hero = Adventurer("Sander", "Paladin", 50)
    friend = Adventurer("Peep", "Druid", 99)
    world.add_adventurer(hero)
    world.add_adventurer(friend)
    world.make_adventurer_active_from_list([hero, friend])
    assert hero in world.get_active_adventurers()
    world.make_adventurer_active_from_list([hero, friend])
    assert hero, friend in world.get_active_adventurers()


def test_world_get_active_adventurers():
    """Test world get active adventurers."""
    world = World("Sõber")
    hero = Adventurer("Sander", "Paladin", 50, 10)
    friend = Adventurer("Peep", "Druid", 99, 20)
    world.add_adventurer(hero)
    world.add_adventurer(friend)
    world.make_adventurer_active_from_list([hero, friend])
    world.make_adventurer_active_from_list([hero, friend])
    assert world.get_active_adventurers() == [friend, hero]


def test_world_add_strongest_adventurer():
    """Test world add strongest adventurer."""
    world = World("Sõber")
    hero = Adventurer("Sander", "Paladin", 50, 10)
    friend = Adventurer("Peep", "Paladin", 99, 20)
    world.add_adventurer(hero)
    world.add_adventurer(friend)
    world.add_strongest_adventurer("Paladin")
    assert friend in world.get_active_adventurers()


def test_world_add_weakest_adventurer():
    """Test world add weakest adventurer."""
    world = World("Sõber")
    hero = Adventurer("Sander", "Paladin", 50, 10)
    friend = Adventurer("Peep", "Paladin", 99, 20)
    world.add_adventurer(hero)
    world.add_adventurer(friend)
    world.add_weakest_adventurer("Paladin")
    assert hero in world.get_active_adventurers()


def test_world_add_most_experienced_adventurer():
    """Test world add most experienced adventurer."""
    world = World("Sõber")
    hero = Adventurer("Sander", "Paladin", 50, 10)
    friend = Adventurer("Peep", "Paladin", 99, 20)
    world.add_adventurer(hero)
    world.add_adventurer(friend)
    world.add_most_experienced_adventurer("Paladin")
    assert friend in world.get_active_adventurers()


def test_world_add_least_experienced_adventurer():
    """Test world add least experienced adventurer."""
    world = World("Sõber")
    hero = Adventurer("Sander", "Paladin", 50, 10)
    friend = Adventurer("Peep", "Paladin", 99, 20)
    world.add_adventurer(hero)
    world.add_adventurer(friend)
    world.add_least_experienced_adventurer("Paladin")
    assert hero in world.get_active_adventurers()


def test_world_add_adventurer_by_name_adventurer():
    """Test world add adventurer by name adventurer."""
    world = World("Sõber")
    hero = Adventurer("Sander", "Paladin", 50, 10)
    friend = Adventurer("Peep", "Paladin", 99, 20)
    world.add_adventurer(hero)
    world.add_adventurer(friend)
    world.add_adventurer_by_name("Sander")
    assert hero in world.get_active_adventurers()


def test_world_add_all_adventurers_of_class_type():
    """Test world add all adventurers of class type."""
    world = World("Sõber")
    hero = Adventurer("Sander", "Paladin", 50, 10)
    friend1 = Adventurer("Peep", "Paladin", 99, 20)
    friend2 = Adventurer("Peep", "eeee", 99, 20)
    world.add_adventurer(hero)
    world.add_adventurer(friend1)
    world.add_adventurer(friend2)
    world.add_all_adventurers_of_class_type("Paladin")
    assert hero, friend1 in world.get_active_adventurers()


def test_world_add_all_adventurers_adventurer():
    """Test world add all adventurers adventurer."""
    world = World("Sõber")
    hero = Adventurer("Sander", "Paladin", 50, 10)
    friend1 = Adventurer("Peep", "Paladin", 99, 20)
    friend2 = Adventurer("Peep", "eeee", 99, 20)
    world.add_adventurer(hero)
    world.add_adventurer(friend1)
    world.add_adventurer(friend2)
    world.add_all_adventurers()
    assert world.get_active_adventurers() == [friend1, friend2, hero]


def test_world_get_active_monsters():
    """Test world get active monsters."""
    world = World("Sõber")
    hero = Monster("Sander", "Paladin", 50)
    friend = Monster("Peep", "Druid", 99)
    world.add_monster(hero)
    world.add_monster(friend)
    world.add_strongest_monster()
    world.add_strongest_monster()
    assert world.get_active_monsters() == [friend, hero]


def test_world_add_monster_by_name():
    """Test world add monster by name."""
    world = World("Sõber")
    hero = Monster("Sander", "Paladin", 50)
    friend = Monster("Peep", "Druid", 99)
    world.add_monster(hero)
    world.add_monster(friend)
    world.add_monster_by_name("Sander")
    assert world.get_active_monsters() == [hero]


def test_world_add_strongest_monster():
    """Test world add strongest monster."""
    world = World("Sõber")
    hero = Monster("Sander", "Paladin", 50)
    friend = Monster("Peep", "Druid", 99)
    friend2 = Monster("Peep", "Dawg", 99)
    world.add_monster(hero)
    world.add_monster(friend)
    world.add_monster(friend2)
    world.add_strongest_monster()
    assert world.get_active_monsters() == [friend]


def test_world_add_weakest_monster():
    """Test world add weakest monster."""
    world = World("Sõber")
    hero = Monster("Sander", "Paladin", 50)
    friend = Monster("Peep", "Druid", 99)
    friend2 = Monster("Peep", "Dawg", 77)
    world.add_monster(hero)
    world.add_monster(friend)
    world.add_monster(friend2)
    world.add_weakest_monster()
    assert world.get_active_monsters() == [hero]


def test_world_add_all_monsters_of_type():
    """Test world add all monsters of type."""
    world = World("Sõber")
    hero = Monster("Sander", "Paladin", 50)
    friend = Monster("Peep", "Druid", 99)
    friend2 = Monster("Peep", "Druid", 77)
    world.add_monster(hero)
    world.add_monster(friend)
    world.add_monster(friend2)
    world.add_all_monsters_of_type("Druid")
    assert world.get_active_monsters() == [friend, friend2]


def test_world_add_all_monsters():
    """Test world add all monsters."""
    world = World("Sõber")
    hero = Monster("Sander", "Paladin", 50)
    friend = Monster("Peep", "Druid", 99)
    friend2 = Monster("Peep", "Druid", 77)
    world.add_monster(hero)
    world.add_monster(friend)
    world.add_monster(friend2)
    world.add_all_monsters()
    assert world.get_active_monsters() == [friend, friend2, hero]


def test_go_adventure_friendly():
    """Test go adventure friendly."""
    world = World("Sõber")
    m1 = Monster("Sander", "Paladin", 50)
    m2 = Monster("Peep", "Druid", 99)
    m3 = Monster("Peep", "Druid", 77)
    world.add_monster(m1)
    world.add_monster(m2)
    world.add_monster(m3)
    a1 = Adventurer("Sander", "Paladin", 50, 10)
    a2 = Adventurer("Peep", "Paladin", 99, 20)
    a3 = Adventurer("Peep", "eeee", 99, 20)
    world.add_adventurer(a1)
    world.add_adventurer(a2)
    world.add_adventurer(a3)
    world.add_all_monsters()
    world.add_all_adventurers()
    world.go_adventure_friendly(248, 226)  # win
    assert world.get_active_monsters() == []
    assert m1 in world.get_monster_list()
    assert m2 in world.get_monster_list()
    assert m3 in world.get_monster_list()
    assert world.get_active_adventurers() == []
    assert a1 in world.get_adventurer_list()
    assert a2 in world.get_adventurer_list()
    assert a3 in world.get_adventurer_list()
    assert world.get_graveyard() == []
    assert a1.experience == 85
    assert a2.experience == 95

    world.add_all_monsters()
    world.add_all_adventurers()
    world.go_adventure_friendly(226, 226)  # tie
    assert a1.power == 62
    assert a2.power == 112
    assert a1.experience == 0
    assert a2.experience == 0

    world.add_all_monsters()
    world.add_all_adventurers()
    world.go_adventure_friendly(200, 226)  # loss
    assert world.get_active_monsters() == []
    assert m1 in world.get_monster_list()
    assert m2 in world.get_monster_list()
    assert m3 in world.get_monster_list()
    assert world.get_active_adventurers() == []
    assert a1 in world.get_adventurer_list()
    assert a2 in world.get_adventurer_list()
    assert a3 in world.get_adventurer_list()
    assert world.get_graveyard() == []


def test_world_go_adventure_deadly():
    """Test world go adventure deadly."""
    world = World("Sõber")
    m1 = Monster("Sander1", "Paladin", 50)
    m2 = Monster("Peep2", "Druid", 99)
    m3 = Monster("Peep3", "Druid", 77)
    world.add_monster(m1)
    world.add_monster(m2)
    world.add_monster(m3)
    a1 = Adventurer("Sander4", "Paladin", 50, 10)
    a2 = Adventurer("Peep5", "Paladin", 99, 20)
    a3 = Adventurer("Peep6", "eeee", 99, 20)
    world.add_adventurer(a1)
    world.add_adventurer(a2)
    world.add_adventurer(a3)
    world.add_strongest_monster()
    world.add_all_adventurers()
    world.go_adventure_deadly(248, 226)  # win
    assert world.get_active_monsters() == []
    assert m2 in world.get_graveyard()
    assert world.get_active_adventurers() == []
    assert a1 in world.get_adventurer_list()
    assert a2 in world.get_adventurer_list()
    assert a3 in world.get_adventurer_list()
    assert world.get_graveyard() is not []
    assert a1.power == 66
    assert a2.power == 116
    assert a1.experience == 0
    assert a2.experience == 0

    world.add_all_monsters()
    world.add_all_adventurers()
    world.go_adventure_deadly(226, 226)  # tie
    assert world.get_active_monsters() == []
    assert m1 in world.get_monster_list()
    assert m3 in world.get_monster_list()
    assert world.get_active_adventurers() == []
    assert a1 in world.get_adventurer_list()
    assert a2 in world.get_adventurer_list()
    assert a3 in world.get_adventurer_list()
    assert a1.power == 66
    assert a2.power == 116
    assert a1.experience == 37
    assert a2.experience == 37

    world.add_all_monsters()
    world.add_all_adventurers()
    world.go_adventure_deadly(200, 226)  # loss
    assert world.get_active_monsters() == []
    assert m1 in world.get_monster_list()
    assert m3 in world.get_monster_list()
    assert world.get_active_adventurers() == []
    assert a1 in world.get_graveyard()
    assert a2 in world.get_graveyard()
    assert a3 in world.get_graveyard()
    assert world.get_graveyard() is not []


def test_paladin_and_zombie():
    """Test paladin and zombie."""
    world = World("Sõber")
    m1 = Monster("Sander1", "Zombie", 50)
    m2 = Monster("Peep2", "Zombie", 197)
    m3 = Monster("Peep3", "Zombie", 77)
    a1 = Adventurer("Sander4", "Paladin", 50, 10)
    a2 = Adventurer("Peep5", "Paladin", 99, 20)
    a3 = Adventurer("Peep6", "Paladin", 99, 20)
    world.add_monster(m1)
    world.add_monster(m2)
    world.add_monster(m3)
    world.add_adventurer(a1)
    world.add_adventurer(a2)
    world.add_adventurer(a3)
    world.add_strongest_monster()
    world.add_strongest_adventurer("Paladin")
    world.go_adventure(True)
    assert m2 in world.get_graveyard()
    assert a2.power == 140
