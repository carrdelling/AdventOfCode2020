

def solve(data):

    solution = 0

    for _id in data:

        row = int(''.join([{'F': '0', 'B': '1'}[x] for x in _id[:7]]), 2)
        col = int(''.join([{'L': '0', 'R': '1'}[x] for x in _id[7:]]), 2)

        seat = (row * 8) + col

        solution = max(solution, seat)

    return solution


def main():

    with open('input') as in_f:
        data = [row.strip() for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
