

REQUIRED_FIELDS = {

    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'

}


def valid(tag, rest):

    if tag in {'hgt'}:
        if 'in' in rest:
            try:
                if 59 <= int(rest[:-2]) <= 76:
                    return True
            except:
                pass

        if 'cm' in rest:
            try:
                if 150 <= int(rest[:-2]) <= 193:
                    return True
            except:
                pass

    if tag in {'byr'}:
        if len(rest) == 4 and 1920 <= int(rest) <= 2002:
            return True

    if tag in {'iyr'}:
        if len(rest) == 4 and 2010 <= int(rest) <= 2020:
            return True

    if tag in {'eyr'}:
        if len(rest) == 4 and 2020 <= int(rest) <= 2030:
            return True

    if tag in {'pid'}:
        if rest.isdigit() and len(rest) == 9:
            return True

    if tag in {'ecl'}:
        if rest in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
            return True

    if tag in {'hcl'}:

        _valid = rest[0] == '#' and len(rest) == 7
        for c in rest[1:]:
            _valid &= (c.isdigit()) or (c in {'a', 'b', 'c', 'd', 'e', 'f'})

        if _valid:
            return True

    return False


def process(passport):

    necessary = {x for x in REQUIRED_FIELDS}

    for row in passport:
        chunks = row.strip().split()

        for c in chunks:
            tag, rest = c.split(':')

            if valid(tag, rest):
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
