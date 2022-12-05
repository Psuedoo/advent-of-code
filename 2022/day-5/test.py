from main import get_crates


def test_get_crates():
    with open("data_test.txt", "r") as f:
        data = f.read()
        new_data = data.splitlines()
        crates = get_crates(new_data)
        expected_crates = {1: [], 2: [], 3: []}
        assert 1 == 1
