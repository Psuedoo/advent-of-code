POSSIBLE_COUNTS = {"red": 12, "green": 13, "blue": 14}
POSSIBLE_COLORS = ["red", "green", "blue"]


class Cube:
    def __init__(self, color: str, count: int):
        self.color = color
        self.count = count

    def is_possible(self):
        return self.count <= POSSIBLE_COUNTS[self.color]


class Grab:
    def __init__(self) -> None:
        self.cubes = []
        self.total_red = 0
        self.total_green = 0
        self.total_blue = 0

    def add_cubes(self, cubes: list[str]):
        for cube in cubes:
            count, color = cube.strip().split(" ")
            self.cubes.append(Cube(color=color, count=int(count)))

    def is_possible(self):
        return False not in [cube.is_possible() for cube in self.cubes]

    def set_total_color_counts(self):
        for cube in self.cubes:
            match cube.color:
                case "red":
                    self.total_red += cube.count
                case "green":
                    self.total_green += cube.count
                case "blue":
                    self.total_blue += cube.count


class Game:
    def __init__(self, label: str):
        self.label = label
        self.grabs = []
        self.min_red = 0
        self.min_green = 0
        self.min_blue = 0
        self.power_of_cubes = 0

    @property
    def number(self):
        str_number = self.label.split(" ")[1].strip()
        return int(str_number)

    def add_grab(self, grab: Grab):
        self.grabs.append(grab)

    def is_possible(self):
        return False not in [grab.is_possible() for grab in self.grabs]

    def set_min_possible_colors(self):
        for grab in self.grabs:
            grab.set_total_color_counts()

            if grab.total_red > self.min_red or self.min_red == 0:
                self.min_red = grab.total_red

            if grab.total_green > self.min_green or self.min_green == 0:
                self.min_green = grab.total_green

            if grab.total_blue > self.min_blue or self.min_blue == 0:
                self.min_blue = grab.total_blue

    def set_power_of_cubes(self):
        self.power_of_cubes = self.min_red * self.min_green * self.min_blue


with open("data.txt", "r") as f:
    data = f.readlines()
    games = []
    total_possible_count = 0
    total_powers = 0

    for line in data:
        clean_line = line.strip()
        split = clean_line.split(":")
        game_label = split[0].strip()
        curr_game = Game(label=game_label)
        games.append(curr_game)

        grabs = split[1].split(";")
        # Cleaning grab
        for grab in grabs:
            cubes = grab.split(",")
            curr_grab = Grab()
            curr_grab.add_cubes(cubes=cubes)
            curr_game.add_grab(curr_grab)

    for game in games:
        game.set_min_possible_colors()
        game.set_power_of_cubes()
        total_powers += game.power_of_cubes

    print(total_powers)
