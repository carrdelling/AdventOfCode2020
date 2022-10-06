

def solve(data):

    seen = set()

    product = None
    for d in data:
        rest = 2020 - d

        if rest in seen:
            product = d * rest
            break

        seen.add(d)

    return product


def main():

    with open('input') as in_f:
        data = [int(row.strip()) for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
