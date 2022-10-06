from collections import defaultdict


def purge_tickets(valid, tickets):

    # scan tickets
    valid_tickets = []
    for t in tickets[1:]:
        wrong = False
        for n in t:
            if n not in valid:
                wrong = True
                break
        if not wrong:
            valid_tickets.append(t)

    return valid_tickets


def solve(tags, tickets):

    valid = set()
    my_ticket = tickets[0]

    for r1, r2 in tags.values():
        r_min, r_max = map(int, r1.split('-'))

        for i in range(r_min, r_max +1):
            valid.add(i)

        r_min, r_max = map(int, r2.split('-'))

        for i in range(r_min, r_max + 1):
            valid.add(i)

    good_tickets = purge_tickets(valid, tickets)

    valid = defaultdict(set)

    for name, (r1, r2) in tags.items():
        r_min, r_max = map(int, r1.split('-'))

        for i in range(r_min, r_max +1):
            valid[name].add(i)

        r_min, r_max = map(int, r2.split('-'))

        for i in range(r_min, r_max + 1):
            valid[name].add(i)

    stats = defaultdict(set)

    for ticket in good_tickets:
        for idx, n in enumerate(ticket):
            stats[idx].add(n)

    # map fields
    mapping = {}
    changes = True
    mapped_idx = set()

    while changes:
        changes = False
        candidates = defaultdict(set)
        for field_name, field_valid in valid.items():

            if field_name in mapping:
                continue

            for idx, values in stats.items():

                wrong = {x for x in values} - {x for x in field_valid}

                if len(wrong) < 1:
                    candidates[field_name].add(idx)

            if len(candidates[field_name]) == 1:
                mapping[field_name] = list(candidates[field_name])[0]
                mapped_idx.add(mapping[field_name])
                changes = True

        # flip candidates
        for idx in stats:
            if idx in mapped_idx:
                continue

            how_many = [k for k, v in candidates.items() if idx in v]

            if len(how_many) == 1:
                mapping[how_many[0]] = idx
                mapped_idx.add(idx)
                changes = True

    # work with our tickets
    result = 1
    for k, v in mapping.items():
        if 'departure' in k:
            result *= my_ticket[v]

    return result


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
