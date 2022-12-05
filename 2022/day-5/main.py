from dataclasses import dataclass, field


@dataclass
class Crate:
    name: str


@dataclass
class Column:
    position: int
    crates: list = field(default_factory=list)

    def get_highest(self):
        return self.crates[0]

    def move_crates(self, crate_count, new_column):
        for x in range(crate_count):
            new_column.crates.insert(0, self.crates.pop(crate_count - 1))
            crate_count -= 1


def get_columns(data):
    columns = []
    for line in data:
        if "[" not in line:
            columns = [Column(position=pos) for pos in line.split()]
            break
    return columns


def populate_crates(data, columns):
    column_range = len(columns) * 4
    for line_index, line in enumerate(data):
        if "[" not in line:
            break
        for index, char in enumerate(line):
            if char == "[":
                if index < column_range:
                    column = columns[index // 4]
                    crate = Crate(name=line[index + 1])
                    column.crates.append(crate)


def get_instructions(data):
    instructions = []

    for line in data:
        if line.startswith("move"):
            instructions.append(line.split())
    for instruction in instructions:
        instruction.pop(0)
        instruction.pop(1)
        instruction.pop(2)

    return instructions


def run_instructions(instructions, columns):
    for instruction in instructions:
        count = int(instruction[0])
        from_col = columns[int(instruction[1]) - 1]
        to_col = columns[int(instruction[2]) - 1]
        from_col.move_crates(count, to_col)


with open("data.txt", "r") as f:
    data = f.read()
    new_data = data.splitlines()
    columns = get_columns(new_data)
    populate_crates(new_data, columns)
    i = get_instructions(new_data)
    run_instructions(i, columns)
    for x in columns:
        print(x.get_highest())
