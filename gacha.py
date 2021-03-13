"""
gacca
"""
from character_creation import Character, get_pronoun_list


def pull_information(pulls: list):
    pull_info = ""
    counter = 1

    for pull in pulls:
        pull_info += (f"<===PULL {counter}===>\n"
                      f"YOU PULLED A {pull.rarity} STAR UNIT!!!\n"
                      f"NAME: {pull.name}\n"
                      f"BIO: {pull.bio}\n\n")
        counter += 1

    return pull_info


def pull_characters(number_of_pulls: int) -> list:
    pulls = []
    for pull in range(0, number_of_pulls):
        pulls += [Character()]

    return pulls


def main():
    pulls = pull_characters(10)
    print(pull_information(pulls))


if __name__ == "__main__":
    main()
