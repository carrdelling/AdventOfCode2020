from collections import defaultdict
from itertools import product


def neigh(x, y, z, v):

    for _x, _y, _z, _v in product([-1, 0, 1], repeat=4):
        if _x == 0 and _y == 0 and _z == 0 and _v == 0:
            continue

        yield x + _x, y + _y, z + _z, v + _v


def evolve(data):

    new_data = defaultdict(lambda: '.')

    min_x = min(k[0] for k in data)
    max_x = max(k[0] for k in data)
    min_y = min(k[1] for k in data)
    max_y = max(k[1] for k in data)
    min_z = min(k[2] for k in data)
    max_z = max(k[2] for k in data)
    min_v = min(k[3] for k in data)
    max_v = max(k[3] for k in data)

    for x, y, z, v in product(range(min_x-1, max_x+2),
                              range(min_y-1, max_y+2),
                              range(min_z-1, max_z+2),
                              range(min_v-1, max_v+2)):
        active = sum(1 for xx, yy, zz, vv in neigh(x, y, z, v) if data[(xx, yy, zz, vv)] == '#')

        if data[(x, y, z, v)] == '#':
            if active in {2, 3}:
                new_data[(x, y, z, v)] = '#'
            else:
                new_data[(x, y, z, v)] = '.'

        if data[(x, y, z, v)] == '.':
            if active in {3}:
                new_data[(x, y, z, v)] = '#'
            else:
                new_data[(x, y, z, v)] = '.'

    return new_data


def solve(data):

    CYCLES = 6

    for _ in range(CYCLES):
        data = evolve(data)

    solution = sum(1 for v in data.values() if v == '#')

    return solution


def main():

    data = defaultdict(lambda: '.')

    with open('input') as in_f:
        for x, row in enumerate(in_f):
            for y, c in enumerate(row.strip()):
                data[(x, y, 0, 0)] = c

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
