

def trace(program):

    acum = 0
    ip = 0
    seen = set()
    repeat = False

    while not repeat and ip < len(program):

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

    if repeat:
        return -1

    return acum


def solve(program):

    solution = 0

    for i in range(len(program)):

        new_program = list(program)

        if program[i][0] == 'nop':
            new_program[i] = ('jmp', program[i][1])

        if program[i][0] == 'jmp':
            new_program[i] = ('nop', program[i][1])

        if program[i][0] == 'acc':
            continue

        value = trace(new_program)

        if value > -1:
            solution = value
            break

    return solution


def main():

    with open('input') as in_f:
        data = [row.strip().split() for row in in_f]
        data = [(x[0], int(x[1])) for x in data]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
