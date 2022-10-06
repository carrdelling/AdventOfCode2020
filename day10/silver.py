from collections import Counter


def solve(data):

    diffs = Counter([y - x for x, y in zip(data, data[1:])] + [min(data), 3])

    return diffs[1] * diffs[3]


def main():

    with open('input') as in_f:
        data = sorted([int(row.strip()) for row in in_f])

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
