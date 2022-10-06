from collections import deque


def compute(exp):

    acum = 0
    mode = '+'

    while exp:
        v = exp.popleft()

        if isinstance(v, int):
            if mode == '+':
                acum += v
            if mode == '*':
                acum *= v
            continue

        if v in {'+', '*'}:
            mode = v

        if v == ')':
            return acum, exp

        if v == '(':
            inner_acum, rest = compute(exp)

            exp = rest

            if isinstance(inner_acum, int):
                if mode == '+':
                    acum += inner_acum
                if mode == '*':
                    acum *= inner_acum
                continue

    return acum, []


def solve(data):

    solution = sum(compute(deque(exp))[0] for exp in data)

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
