from random import randint
from random import choice

RARITIES = [
    {"Rarity": "Normal", "stat_multiplier": 1.0},
    {"Rarity": "Rare", "stat_multiplier": 1.3},
    {"Rarity": "Super Rare", "stat_multiplier": 1.6}
]


# Hero Classes


class Character:
    def __init__(self, hp, mp, attack, magic_attack, defense, resistance, description):
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.magic_attack = magic_attack
        self.defense = defense
        self.resistance = resistance
        self.description = description

    def get_monster_stats(self):
        return (f"Class: {self.__class__.__name__}\n"
                f"HP: {self.hp} \n"
                f"MP: {self.mp} \n"
                f"Attack: {self.attack} \n"
                f"Magic Attack: {self.magic_attack} \n"
                f"defense: {self.defense} \n"
                f"Resistance: {self.resistance} \n"
                f"Total: {self.hp + self.mp + self.attack + self.magic_attack + self.defense + self.resistance}\n"
                f"Description: {self.description} \n")


class Player(Character):
    def __init__(self, hp, mp, attack, magic_attack, defense, resistance, exp, description):
        super().__init__(hp, mp, attack, magic_attack, defense, resistance, description)
        self.exp = exp

    def get_class_stats(self):
        return (f"Class: {self.__class__.__name__}\n"
                f"HP: {self.hp} \n"
                f"MP: {self.mp} \n"
                f"Attack: {self.attack} \n"
                f"Magic Attack: {self.magic_attack} \n"
                f"defense: {self.defense} \n"
                f"Resistance: {self.resistance} \n"
                f"Total: {self.hp + self.mp + self.attack + self.magic_attack + self.defense + self.resistance}\n"
                f"Rarity: {self.rarity['Rarity']} \n"
                f"EXP: {self.exp}/100 \n"
                f"Description: {self.description} \n")

    def get_classname(self):
        return self.__class__.__name__

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp

    def get_attack(self):
        return self.attack

    def get_magic_attack(self):
        return self.magic_attack

    def get_defense(self):
        return self.defense

    def get_resistance(self):
        return self.resistance

    def get_description(self):
        return self.description

    def get_multi(self):
        return f"Multiplier: {self.rarity['stat_multiplier']}"

    def get_total(self):
        return self.hp + self.mp + self.attack + self.magic_attack + self.defense + self.resistance


class Warrior(Player):
    def __init__(self):
        self.rarity = choice(RARITIES)
        super().__init__(hp=int(randint(13, 16) * self.rarity["stat_multiplier"]),
                         mp=int(randint(7, 8) * self.rarity["stat_multiplier"]),
                         attack=int(randint(7, 10) * self.rarity["stat_multiplier"]),
                         magic_attack=int(randint(5, 7) * self.rarity["stat_multiplier"]),
                         defense=int(randint(6, 8) * self.rarity["stat_multiplier"]),
                         resistance=int(randint(5, 7) * self.rarity["stat_multiplier"]),
                         description="A sword and shield is all you need. You're like a berserker class but "
                                     "more generic.",
                         exp=0
                         )

    def get_rarity(self):
        return f"{self.rarity['Rarity']}\n"


class Mage(Player):
    def __init__(self):
        self.rarity = choice(RARITIES)
        super().__init__(hp=int(randint(9, 12) * self.rarity["stat_multiplier"]),
                         mp=int(randint(10, 15) * self.rarity["stat_multiplier"]),
                         attack=int(randint(4, 6) * self.rarity["stat_multiplier"]),
                         magic_attack=int(randint(8, 11) * self.rarity["stat_multiplier"]),
                         defense=int(randint(5, 7) * self.rarity["stat_multiplier"]),
                         resistance=int(randint(6, 9) * self.rarity["stat_multiplier"]),
                         description="A caster of spells. Powerless without your staff though.",
                         exp=0
                         )

    def get_rarity(self):
        return (f"{self.rarity['Rarity']}\n")


class Thief(Player):
    def __init__(self):
        self.rarity = choice(RARITIES)
        super().__init__(hp=int(randint(12, 14) * self.rarity["stat_multiplier"]),
                         mp=int(randint(8, 11) * self.rarity["stat_multiplier"]),
                         attack=int(randint(7, 9) * self.rarity["stat_multiplier"]),
                         magic_attack=int(randint(5, 7) * self.rarity["stat_multiplier"]),
                         defense=int(randint(6, 7) * self.rarity["stat_multiplier"]),
                         resistance=int(randint(6, 7) * self.rarity["stat_multiplier"]),
                         description="You're fast and deceptive, great at stealing and manipulation. You belong in "
                                     "jail.",
                         exp=0
                         )

    def get_rarity(self):
        return (f"{self.rarity['Rarity']}\n")


class Brawler(Player):
    def __init__(self):
        self.rarity = choice(RARITIES)
        super().__init__(hp=int(randint(11, 13) * self.rarity["stat_multiplier"]),
                         mp=int(randint(8, 13) * self.rarity["stat_multiplier"]),
                         attack=int(randint(9, 13) * self.rarity["stat_multiplier"]),
                         magic_attack=int(randint(3, 5) * self.rarity["stat_multiplier"]),
                         defense=int(randint(8, 10) * self.rarity["stat_multiplier"]),
                         resistance=int(randint(5, 7) * self.rarity["stat_multiplier"]),
                         description="You're great with your hands. ;)",
                         exp=0
                         )

    def get_rarity(self):
        return self.rarity['Rarity']


class Priest(Player):
    def __init__(self):
        self.rarity = choice(RARITIES)
        super().__init__(hp=int(randint(10, 12) * self.rarity["stat_multiplier"]),
                         mp=int(randint(13, 15) * self.rarity["stat_multiplier"]),
                         attack=int(randint(4, 5) * self.rarity["stat_multiplier"]),
                         magic_attack=int(randint(10, 12) * self.rarity["stat_multiplier"]),
                         defense=int(randint(7, 7) * self.rarity["stat_multiplier"]),
                         resistance=int(randint(7, 7) * self.rarity["stat_multiplier"]),
                         description="UNLIMITED HEALING.",
                         exp=0
                         )

    def get_rarity(self):
        return f"{self.rarity['Rarity']}\n"


class DarkKnight(Player):
    def __init__(self):
        self.rarity = choice(RARITIES)
        super().__init__(hp=int(randint(10, 13) * self.rarity["stat_multiplier"]),
                         mp=int(randint(9, 10) * self.rarity["stat_multiplier"]),
                         attack=int(randint(9, 13) * self.rarity["stat_multiplier"]),
                         magic_attack=int(randint(6, 8) * self.rarity["stat_multiplier"]),
                         defense=int(randint(5, 7) * self.rarity["stat_multiplier"]),
                         resistance=int(randint(7, 7) * self.rarity["stat_multiplier"]),
                         description="I see dead people.",
                         exp=0
                         )

    def get_rarity(self):
        return f"{self.rarity['Rarity']}\n"


class Goblin(Character):
    def __init__(self):
        super().__init__(hp=randint(6, 8),
                         mp=randint(6, 8),
                         attack=randint(7, 9),
                         magic_attack=randint(5, 7),
                         defense=randint(4, 5),
                         resistance=randint(4, 5),
                         description="If Shrek fused with Lord Farquaad.")


class Zombie(Character):
    def __init__(self):
        super().__init__(hp=randint(8, 10),
                         mp=randint(6, 8),
                         attack=randint(3, 5),
                         magic_attack=randint(3, 4),
                         defense=randint(4, 5),
                         resistance=randint(4, 5),
                         description="Smells. Real. Bad")


class Werewolf(Character):
    def __init__(self):
        super().__init__(hp=randint(8, 10),
                         mp=randint(6, 8),
                         attack=randint(3, 5),
                         magic_attack=randint(3, 4),
                         defense=randint(4, 5),
                         resistance=randint(4, 5),
                         description=":dog: Woof woof. ;)")


class Vampire(Character):
    def __init__(self):
        super().__init__(hp=randint(7, 9),
                         mp=randint(6, 8),
                         attack=randint(6, 7),
                         magic_attack=randint(3, 4),
                         defense=randint(5, 7),
                         resistance=randint(2, 3),
                         description="He wants to Succ Blood.")
