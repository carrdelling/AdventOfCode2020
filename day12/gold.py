
CLOCKWISE = {
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
    (-1, 0): (0, 1),
}

COUNTER = {v: k for k, v in CLOCKWISE.items()}


def solve(data):

    pos = (0, 0)
    waypoint = (-1, 10)

    for ins, v in data:

        if ins == 'N':
            waypoint = waypoint[0] - v, waypoint[1]

        if ins == 'S':
            waypoint = waypoint[0] + v, waypoint[1]

        if ins == 'E':
            waypoint = waypoint[0], waypoint[1] + v

        if ins == 'W':
            waypoint = waypoint[0], waypoint[1] - v

        if ins in {'L', 'R'}:
            if (ins, v) in {('L', 90), ('R', 270)}:
                waypoint = -waypoint[1], waypoint[0]
            elif (ins, v) in {('L', 270), ('R', 90)}:
                waypoint = waypoint[1], -waypoint[0]
            elif v == 180:
                waypoint = -waypoint[0], -waypoint[1]
            elif v == 360:
                continue
            else:
                assert False, f"Bad ins f{ins, v}"

        if ins == 'F':
            pos = pos[0] + (waypoint[0] * v), pos[1] + (waypoint[1] * v)

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
