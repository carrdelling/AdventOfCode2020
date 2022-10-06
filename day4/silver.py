
REQUIRED_FIELDS = {

    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'

}


def process(passport):

    necessary = {x for x in REQUIRED_FIELDS}

    for row in passport:
        chunks = row.strip().split()

        for c in chunks:
            tag, rest = c.split(':')

            necessary.discard(tag)

    return len(necessary) < 1


def solve(data):

    solution = 0

    passport = []
    for row in data:

        if len(row) > 1:
            passport.append(row)
        else:
            solution += 1 if process(passport) else 0
            passport = []
    else:
        solution += 1 if process(passport) else 0

    return solution


def main():

    with open('input') as in_f:
        data = [row.strip() for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
