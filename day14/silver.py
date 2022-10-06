

def solve(data):

    memory = {}
    mask = None
    for s, v in data:

        if s == 'mask':
            mask = v
        else:
            addr = int(s[4:-1])
            true_mask = int(''.join('1' if x == 'X' else '0' for x in mask), 2)
            base_mask = int(''.join('0' if x == 'X' else x for x in mask), 2)

            value = int(v) & true_mask
            full_value = value | base_mask

            memory[addr] = full_value

    solution = sum(memory.values())

    return solution


def main():

    with open('input') as in_f:
        data = [x.strip().split(' = ') for x in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
