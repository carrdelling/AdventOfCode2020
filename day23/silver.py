

class Deck:

    def __init__(self, cards):
        self.cards = [x for x in cards]
        self.current_idx = 0

    def __str__(self):
        return f"({self.current_idx}) {self.cards}"

    def do_round(self):

        # pick next three
        strip_1 = self.cards[self.current_idx + 1: self.current_idx + 4]
        strip_2 = self.cards[:3-len(strip_1)]
        strip = strip_1 + strip_2

        # set destination
        label = self.cards[self.current_idx]
        label = 9 if label == 1 else label - 1
        while label in strip:
            label = 9 if label == 1 else label - 1

        # set next current
        self.current_idx = (self.current_idx + 4) % 9
        current_value = self.cards[self.current_idx]

        # apply movements
        self.cards = [x for x in self.cards if x not in strip]

        destination_idx = 0
        while self.cards[destination_idx] != label:
            destination_idx += 1

        self.cards = self.cards[:destination_idx + 1] + strip + self.cards[destination_idx + 1:]

        self.current_idx = 0
        while self.cards[self.current_idx] != current_value:
            self.current_idx += 1

    def signature(self):

        one_index = 0
        while self.cards[one_index] != 1:
            one_index += 1

        output = self.cards[one_index + 1:] + self.cards[:one_index]
        return ''.join(map(str, output))


def solve(cards):

    game = Deck(cards)

    for _ in range(100):
        game.do_round()

    return game.signature()


def main():

    with open('input') as in_f:
        value = list(map(int, in_f.readline().strip()))
    solution = solve(value)

    print(solution)


if __name__ == "__main__":

    main()
