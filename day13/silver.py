

def solve(start, buses):

    available = [int(x) for x in buses if x != 'x']
    waits = sorted([((((start // b) + 1) * b) - start, b) for b in available])

    return waits[0][0] * waits[0][1]


def main():

    with open('input') as in_f:
        start = int(in_f.readline().strip())
        buses = [x for x in in_f.readline().strip().split(',')]

    solution = solve(start, buses)

    print(solution)


if __name__ == "__main__":

    main()
