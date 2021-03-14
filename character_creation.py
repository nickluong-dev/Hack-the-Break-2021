"""
character stuff
"""
from random import randint, choice
from character_classes import *


def get_gender_type(gender: int) -> str:
    genders = {1: "man", 2: "woman", 3: "traveler"}
    return genders[gender]


def get_pronoun_list(gender: int) -> list:
    pronouns = {1: ["he", "him", "his"], 2: ["she", "her", "her"], 3: ["they", "them", "their"]}
    return pronouns[gender]


def get_personality_type() -> str:
    personalities = ["n energetic", " timid", " burly", "n easy-going", "n unreliable", "n unpleasant",
                     " mischievous", " happy-go-lucky", " cautious", " pragmatic", "n altruistic",
                     "n unlucky", " lucky", " fearsome", "n unconfident", " confident"]
    return choice(personalities)


def get_male_name() -> str:
    names = ["Shinji", "Roger", "Eve", "Gary", "Terry", "Nick", "Sean", "Henry", "Aidan",
             "Tye", "Faris", "Vincent", "Jean", "Marty", "Volk", "Prince", "Alan",
             "Lowen", "Mars", "Luther", "Lecter", "Leo", "Eugene", "Jack", "Alex"]
    return choice(names)


def get_female_name() -> str:
    names = ["Asuka", "Rei", "Elly", "Catherine", "Ann", "Lily", "Aeleen", "Melany",
             "Alana", "Louise", "Noelle", "Mary", "Sophie", "Sophia", "Gabby", "Rebecca",
             "Hanna", "Vanessa", "Illya", "Alex", "Veronica", "Soleil", "Eirika"]
    return choice(names)


def get_land(pronoun: list) -> str:
    lands = ["where the winters are long and cold", "named Elbrook",
             f"forgotten by all, but not {pronoun[1]}", "far, far, farther yet from here",
             "of humid summers and dry winters", "with no ruler",
             f"which {pronoun[0]} can no longer return to", "writhe with strife and conflict",
             "with unending peace that blends the days together",
             "where Gaia's blessings have been bled dry",
             "where the breeze is calm and steady, but none are present to feel the wind",
             f"{pronoun[0]} once ruled", f"which has exiled {pronoun[1]}",
             "devastated by the wrath of a god who went yet another year without sacrifice"]
    return choice(lands)


def get_extended_bio(pronoun: list, name: str) -> str:
    ext_bio = [f"{name} has a stern neutral expression, but {pronoun[0]} couldn't hurt a fly.",
               f"Once, masquerading under the guise of a merchant, {name} made a fortune from swindling the rich.",
               f"Long ago, {name} lead a clandestine vigilante organization. "
               f"{pronoun[0].title()} cannot afford to be found.",
               f"Whispers on the wind tell of another with {name}'s face. These whispers are soon extinguished.",
               f"As years pass and the seasons change, {name} stays the same."
               f" There are none among the living who remember how this came to be.",
               f"After angering a witch, {name} was placed under a curse which "
               f"stole {pronoun[2]} ability to remember faces.",
               f"The world would soon end; this, {name} believed. This, {pronoun[0]} knew with all {pronoun[2]} being.",
               f"{name} can play almost any instrument perfectly, but is prone to breaking them.",
               f"{name} is loved by animals, and loves animals in return.",
               f"{name} didn't mean mean to end up here, but that's quite alright to {pronoun[1]}.",
               f"'Here for a good time, not a long time' is {pronoun[2]} motto. "
               f"{pronoun[2].title()} friends think {pronoun[0]} should get a better motto.",
               f"'Get in the robot, {name}.' {name} still thinks about that day, and shutters.",
               f"Yelling loudly is {pronoun[2]} greatest talent. 'It ain't easy,' {name} is quick to insist.",
               f"{name} "]
    return choice(ext_bio)


def create_randomized_bio(gender: int, name: str) -> str:
    personality = get_personality_type()
    pronoun = get_pronoun_list(gender)
    land = get_land(pronoun)
    ext_bio = get_extended_bio(pronoun, name)

    bio = f"A{personality} {get_gender_type(gender)} from a land {land}.\n{ext_bio}"
    return bio


class CharacterInfo:
    def __init__(self):
        self.gender = randint(1, 3)

        name_choices = {1: get_male_name, 2: get_female_name, 3: choice([get_male_name, get_female_name])}
        self.name = name_choices[self.gender]()

        self.bio = create_randomized_bio(self.gender, self.name)

        character_classes = [Warrior, Mage, Thief, Brawler, Priest, DarkKnight]

        self.stats = choice(character_classes)()


def main():
    new_character = CharacterInfo()
    return new_character.bio


if __name__ == "__main__":
    main()
