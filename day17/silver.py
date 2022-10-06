from collections import defaultdict
from itertools import product


def neigh(x, y, z):

    for _x, _y, _z in product([-1, 0, 1], repeat=3):
        if _x == 0 and _y == 0 and _z == 0:
            continue

        yield x + _x, y + _y, z + _z


def evolve(data):

    new_data = defaultdict(lambda: '.')

    min_x = min(k[0] for k in data)
    max_x = max(k[0] for k in data)
    min_y = min(k[1] for k in data)
    max_y = max(k[1] for k in data)
    min_z = min(k[2] for k in data)
    max_z = max(k[2] for k in data)

    for x, y, z in product(range(min_x-1, max_x+2),
                           range(min_y-1, max_y+2),
                           range(min_z-1, max_z+2)):
        active = sum(1 for xx, yy, zz in neigh(x, y, z) if data[(xx, yy, zz)] == '#')

        if data[(x, y, z)] == '#':
            if active in {2, 3}:
                new_data[(x, y, z)] = '#'
            else:
                new_data[(x, y, z)] = '.'

        if data[(x, y, z)] == '.':
            if active in {3}:
                new_data[(x, y, z)] = '#'
            else:
                new_data[(x, y, z)] = '.'

    return new_data


def print_data(data):

    min_x = min(k[0] for k in data)
    max_x = max(k[0] for k in data)
    min_y = min(k[1] for k in data)
    max_y = max(k[1] for k in data)
    min_z = min(k[2] for k in data)
    max_z = max(k[2] for k in data)

    for z in range(min_z - 1, max_z + 2):
        screen = []

        for x in range(min_x - 1, max_x + 2):
            row = []

            for y in range(min_y - 1, max_y + 2):
                row.append(data[(x, y, z)])

            screen.append(''.join(row))

        print('\n'.join(screen))
        print('*' * 10)
        print('\n')


def solve(data):

    CYCLES = 6

    for _ in range(CYCLES):
        data = evolve(data)
    print_data(data)

    solution = sum(1 for v in data.values() if v == '#')

    return solution


def main():

    data = defaultdict(lambda: '.')

    with open('input') as in_f:
        for x, row in enumerate(in_f):
            for y, c in enumerate(row.strip()):
                data[(x, y, 0)] = c

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
