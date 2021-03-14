"""
gacca
"""
from character_creation import CharacterInfo, get_pronoun_list


def pull_information(pulls: list):
    pull_info = ""
    counter = 1

    for pull in pulls:
        pull_info += (f"<===PULL {counter}===>\n"
                      f"YOU PULLED A {pull.class_type.rarity['Rarity'].upper()} UNIT!!!\n"
                      f"NAME: {pull.name}\n"
                      f"BIO: {pull.bio}\n"
                      f"CLASS: {pull.class_type.__class__.__name__}\n\n")
        counter += 1

    return pull_info


def pull_characters(number_of_pulls: int) -> list:
    pulls = []
    for pull in range(0, number_of_pulls):
        pulls += [CharacterInfo()]

    return pulls


def main():
    pulls = pull_characters(10)
    print(pull_information(pulls))


if __name__ == "__main__":
    main()
