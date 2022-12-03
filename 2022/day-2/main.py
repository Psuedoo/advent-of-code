def get_score(opponent, you, outcome_based=False):
    translate_move = {"X": "A", "Y": "B", "Z": "C"}
    outcomes = {
        "A": {
            "A": 4,  # Rock vs Rock = 4
            "B": 8,  # Rock vs Paper = 8
            "C": 3,  # Rock vs Scissors = 3
        },
        "B": {
            "B": 5,  # Paper vs Paper = 5
            "C": 9,  # Paper vs Scissors = 9
            "A": 1,  # Paper vs Rock = 1
        },
        "C": {
            "C": 6,  # Scissors vs Scissors = 6
            "A": 7,  # Scissors vs Rock = 7
            "B": 2,  # Scissors vs Paper = 2
        },
    }
    if outcome_based:
        translate_move = {"X": "Loss", "Y": "Tie", "Z": "Win"}
        outcomes = {
            "A": {"Loss": 3, "Tie": 4, "Win": 8},
            "B": {"Loss": 1, "Tie": 5, "Win": 9},
            "C": {"Loss": 2, "Tie": 6, "Win": 7},
        }
    you = translate_move[you]
    return outcomes[opponent][you]


with open("data.txt", "r") as f:
    data = f.read()
    new_data = data.splitlines()
    total_score = 0

    for line in new_data:
        choices = line.split()

        # To switch to part 2, change outcome_based to True
        score = get_score(choices[0], choices[1], outcome_based=False)
        total_score += score
    print(total_score)
