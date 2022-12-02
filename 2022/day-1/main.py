with open("data.txt", "r") as f:
    data = f.read()
    new_data = data.splitlines()
    elves = []
    cal_count = 0
    for line in new_data:
        if line == "":
            elves.append(cal_count)
            cal_count = 0
            continue
        else:
            cal_count += int(line)

    fattest_elves = sorted(elves, reverse=True)
    total = 0
    for elves in fattest_elves[:3]:
        total += elves
        print(total)
