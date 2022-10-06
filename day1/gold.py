from itertools import product


def solve(data):

    solution = None
    for a, b, c in product(data, repeat=3):

        if a+b+c == 2020:
            solution = a * b * c
            break

    return solution


def main():

    with open('input') as in_f:
        data = [int(row.strip()) for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
