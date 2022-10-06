from collections import deque


def expand(mask, pattern):

    states = [(deque(x for x in mask), deque(x for x in pattern), '')]

    while states:

        m, p, o = states.pop()

        if len(m) < 1:
            yield o
            continue

        nm = m.popleft()
        np = p.popleft()

        if nm == '0':
            o += np
            new_state = (deque(m), deque(p), o)
            states.append(new_state)

        if nm == '1':
            o += '1'
            new_state = (deque(m), deque(p), o)
            states.append(new_state)

        if nm == 'X':
            oo = o + '0'
            new_state = (deque(m), deque(p), oo)
            states.append(new_state)

            oo = o + '1'
            new_state = (deque(m), deque(p), oo)
            states.append(new_state)


def solve(data):

    memory = {}
    mask = None
    for s, v in data:

        if s == 'mask':
            mask = v
        else:
            addr = int(s[4:-1])
            b_addr = f'{addr:036b}'

            for rp in expand(mask, b_addr):
                memory[rp] = int(v)

    solution = sum(memory.values())

    return solution


def main():

    with open('input') as in_f:
        data = [x.strip().split(' = ') for x in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
