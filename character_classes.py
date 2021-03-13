import random



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
    def __init__(self, hp, mp, attack, magic_attack, defence, resistance, exp, rarity, description):
        super().__init__(hp, mp, attack, magic_attack, defence, resistance)
        self.exp = exp
        self.rarity = rarity
        self.description = description

    def get_exp(self):
        print(f"EXP: {self.exp}/100 \n")

    def get_rarity(self):
        return self.rarity

    def get_stats(self):
        print(f"HP: {self.hp} \n"
              f"MP: {self.mp} \n"
              f"Attack: {self.attack} \n"
              f"Magic Attack: {self.magic_attack} \n"
              f"Defence: {self.defence} \n"
              f"Resistance: {self.resistance} \n"
              f"Rarity: {self.rarity} \n"
              f"Description: {self.description} \n")


Warrior = Player(
        random.randrange(13, 16) * Player.get_rarity(),
        random.randrange(5, 7),
        random.randrange(7, 10),
        random.randrange(3, 5),
        random.randrange(6, 8),
        random.randrange(4, 6),
        0, {1, 2, 3},
        "A sword and shield is all you need. You're like a berserker class but more generic.")

Mage = Player(
        random.randrange(9, 12),
        random.randrange(10, 15),
        random.randrange(4, 6),
        random.randrange(7, 10),
        random.randrange(5, 7),
        random.randrange(6, 9),
        0, "Normal",
        "A caster of spells. Powerless without your staff though.")

Thief = Player(
        random.randrange(12, 13),
        random.randrange(8, 11),
        random.randrange(7, 8),
        random.randrange(5, 7),
        random.randrange(6, 7),
        random.randrange(6, 7),
        0, "Normal",
        "You're fast and deceptive, great at stealing and manipulation. You belong in jail.")


test = Warrior
test.get_stats()
test.get_exp()

