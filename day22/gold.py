from collections import deque


def play_game(a, b):

    cache = set()

    rounds = 1
    while len(a) > 0 and len(b) > 0:

        signature = tuple(a) + (-1,) + tuple(b)

        if signature in cache:
            # a wins
            return a, deque([])
        cache.add(signature)

        n_a = a.popleft()
        n_b = b.popleft()

        if (len(a) < n_a) or (len(b) < n_b):
            # single round game
            if n_a > n_b:
                a.append(n_a)
                a.append(n_b)
            else:
                b.append(n_b)
                b.append(n_a)
        else:
            # recursive game
            size_a, size_b = n_a, n_b
            sub_a, sub_b = list(a)[:size_a], list(b)[:size_b]

            aa, bb = play_game(deque(sub_a), deque(sub_b))

            if len(aa) < 1:
                b.append(n_b)
                b.append(n_a)
            elif len(bb) < 1:
                a.append(n_a)
                a.append(n_b)
            else:
                assert False
        rounds += 1

    return a, b


def solve(a, b):

    a, b = play_game(a, b)

    full = [x for x in a] + [x for x in b]

    score = 0
    for m, v in enumerate(full[::-1], 1):
        score += (m * v)

    return score


def main():

    with open('input') as in_f:
        lines = in_f.read().split('\n\n')
        a = deque([int(row.strip()) for row in lines[0].split('\n')[1:]])
        b = deque([int(row.strip()) for row in lines[1].split('\n')[1:]])
    solution = solve(a, b)

    print(solution)


if __name__ == "__main__":

    main()
