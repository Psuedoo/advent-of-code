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
        # breakpoint()
        if direction == "R":
            self.zero_counter += self.calculate_zero_passes(steps)
            self.position += steps
            self.position %= 100
        elif direction == "L":
            self.position -= steps
            self.position %= 100
            self.zero_counter += self.calculate_zero_passes(steps)


files = ["lol.txt", "test-data.txt", "data.txt"]
# files = ["lol.txt", "test-data.txt"]

for file in files:
    with open(f"2025/day-1/{file}", "r") as f:
        data = f.readlines()
        safe = Safe(name=file)
        for line in data:
            direction = line[0]
            turn_count = int(line[1:])

            safe.turn(direction=direction, steps=turn_count)

        print(f"{safe.name}: {safe.zero_counter}")

# 6367 = too low
# 6433 = wrong
# 6463 = wrong
# 6504 = wrong
# 7267 = too high
