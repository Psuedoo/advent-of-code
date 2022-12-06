with open("data.txt", "r") as f:
    data = f.read()
    for index, char in enumerate(data):
        # Change 14 to 4 for part one
        if len(set(data[index - 14 : index])) == 14:
            print(index)
            break
