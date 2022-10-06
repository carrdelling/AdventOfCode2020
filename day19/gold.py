

def parse(state, available, rules):

    if len(state) < 1:
        return len(available) < 1

    # nor rules to apply is bad
    if len(available) < 1:
        return False

    next_rule = available[0]
    r = rules[next_rule]

    # check terminal
    if '"' in r:
        if state[0] in r:
            return parse(state[1:], available[1:], rules)
        else:
            return False  # bad terminal
    else:
        return any(parse(state, t + available[1:], rules) for t in r)  # check all posibilities


def solve(data, rules):

    return sum(1 for m in data if parse(m, [0], rules))


def parse_rule(s):

    pre, post = s.split(": ")
    if '"' not in post:
        post = [[int(v) for v in t.split()] for t in post.split("|")]

    return int(pre), post


def main():

    rules = {}
    data = []

    with open('input') as in_f:

        for row in in_f:
            if ':' in row:
                pre, post = parse_rule(row.strip())
                rules[pre] = post
            elif len(row) > 3:
                data.append(row.strip())

        # gold changes
        new_rules = ["8: 42 | 42 8", "11: 42 31 | 42 11 31"]
        for r in new_rules:
            pre, post = parse_rule(r.strip())
            rules[pre] = post

    solution = solve(data, rules)

    print(solution)


if __name__ == "__main__":

    main()
