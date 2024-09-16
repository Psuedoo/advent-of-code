class PartNumber:
    def __init__(self, number, starting_x, ending_x) -> None:
        self.number = number
        self.starting_x = starting_x
        self.ending_x = ending_x
        self.all_x_coords = range(starting_x, ending_x)


class Engine:
    def __init__(self) -> None:
        self.coord_plane = []

    def get_location(self, x_coord: int, y_coord: int):
        loc = self.coord_plane[y_coord][x_coord]
        print(f"{loc=}")
        return loc

    def get_potential_part_numbers(self):
        pass

    def is_coord_potential_part_number(self, x_coord: int, y_coord: int):
        initial_loc = self.get_location(x_coord, y_coord)

        above = y_coord - 1
        below = y_coord + 1
        right = x_coord + 1
        left = x_coord - 1

        surrounding = [
            self.get_location(x_coord, above),  # Above
            self.get_location(x_coord, below),  # Below
            self.get_location(right, y_coord),  # Right
            self.get_location(left, y_coord),  # Left
            self.get_location(left, below),  # Left Bottom Diagonal
            self.get_location(right, below),  # Right Bottom Diagonal
            self.get_location(left, above),  # Left Above Diagonal
            self.get_location(right, above),  # Right Above Diagonal
        ]

        if "*" in surrounding and initial_loc.isdigit():
            return True

        return False


with open("test_data.txt", "r") as f:
    data = f.readlines()
    engine = Engine()
    for row in data:
        engine_y = []
        for col in row:
            if col == "\n":
                continue
            engine_y.append(col)

        engine.coord_plane.append(engine_y)

    for row in engine.coord_plane:
        print(row)

    print(f"{engine.is_coord_potential_part_number(3, 0)=}")

    # TODO: Create a function that gets all of the 'potential' part numbers (numbers)
    # Then check each coord of the part number to see if it's a potential part number

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
