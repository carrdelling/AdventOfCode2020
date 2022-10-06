

def solve(data):
    last_said = {}
    order = 0
    value = None

    for d in data:
        last_said[int(d)] = order
        order += 1
    else:
        pos_last = 0

    while order < 2020:
        value = pos_last
        pos_last = order - last_said[value] if value in last_said else 0

        last_said[value] = order

        order += 1

    return value


def main():

    with open('input') as in_f:
        data = [x for x in in_f.readline().strip().split(',')]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
