import math


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def solve(start, buses):

    mods = [(idx, int(b)) for idx, b in enumerate(buses) if b != 'x']
    print(mods)

    current = 0
    step = mods[0][1]
    pointer = 1
    while pointer < len(mods):
        req = mods[pointer]
        offset = req[0]
        cycle = req[1]
        if (current + offset) % cycle == 0:
            step = lcm(step, cycle)
            pointer = pointer + 1
        else:
            current = current + step

    return current


def main():

    with open('input') as in_f:
        start = int(in_f.readline().strip())
        buses = [x for x in in_f.readline().strip().split(',')]

    solution = solve(start, buses)

    print(solution)


if __name__ == "__main__":

    main()
