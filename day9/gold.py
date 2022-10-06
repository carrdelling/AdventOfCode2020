from collections import deque


def check(n, valid):

    for x in valid:
        t = n - x
        if t in valid:
            return True
    return False


def solve(data):

    data = list(map(int, data))
    preamble = data[:25]
    message = data[25:]

    valid = deque([x for x in preamble])
    valid_s = {x for x in preamble}

    idx = 0
    found = False
    crack = 0

    # find crack
    while not found:

        target = message[idx]

        if check(target, valid_s):
            x = valid.popleft()
            valid.append(target)
            valid_s.remove(x)
            valid_s.add(target)
        else:
            found = True
            crack = target

        idx += 1

    # build it
    left = 0
    right = 1
    acum = data[left] + data[right]

    while not acum == crack:

        if acum < crack:
            right += 1
            acum += data[right]
        else:
            acum -= data[left]
            left += 1

    min_v = min(data[left:right + 1])
    max_v = max(data[left:right + 1])

    solution = min_v + max_v

    return solution


def main():

    with open('input') as in_f:
        data = [(row.strip()) for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
