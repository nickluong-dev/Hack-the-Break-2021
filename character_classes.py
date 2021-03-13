from random import randint
from random import choice

RARITIES = [
    {"Rarity": "Normal", "stat_multiplier": 1.0},
    {"Rarity": "Rare", "stat_multiplier": 1.2},
    {"Rarity": "Super Rare", "stat_multiplier": 1.7}
]

# Hero Classes


class Character:
    def __init__(self, hp, mp, attack, magic_attack, defence, resistance):
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.magic_attack = magic_attack
        self.defence = defence
        self.resistance = resistance


class Player(Character):
    def __init__(self, hp, mp, attack, magic_attack, defence, resistance, exp, description):
        super().__init__(hp, mp, attack, magic_attack, defence, resistance)
        self.exp = exp
        self.description = description

    def get_exp(self):
        print(f"EXP: {self.exp}/100 \n")

    def get_stats(self):
        print(f"Class: {self.__class__.__name__}\n"
              f"HP: {self.hp} \n"
              f"MP: {self.mp} \n"
              f"Attack: {self.attack} \n"
              f"Magic Attack: {self.magic_attack} \n"
              f"Defence: {self.defence} \n"
              f"Resistance: {self.resistance} \n"
              f"Rarity: {self.rarity['Rarity']} \n"
              f"Description: {self.description} \n")

    def get_multi(self):
        print(f"Multiplier: {self.rarity['stat_multiplier']}")

    def get_total(self):
        print(f"Total: {self.hp+self.mp+self.attack+self.magic_attack+self.defence+self.resistance}")


class Warrior(Player):
    def __init__(self):
        self.rarity = choice(RARITIES)
        super().__init__(hp=int(randint(13, 16) * self.rarity["stat_multiplier"]),
                         mp=int(randint(5, 7) * self.rarity["stat_multiplier"]),
                         attack=int(randint(7, 10) * self.rarity["stat_multiplier"]),
                         magic_attack=int(randint(3, 5) * self.rarity["stat_multiplier"]),
                         defence=int(randint(6, 8) * self.rarity["stat_multiplier"]),
                         resistance=int(randint(4, 6) * self.rarity["stat_multiplier"]),
                         description="A sword and shield is all you need. You're like a berserker class but "
                                     "more generic.",
                         exp=0
                         )

    def get_rarity(self):
        print(f"{self.rarity['Rarity']}\n")


class Mage(Player):
    def __init__(self):
        self.rarity = choice(RARITIES)
        super().__init__(hp=int(randint(9, 12) * self.rarity["stat_multiplier"]),
                         mp=int(randint(10, 15) * self.rarity["stat_multiplier"]),
                         attack=int(randint(4, 6) * self.rarity["stat_multiplier"]),
                         magic_attack=int(randint(8, 11) * self.rarity["stat_multiplier"]),
                         defence=int(randint(5, 7) * self.rarity["stat_multiplier"]),
                         resistance=int(randint(6, 9) * self.rarity["stat_multiplier"]),
                         description="A caster of spells. Powerless without your staff though.",
                         exp=0
                         )

    def get_rarity(self):
        print(f"{self.rarity['Rarity']}\n")



class Thief(Player):
    def __init__(self):
        self.rarity = choice(RARITIES)
        super().__init__(hp=int(randint(12, 14) * self.rarity["stat_multiplier"]),
                         mp=int(randint(8, 11) * self.rarity["stat_multiplier"]),
                         attack=int(randint(7, 9) * self.rarity["stat_multiplier"]),
                         magic_attack=int(randint(5, 7) * self.rarity["stat_multiplier"]),
                         defence=int(randint(6, 7) * self.rarity["stat_multiplier"]),
                         resistance=int(randint(6, 7) * self.rarity["stat_multiplier"]),
                         description="You're fast and deceptive, great at stealing and manipulation. You belong in "
                                     "jail.",
                         exp=0
                         )

    def get_rarity(self):
        print(f"{self.rarity['Rarity']}\n")


class Brawler(Player):
    def __init__(self):
        self.rarity = choice(RARITIES)
        super().__init__(hp=int(randint(11, 13) * self.rarity["stat_multiplier"]),
                         mp=int(randint(8, 13) * self.rarity["stat_multiplier"]),
                         attack=int(randint(9, 13) * self.rarity["stat_multiplier"]),
                         magic_attack=int(randint(3, 5) * self.rarity["stat_multiplier"]),
                         defence=int(randint(8, 10) * self.rarity["stat_multiplier"]),
                         resistance=int(randint(5, 7) * self.rarity["stat_multiplier"]),
                         description="You're great with your hands. ;)",
                         exp=0
                         )

    def get_rarity(self):
        print(f"{self.rarity['Rarity']}\n")


class Priest(Player):
    def __init__(self):
        self.rarity = choice(RARITIES)
        super().__init__(hp=int(randint(10, 12) * self.rarity["stat_multiplier"]),
                         mp=int(randint(13, 15) * self.rarity["stat_multiplier"]),
                         attack=int(randint(4, 5) * self.rarity["stat_multiplier"]),
                         magic_attack=int(randint(10, 12) * self.rarity["stat_multiplier"]),
                         defence=int(randint(7, 7) * self.rarity["stat_multiplier"]),
                         resistance=int(randint(7, 7) * self.rarity["stat_multiplier"]),
                         description="UNLIMITED HEALING.",
                         exp=0
                         )

    def get_rarity(self):
        print(f"{self.rarity['Rarity']}\n")


class DarkKnight(Player):
    def __init__(self):
        self.rarity = choice(RARITIES)
        super().__init__(hp=int(randint(10, 14) * self.rarity["stat_multiplier"]),
                         mp=int(randint(9, 10) * self.rarity["stat_multiplier"]),
                         attack=int(randint(10, 14) * self.rarity["stat_multiplier"]),
                         magic_attack=int(randint(6, 8) * self.rarity["stat_multiplier"]),
                         defence=int(randint(5, 7) * self.rarity["stat_multiplier"]),
                         resistance=int(randint(7, 9) * self.rarity["stat_multiplier"]),
                         description="UNLIMITED HEALING.",
                         exp=0
                         )

    def get_rarity(self):
        print(f"{self.rarity['Rarity']}\n")


test = Warrior()
test.get_stats()
test.get_total()

test2 = Mage()
test2.get_stats()
test2.get_total()

test3 = Thief()
test3.get_stats()
test3.get_total()

test4 = Priest()
test4.get_stats()
test4.get_total()

test5 = DarkKnight()
test5.get_stats()
test5.get_total()

test6 = Brawler()
test6.get_stats()
test6.get_total()