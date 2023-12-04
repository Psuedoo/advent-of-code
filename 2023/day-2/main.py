from dataclasses import dataclass, field


@dataclass
class Game:
    number: int
    cube_sets: list = field(default_factory=list)


@dataclass
class CubeSet:
    game: Game
    cubes: list = field(default_factory=list)


@dataclass
class Cube:
    count: int
    color: str


def parse_line(line):
    new_line = line.strip("Game :")
    line_split = new_line.split(":")
    game_number = line_split[0]
    cube_sets = line_split[1].split(";")
    game = Game(number=game_number)
    parse_cube_sets(cube_sets, game)


def parse_cube_sets(cube_sets, game):
    for cube_set in cube_sets:
        cubes = cube_set.split(",")
        parse_cubes(cubes)


def parse_cubes(cube_set):
    for cube in cube_set:
        clean_cube = cube.strip()
        parsed_cube = clean_cube.split()
        obj_cube = Cube(count=int(parsed_cube[0]), color=parsed_cube[1])


with open("data.txt", "r") as f:
    data = f.readlines()
    games = []
    for line in data:
        games.append(parse_line(line))
        print(games)
