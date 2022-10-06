

def solve(tags, tickets):

    valid = set()

    for r1, r2 in tags.values():
        r_min, r_max = map(int, r1.split('-'))

        for i in range(r_min, r_max +1):
            valid.add(i)

        r_min, r_max = map(int, r2.split('-'))

        for i in range(r_min, r_max + 1):
            valid.add(i)

    # scan tickets
    missing = []
    for t in tickets[1:]:
        for n in t:
            if n not in valid:
                missing.append(n)

    return sum(missing)


def main():

    with open('input') as in_f:

        tags = {}
        tickets = []
        for row in in_f:

            if 'your ticket' in row:
                continue
            if 'nearby tickets' in row:
                continue

            if ':' in row:
                name, ranges = row.strip().split(': ')
                ranges = ranges.split(' or ')

                tags[name] = ranges

            if ',' in row:
                ticket = [int(x) for x in row.strip().split(',')]
                tickets.append(ticket)

    solution = solve(tags, tickets)

    print(solution)


if __name__ == "__main__":

    main()
