from character_creation import CharacterInfo, get_pronoun_list


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
