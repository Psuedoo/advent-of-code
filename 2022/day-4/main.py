def check_sets(set_one, set_two, check_fully_contained):
    # Check fully contained is part one of the solution
    if check_fully_contained:
        return set_one.issubset(set_two) or set_two.issubset(set_one)
    if set_one.intersection(set_two):
        return True
    return False


with open("data.txt") as f:
    data = f.read()
    pairs = data.splitlines()
    results = []
    for pair in pairs:
        sections = pair.split(",")

        sections[0] = set(
            range(int(sections[0].split("-")[0]), int(sections[0].split("-")[1]) + 1)
        )
        sections[1] = set(
            range(int(sections[1].split("-")[0]), int(sections[1].split("-")[1]) + 1)
        )

        results.append(
            check_sets(sections[0], sections[1], check_fully_contained=False)
        )

    print(results.count(True))
