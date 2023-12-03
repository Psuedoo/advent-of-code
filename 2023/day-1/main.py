NUMBERS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_digit_numbers(line):
    my_numbers = []

    for index, char in enumerate(line):
        if char.isdigit():
            my_numbers.append({"index": index, "number": char})

    return my_numbers


def get_word_numbers(line):
    my_numbers = []

    for number in NUMBERS.keys():
        if number in line:
            index = line.find(number)
            my_numbers.append({"index": index, "number": NUMBERS[number]})

    return my_numbers


def get_numbers(line):
    raw_numbers = []

    raw_numbers.append(get_digit_numbers(line))
    raw_numbers.append(get_word_numbers(line))

    my_numbers = flatten_array(raw_numbers)

    sorted_numbers = sorted(my_numbers, key=lambda d: d["index"])

    try:
        first_number = sorted_numbers[0]["number"]
        last_number = sorted_numbers[-1]["number"]
        return int("".join([first_number, last_number]))
    except IndexError:
        return 0
        pass  # lol idk


def flatten_array(array):
    flat_array = []
    for arr in array:
        for item in arr:
            flat_array.append(item)

    return flat_array


with open("data.txt", "r") as f:
    data = f.readlines()
    coord_numbers = []
    for line in data:
        numbers = get_numbers(line)
        coord_numbers.append(numbers)

    print(coord_numbers)

    coords = sum(coord_numbers)
    print(coords)
