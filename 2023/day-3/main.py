class PartNumber:
    def __init__(self, number, y, starting_x, ending_x) -> None:
        self.number = number
        self.y = y
        self.starting_x = starting_x
        self.ending_x = ending_x
        self.all_x_coords = range(starting_x, ending_x + 1)

    def __str__(self):
        return str(self.__dict__)


class Gear:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Engine:
    def __init__(self) -> None:
        self.coord_plane = []

    def get_location(self, x_coord: int, y_coord: int):
        try:
            return self.coord_plane[y_coord][x_coord]
        except IndexError:
            return None

    def get_potential_gears(self):
        pontential_gears = []
        for y_index, row in enumerate(self.coord_plane):
            for x_index, char in enumerate(row):
                if char == "*":
                    pontential_gears.append(Gear(x=x_index, y=y_index))

    def is_gear_valid(self, gear: Gear):
        # TODO: Implement function to check if gear is surrounded by part number
        part_numbers = self.get_valid_part_numbers()
        pass

    def get_gear_ratio(self, gear: Gear):
        # TODO: Implement function to multiply surrounding part numbers
        pass

    def get_gear_ratio_sum(self):
        # TODO: Get all valid gears
        # Get their ratios
        # Add them up
        pass

    def get_potential_part_numbers(self):
        part_numbers = []
        for y_index, row in enumerate(self.coord_plane):
            str_part_number = ""
            y = ""
            starting_x = ""

            for x_index, char in enumerate(row):
                if char.isdigit():

                    # If this is the leftmost digit in a number, we should capture the starting point
                    if not str_part_number:
                        y = y_index
                        starting_x = x_index

                    str_part_number += char

                if str_part_number and not char.isdigit():

                    part_number = PartNumber(
                        number=int(str_part_number),
                        y=y,
                        starting_x=starting_x,
                        ending_x=x_index - 1,
                    )
                    part_numbers.append(part_number)
                    str_part_number = ""

            if str_part_number:
                part_number = PartNumber(
                    number=int(str_part_number),
                    y=y,
                    starting_x=starting_x,
                    ending_x=len(row) - 1,
                )
                part_numbers.append(part_number)
                str_part_number = ""

        return part_numbers

    def is_valid_part_number(self, part_number: PartNumber):
        for x_coord in part_number.all_x_coords:

            if self.is_coord_potential_part_number(
                x_coord=x_coord, y_coord=part_number.y
            ):
                return True

        return False

    def is_coord_potential_part_number(self, x_coord: int, y_coord: int):
        initial_loc = self.get_location(x_coord, y_coord)
        if not initial_loc or not initial_loc.isdigit():
            return False

        above = y_coord - 1
        below = y_coord + 1
        right = x_coord + 1
        left = x_coord - 1

        if left < 0:
            left = 0

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

        for char in surrounding:
            if not char:
                continue

            if char == ".":
                continue

            if char.isalnum():
                continue

            if char.isdigit():
                continue

            return True

        return False

    def get_valid_part_numbers(self):

        part_numbers = engine.get_potential_part_numbers()

        valid_part_numbers = []

        for part_number in part_numbers:
            if engine.is_valid_part_number(part_number):
                valid_part_numbers.append(part_number)
            else:
                print(f"{part_number} failed the checks")

        return valid_part_numbers


with open("data.txt", "r") as f:
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

    valid_part_numbers = engine.get_valid_part_numbers()

    print(sum([pn.number for pn in valid_part_numbers]))
