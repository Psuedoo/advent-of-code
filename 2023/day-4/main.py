class Card:
    def __init__(
        self, number: int, winning_numbers: list[str], scratched_numbers: list[str]
    ):
        self.number = number
        self.winning_numbers = [int(num) for num in winning_numbers]
        self.scratched_numbers = [int(num) for num in scratched_numbers]
        self.score = 0

    def __str__(self):
        return f"{self.__dict__}"

    def double_score(self):
        if self.score == 0:
            self.score = 1
            return
        self.score += self.score

    def calculate_score(self):
        matches = [num for num in self.scratched_numbers if num in self.winning_numbers]

        for _ in matches:
            self.double_score()


with open("data.txt", "r") as f:
    data = f.readlines()
    total_score = 0
    for line in data:
        line = line.strip()
        label_split = line.split(":")
        cards_split = label_split[1].split("|")
        label = int(label_split[0].strip("Card"))

        winning_numbers = cards_split[0].strip().split(" ")
        winning_numbers = [num for num in winning_numbers if num != ""]

        scratched_numbers = cards_split[1].strip().split(" ")
        scratched_numbers = [num for num in scratched_numbers if num != ""]

        my_card = Card(
            number=label,
            winning_numbers=winning_numbers,
            scratched_numbers=scratched_numbers,
        )
        my_card.calculate_score()
        total_score += my_card.score

    print(total_score)
