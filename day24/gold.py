from collections import deque


def initial_state(paths):

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

    return black


def neighbours(x, y):

    n = ((0, 2), (0, -2), (1, 1),
         (1, -1), (-1, 1),  (-1, -1))

    for _x, _y in n:
        yield x + _x, y+_y


def solve(paths):

    state = initial_state(paths)

    for g in range(100):

        new_state = set()

        candidates = set()
        for x, y in state:
            candidates.add((x, y))
            for _x, _y in neighbours(x, y):
                candidates.add((_x, _y))

        for x, y in candidates:

            black = sum(1 for _x, _y in neighbours(x, y) if (_x, _y) in state)

            if (x, y) in state:
                if black in {1, 2}:
                    new_state.add((x, y))
            else:
                if black == 2:
                    new_state.add((x, y))

        state = {x for x in new_state}

    return len(state)


def main():

    data = []
    with open('input') as in_f:
        for row in in_f:
            data.append(row.strip())

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()