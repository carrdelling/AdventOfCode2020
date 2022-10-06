from collections import defaultdict


def solve(grid):

    x, y = 0, 0
    goal = max(k[0] for k in grid) + 1
    width = max(k[1] for k in grid) + 1

    trees = 0
    while x < goal:

        # down 1
        x += 1

        # right 3
        y = (y + 3) % width

        # inspect
        trees += 1 if grid[(x, y)] == '#' else 0

    return trees


def main():

    grid = defaultdict(lambda: '.')
    with open('input') as in_f:
        for x, row in enumerate(in_f):
            for y, c in enumerate(row.strip()):
                grid[(x, y)] = c

    solution = solve(grid)

    print(solution)


if __name__ == "__main__":

    main()
