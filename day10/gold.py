

def solve(data):

    ways = {d: 0 for d in data}
    ways[0] = 1

    for current in sorted(ways):
        options = [d for d in ways if 3 >= (d - current) >= 1]

        for o in options:
            ways[o] += ways[current]

    solution = ways[max(ways)]

    return solution


def main():

    with open('input') as in_f:
        data = sorted([int(row.strip()) for row in in_f])

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
