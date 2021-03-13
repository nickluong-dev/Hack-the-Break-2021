"""
map
"""
from random import randint, randrange


def generate_map_locations(x_size: int, y_size: int, player_coords: list) -> dict:
    staircase_coords = [randrange(0, x_size), randrange(0, y_size)]
    while staircase_coords == player_coords:
        staircase_coords[0] = randrange(0, x_size)

    monster_locations = []
    for _ in range(0, int(x_size * y_size / 10)):
        new_monster_coords = [randrange(0, x_size), randrange(0, y_size)]
        while new_monster_coords == staircase_coords or new_monster_coords == player_coords:
            new_monster_coords[0] = randrange(0, x_size)

        monster_locations += [new_monster_coords]

    return {"monsters": monster_locations, "staircase": staircase_coords}


def get_location_type(locations: dict, x: int, y: int, player_location: list):
    for location in locations["monsters"]:
        if location[0] == x and location[1] == y:
            return "M"
    if locations["staircase"][0] == x and locations["staircase"][1] == y:
        return "S"
    if player_location[0] == x and player_location[1] == y:
        return "P"
    return "X"


def get_map_information(locations: dict, x_size: int, y_size: int, player_location: list) -> str:
    information = ""
    for y in range(0, y_size):
        information += "["
        for x in range(0, x_size - 1):
            information += f"{get_location_type(locations, x, y, player_location)} "
        information += f"{get_location_type(locations, x_size - 1, y, player_location)}]\n"

    return information


def main():
    locations = generate_map_locations(5, 5, [3, 2])
    print(get_map_information(locations, 5, 5, [3, 2]))


if __name__ == "__main__":
    main()
