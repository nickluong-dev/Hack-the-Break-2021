"""
gaca
"""
from random import randint, choice


def GENDER_TYPES() -> dict:
    return {1: "man", 2: "woman", 3: "traveler"}


def get_pronoun_list(gender: int) -> list:
    pronouns = {1: ["he", "him", "his"], 2: ["she", "her", "hers"], 3: ["they", "them", "theirs"]}
    return pronouns[gender]


def get_personality_type() -> str:
    personalities = ["energetic", "timid", "burly", "easy-going", "unreliable", "unpleasant",
                     "mischievous", "happy-go-lucky", "cautious", "pragmatic", "altruistic",
                     "unlucky", "lucky", "fearsome", "unconfident", "confident"]
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
             f"{pronoun[0]} once ruled", f"which has exiled {pronoun[1]}"]
    return choice(lands)


def create_randomized_bio(name: str, gender: int) -> str:
    personality = get_personality_type()
    land = get_land(get_pronoun_list(gender))

    bio = f"{name} is a {personality} {GENDER_TYPES()[gender]} from a land {land}."
    return bio


class Character:
    def __init__(self):
        self.__gender = randint(1, 3)
        name_choices = {1: get_male_name, 2: get_female_name, 3: choice([get_male_name, get_female_name])}
        self.__name = name_choices[self.__gender]()
        self.__rarity = randint(1, 5)
        self.__bio = create_randomized_bio(self.__name, self.__gender)
        self.__class = 0  # use the classes thing when it's ready

    def print_bio(self):
        print(self.__bio)


def main():
    new_character = Character()
    new_character.print_bio()


if __name__ == "__main__":
    main()
