from character_creation import CharacterInfo, get_pronoun_list
from character_classes import *


def convert_character_to_dictionary(character):
    class_dict = {'class': character.stats.__class__.__name__,
                  'hp': character.stats.hp,
                  'mp': character.stats.mp,
                  'attack': character.stats.attack,
                  'magic_attack': character.stats.magic_attack,
                  'defence': character.stats.defence,
                  'resistance': character.stats.resistance,
                  'description': character.stats.description,
                  'rarity': character.stats.rarity,
                  'exp': character.stats.exp}

    char_dict = {'gender': character.gender,
                 'name': character.name,
                 'bio': character.bio,
                 'stats': class_dict}

    return char_dict


def convert_dictionary_to_character(dictionary):
    make_classes = {"Warrior": Warrior, "Mage": Mage, "Thief": Thief, "Brawler": Brawler,
                    "Priest": Priest, "DarkKnight": DarkKnight}
    char_class = make_classes[dictionary['stats']['class']]()

    char_class.hp = dictionary['stats']['hp']
    char_class.mp = dictionary['stats']['mp']
    char_class.attack = dictionary['stats']['attack']
    char_class.magic_attack = dictionary['stats']['magic_attack']
    char_class.defence = dictionary['stats']['defence']
    char_class.resistance = dictionary['stats']['resistance']
    char_class.description = dictionary['stats']['description']
    char_class.rarity = dictionary['stats']['rarity']
    char_class.exp = dictionary['stats']['exp']

    character = CharacterInfo()
    character.gender = dictionary['gender']
    character.name = dictionary['name']
    character.bio = dictionary['bio']
    character.stats = char_class

    return character
