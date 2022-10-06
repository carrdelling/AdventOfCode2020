

def solve(card, door):

    FACTOR = 20201227

    value = 1
    loop = 1
    for _ in range(1, FACTOR):
        value = (value * 7) % FACTOR
        if value == door:
            break
        loop += 1

    key = 1
    for _ in range(loop):
        key = (key * card) % 20201227

    return key


def main():

    data = []
    with open('input') as in_f:
        for row in in_f:
            data.append(int(row.strip()))

    solution = solve(*data)

    print(solution)


if __name__ == "__main__":

    main()