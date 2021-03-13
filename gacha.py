"""
gaca
"""
from character_creation import Character, get_pronoun_list


def pull_characters(number_of_pulls: int):
    pulls = []
    for pull in range(0, number_of_pulls):
        pulls += [Character()]
        print(pulls[pull].get_bio())

    return pulls


def main():
    pull_characters(10)


if __name__ == "__main__":
    main()
