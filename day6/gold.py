
def process(text):

    common = {a for a in list(text[0]) if a not in {' ', '\n'}}
    for x in text[1:]:
        common &= {a for a in list(x) if a not in {' ', '\n'}}

    return len(common)


def solve(data):

    solution = 0

    answers = []
    for row in data:

        if len(row) > 0:
            answers.append(row)
        else:
            solution += process(answers)
            answers = []
    else:
        solution += process(answers)

    return solution


def main():

    with open('input') as in_f:
        data = [row.strip() for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
