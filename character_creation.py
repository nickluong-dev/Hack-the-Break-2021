"""
character stuff
"""
from random import randint, choice
from character_classes import *
import user_controller

def get_gender_type(gender: int) -> str:
    genders = {1: "man", 2: "woman", 3: "traveler"}
    return genders[gender]


def get_pronoun_list(gender: int) -> list:
    pronouns = {1: ["he", "him", "his"], 2: ["she", "her", "her"], 3: ["they", "them", "their"]}
    return pronouns[gender]


def get_personality_type() -> str:
    personalities = ["n energetic", " timid", " burly", "n easy-going", "n unreliable", "n unpleasant",
                     " mischievous", " happy-go-lucky", " cautious", " pragmatic", "n altruistic",
                     "n unlucky", " lucky", " fearsome", "n unconfident", " confident", " troubled",
                     " heavens-blessed", " secretive", " confrontational", " motivated", " sickly",
                     " determined", " loud", " quiet", " voracious", " blind", " deaf", " perpetually-tired",
                     " twice-cursed", " therian", "n elven", " dwarven", " shifty", "n eldritch", " void-sent",
                     "n unthanked", "n unseen", " sinister", " wicked"]
    return choice(personalities)


def get_male_name() -> str:
    names = ["Shinji", "Roger", "Eve", "Gary", "Terry", "Nick", "Sean", "Henry", "Aidan",
             "Tye", "Faris", "Vincent", "Jean", "Marty", "Volk", "Prince", "Alan",
             "Lowen", "Mars", "Luther", "Lecter", "Leo", "Eugene", "Jack", "Alex", "Vinny",
             "Zane", "Zachary", "Dustin", "Paul", "John", "Dirk", "Jake", "Dave", "Manuel",
             "Hanneman", "Raphael", "Claude", "Dimitri", "Davis", "Jim", "Dan", "Arthur"]
    return choice(names)


def get_female_name() -> str:
    names = ["Asuka", "Rei", "Elly", "Catherine", "Ann", "Lily", "Aeleen", "Melany",
             "Alana", "Louise", "Noelle", "Mary", "Sophie", "Sophia", "Gabby", "Rebecca",
             "Hanna", "Vanessa", "Illya", "Alex", "Veronica", "Soleil", "Eirika", "Rose",
             "Roxy", "Jade", "Jane", "Jessie", "Ruth", "Marianne", "Aysha", "Erin",
             "Eve", "Eden", "Philia", "Yona", "Janelle", "Chloe", "Jaiden", "Wendy"]
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


def get_extended_bio(pronoun: list, name: str, gender: int) -> str:
    ext_bio = [f"{name} has a stern neutral expression, but {pronoun[0]} couldn't hurt a fly.",
               f"Once, masquerading under the guise of a merchant, {name} made a fortune from swindling the rich.",
               f"Long ago, {name} lead a clandestine vigilante organization. "
               f"{pronoun[0].title()} cannot afford to be found.",
               f"Whispers on the wind tell of another with {name}'s face. These whispers are soon extinguished.",
               f"As years pass and the seasons change, {name} stays the same."
               f" There are none among the living who remember how this came to be.",
               f"After angering a witch, {name} was placed under a curse which "
               f"stole {pronoun[2]} ability to remember faces.",
               f"The world would soon end; this, {name} believed. But that's fine, {name} also believed.",
               f"{name} can play almost any instrument perfectly, but is prone to breaking them.",
               f"{name} is loved by animals, and loves animals in return.",
               f"{name} didn't mean mean to end up here, but that's quite alright to {pronoun[1]}.",
               f"'Here for a good time, not a long time' is {pronoun[2]} motto. "
               f"{pronoun[2].title()} friends think {pronoun[0]} should get a better motto.",
               f"'Get in the robot, {name}.' {name} still thinks about that day, and shutters.",
               f"Yelling loudly is {pronoun[2]} greatest talent. 'It ain't easy,' {name} is quick to insist.",
               f"Many regard {name} as a hero, but {pronoun[0]} insist{'s' if gender != 3 else ''} that {pronoun[0]} "
               f"{'was' if gender != 3 else 'were'} simply at the right place at the right time.",
               f"{name} once won a curry competition. {pronoun[0]} refuses to elaborate further.",
               f"'There are many things to see in this world,' {name} commonly says, 'and I've seen them all.' "
               f"{name} is not telling the truth.",
               f"A goddess granted {name} the ability to see the fates of those around {pronoun[1]}. Whether this is"
               f" a blessing or a curse remains to be seen."]
    return choice(ext_bio)


def create_randomized_bio(gender: int, name: str) -> str:
    personality = get_personality_type()
    pronoun = get_pronoun_list(gender)
    land = get_land(pronoun)
    ext_bio = get_extended_bio(pronoun, name, gender)

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
    user_controller.available_user_characters.append(new_character.name)
    user_controller.available_user_characters.append(new_character.bio)
    return new_character.bio


if __name__ == "__main__":
    main()
