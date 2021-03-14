"""
map
"""
from random import randint, randrange


def CANNOT_MOVE_HIT_WALL() -> str:
    return "Your face impacts with the cold dungeon walls."


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


def move_player(locations: dict, x_size: int, y_size: int, player_location: list, direction: str) -> str:
    movements = {"up": [0, -1], "down": [0, 1], "left": [-1, 0], "right": [1, 0]}
    predicted_coords = player_location[:]
    predicted_coords[0] += movements[direction][0]
    predicted_coords[1] += movements[direction][1]

    if predicted_coords[0] < 0 or predicted_coords[0] >= x_size:
        return CANNOT_MOVE_HIT_WALL()
    if predicted_coords[1] < 0 or predicted_coords[1] >= y_size:
        return CANNOT_MOVE_HIT_WALL()

    player_location[0] = predicted_coords[0]
    player_location[1] = predicted_coords[1]

    # gonna need to check for combat once combat is implemented here

    return f"You move {direction}."


def main():
    player_location = [3, 2]
    locations = generate_map_locations(5, 5, player_location)
    print(get_map_information(locations, 5, 5, player_location))
    print(move_player(locations, 5, 5, player_location, "up"))
    print(move_player(locations, 5, 5, player_location, "up"))
    print(move_player(locations, 5, 5, player_location, "up"))
    print(get_map_information(locations, 5, 5, player_location))


if __name__ == "__main__":
    main()
