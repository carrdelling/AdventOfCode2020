from collections import deque


def solve(a, b):

    while len(a) > 0 and len(b) > 0:

        n_a = a.popleft()
        n_b = b.popleft()

        if n_a > n_b:
            a.append(n_a)
            a.append(n_b)
        else:
            b.append(n_b)
            b.append(n_a)

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