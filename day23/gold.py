
SIZE = 1000000


def solve(cards):

    # set up array
    location = {}

    for c, cc in zip(cards, cards[1:]):
        location[c] = cc
    location[cards[-1]] = cards[0]
    current = cards[0]

    m = max(cards)
    last = cards[-1]
    first = cards[0]

    location[last] = m + 1
    for i in range(m + 1, SIZE):
        location[i] = i + 1
    location[SIZE] = first

    # do rounds
    for _ in range(10000000):
        one = location[current]
        two = location[one]
        three = location[two]

        destination = SIZE if current == 1 else current - 1
        while destination in {one, two, three}:
            destination -= 1
            destination = SIZE if destination == 0 else destination

        location[current] = location[three]

        extra = location[destination]
        location[destination] = one
        location[three] = extra

        current = location[current]

    first = location[1]
    second = location[first]

    solution = first * second

    return solution


def main():

    with open('input') as in_f:
        value = list(map(int, in_f.readline().strip()))
    solution = solve(value)

    print(solution)


if __name__ == "__main__":

    main()
