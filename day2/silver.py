from collections import Counter


def solve(data):

    # parse each pattern e.g. 6-7 t: ztqhpbt

    valid = 0
    for pattern in data:
        rule, pwd = pattern.strip().split(':')

        count, char = rule.split(' ')
        c_min, c_max = map(int, count.split('-'))

        abc = Counter(pwd)

        if c_min <= abc[char] <= c_max:
            valid += 1

    return valid


def main():

    with open('input') as in_f:
        data = [row.strip() for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
