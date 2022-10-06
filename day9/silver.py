from collections import deque


def check(n, valid):

    for x in valid:
        t = n - x
        if t in valid:
            return True
    return False


def solve(data):

    preamble = list(map(int, data[:25]))
    message = list(map(int, data[25:]))

    valid = deque([x for x in preamble])
    valid_s = {x for x in preamble}

    idx = 0
    found = False
    solution = 0

    while not found:

        target = message[idx]

        if check(target, valid_s):
            x = valid.popleft()
            valid.append(target)
            valid_s.remove(x)
            valid_s.add(target)
        else:
            found = True
            solution = target

        idx += 1

    return solution


def main():

    with open('input') as in_f:
        data = [(row.strip()) for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
