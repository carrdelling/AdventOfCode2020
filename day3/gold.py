from collections import defaultdict


def solve(grid):

    goal = max(k[0] for k in grid) + 1
    width = max(k[1] for k in grid) + 1

    policies = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1)
    ]

    trees = 1

    for px, py in policies:
        this_trees = 0
        x, y = 0, 0

        while x < goal:

            # down 1
            x += px

            # right 3
            y = (y + py) % width

            # inspect
            this_trees += 1 if grid[(x, y)] == '#' else 0

        trees *= this_trees

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
