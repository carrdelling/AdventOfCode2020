from collections import defaultdict
from itertools import product


def neighbours(x, y):

    for _x, _y in product([-1, 0, 1], repeat=2):
        if _x == 0 and _y == 0:
            continue

        yield x + _x, y + _y


def evolve(area):

    new_area = defaultdict(lambda: '.')
    changed = False

    for (x, y), c in list(area.items()):

        if c == 'L':
            for nx, ny in neighbours(x, y):
                if area[(nx, ny)] == '#':
                    new_area[(x, y)] = 'L'
                    break
            else:
                new_area[(x, y)] = '#'
                changed = True

        if c == '#':
            occupied = sum(1 for nx, ny in neighbours(x, y) if area[(nx, ny)] == '#')

            if occupied >= 4:
                new_area[(x, y)] = 'L'
                changed = True
            else:
                new_area[(x, y)] = '#'

        if c == '.':
            new_area[(x, y)] = '.'

    return new_area, changed


def print_map(area):

    max_x = max(k[0] for k in area)
    max_y = max(k[1] for k in area)

    screen = []
    for x in range(max_x+1):
        row = []
        for y in range(max_y+1):
            row.append(area[(x, y)])
        screen.append(''.join(row))

    print('\n'.join(screen))
    print('\n' * 10)


def solve(area):

    evolving = True
    while evolving:
        area, evolving = evolve(area)
        print(sum(1 for k, v in area if area[(k, v)] == '#'))

    return sum(1 for k, v in area if area[(k, v)] == '#')


def main():

    area = defaultdict(lambda: '.')
    with open('input') as in_f:
        for x, row in enumerate(in_f):
            for y, c in enumerate(row.strip()):
                area[(x, y)] = c

    solution = solve(area)

    print(solution)


if __name__ == "__main__":

    main()
