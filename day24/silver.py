from collections import deque


def solve(paths):

    black = set()

    for path in paths:
        p = deque(path)
        current = [0, 0]

        while len(p) > 0:
            op = p.popleft()
            if op in {'s', 'n'}:
                op += p.popleft()

            change = {
                'e': (0, 2),
                'w': (0, -2),
                'se': (1, 1),
                'sw': (1, -1),
                'ne': (-1, 1),
                'nw': (-1, -1),
            }[op]

            current[0] += change[0]
            current[1] += change[1]

        current = tuple(current)

        if current in black:
            black.discard(current)
        else:
            black.add(current)

    return len(black)


def main():

    data = []
    with open('input') as in_f:
        for row in in_f:
            data.append(row.strip())

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()