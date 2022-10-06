

def find(c, exp):

    for idx in range(len(exp)):
        if exp[idx] == c:
            return idx

    return -1


def compute(exp):

    while len(exp) > 1:

        bracket = find('(', exp)

        # there are brackets
        if bracket > -1:
            level = 1
            pos = bracket + 1

            while level > 0:
                if exp[pos] == '(':
                    level += 1
                if exp[pos] == ')':
                    level -= 1
                pos += 1

            exp = exp[:bracket] + compute(exp[bracket + 1:pos - 1]) + exp[pos:]
            continue

        # no brackets
        plus = find('+', exp)

        while plus > -1:
            exp = exp[:plus-1] + [exp[plus-1] + exp[plus+1]] + exp[plus+2:]
            plus = find('+', exp)

        mul = find('*', exp)

        while mul > -1:
            exp = exp[:mul-1] + [exp[mul-1] * exp[mul+1]] + exp[mul + 2:]
            mul = find('*', exp)

    return exp


def solve(data):

    solution = sum(compute(exp)[0] for exp in data)

    return solution


def _force_parse(x):

    try:
        return int(x)
    except:
        return x


def main():

    data = []

    with open('input') as in_f:

        for row in in_f:
            eq = []
            for c in row.strip():
                if c != ' ':
                    x = _force_parse(c)
                    eq.append(x)
            data.append(eq)

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
