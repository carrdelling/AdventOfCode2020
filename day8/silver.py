

def solve(program):

    acum = 0
    ip = 0
    seen = set()
    repeat = False

    while not repeat:

        seen.add(ip)

        ins, value = program[ip]

        if ins == 'nop':
            ip += 1
        elif ins == 'acc':
            acum += value
            ip += 1
        elif ins == 'jmp':
            ip += value

        if ip in seen:
            repeat = True

    solution = acum

    return solution


def main():

    with open('input') as in_f:
        data = [row.strip().split() for row in in_f]
        data = [(x[0], int(x[1])) for x in data]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
