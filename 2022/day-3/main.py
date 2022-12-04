# Change group_size to 1 for first part of the puzzle
GROUP_SIZE = 3


def gen_priorities():
    LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    PRIORITIES = {}
    for index, letter in enumerate(LETTERS):
        PRIORITIES[letter] = index + 1

    return PRIORITIES


def get_sacks_total(sacks):

    PRIORITIES = gen_priorities()

    if len(sacks) > 1:
        total = 0
        for sack in sacks:
            sacks = ["".join(sack) for sack in sacks]
        for index, sack in enumerate(sacks):
            res = set(sack)
            while len(sacks) > 1:
                res = res.intersection(set(sacks[index + 1]))
                sacks.pop(index)
            total += PRIORITIES[res.pop()]
    else:
        for index, sack in enumerate(sacks):
            total = 0

            half = len(sack) // 2
            first_compartment = set(sack[:half])
            second_compartment = set(sack[half:])
            res = first_compartment.intersection(second_compartment)
            for letter in res:
                total += PRIORITIES[letter]
    return total


with open("data.txt", "r") as f:
    data = f.read()
    sacks = data.splitlines()
    total = 0

    for index, sack in enumerate(sacks):
        if index % GROUP_SIZE == 0:
            current_group = sacks[index : index + GROUP_SIZE]
            total += get_sacks_total(current_group)


print(total)
