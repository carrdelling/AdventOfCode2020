
CLOCKWISE = {
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
    (-1, 0): (0, 1),
}

COUNTER = {v: k for k, v in CLOCKWISE.items()}


def solve(data):

    direction = (0, 1)  # east
    pos = (0, 0)

    for ins, v in data:

        if ins == 'N':
            pos = pos[0] - v, pos[1]

        if ins == 'S':
            pos = pos[0] + v, pos[1]

        if ins == 'E':
            pos = pos[0], pos[1] + v

        if ins == 'W':
            pos = pos[0], pos[1] - v

        if ins in {'L', 'R'}:
            if (ins, v) in {('L', 90), ('R', 270)}:
                direction = COUNTER[direction]
            elif (ins, v) in {('L', 270), ('R', 90)}:
                direction = CLOCKWISE[direction]
            elif v == 180:
                direction = (-direction[0], -direction[1])
            elif v == 360:
                continue
            else:
                assert False, f"Bad ins f{ins, v}"

        if ins == 'F':
            pos = pos[0] + (direction[0] * v), pos[1] + (direction[1] * v)

    manhattan = abs(pos[0]) + abs(pos[1])

    return manhattan


def main():

    with open('input') as in_f:
        data = [(row.strip()) for row in in_f]
        data = [(x[0], int(x[1:])) for x in data]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
