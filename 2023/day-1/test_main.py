from main import get_word_numbers


def read_test_data():
    with open("test_data.txt", "r") as f:
        return f.readlines()


def test_get_word_numbers():
    data = read_test_data()
    my_numbers = []
    for line in data:
        my_numbers.append(get_word_numbers(line))

    print(my_numbers)


test_get_word_numbers()
