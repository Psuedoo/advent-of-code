import math


class Safe:
    def __init__(self, name):
        self.name = name

        self.position = 50
        self.highest_position = 99
        self.zero_counter = 0

    def calculate_zero_passes(self, steps):
        zero_counts = (self.position + steps) // (self.highest_position + 1)

        return zero_counts

    def turn(self, direction, steps):

        for _ in range(1, steps + 1):

            if direction == "R":
                self.position += 1
            elif direction == "L":
                self.position -= 1

            if self.position % 100 == 0:
                self.zero_counter += 1

        self.position %= 100


files = ["test-data.txt", "data.txt"]

for file in files:
    with open(f"2025/day-1/{file}", "r") as f:
        data = f.readlines()
        safe = Safe(name=file)
        for line in data:
            direction = line[0]
            turn_count = int(line[1:])

            safe.turn(direction=direction, steps=turn_count)

        print(f"{safe.name}: {safe.zero_counter}")
