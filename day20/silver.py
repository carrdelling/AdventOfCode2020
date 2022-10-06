from collections import Counter
def get_signature(image):

    up = tuple(image[(0, i)] for i in range(10))
    down = tuple(image[(9, i)] for i in range(10))
    left = tuple(image[(i, 0)] for i in range(10))
    right = tuple(image[(i, 9)] for i in range(10))

    return left, up, right, down


def solve(data):

    signatures = {k: get_signature(v) for k, v in data}

    count_s = Counter(x for s in signatures.values() for x in s)

    # see non matching
    non_matching = set()
    for s in signatures.values():
        for x in s:
            if x[::-1] not in count_s:
                non_matching.add(x)

    # count borders
    product = 1
    for k, s in signatures.items():
        weird = 0
        for x in s:
            if (x[::-1] not in count_s) and (count_s[x] == 1):
                weird += 1

        # corner tiles
        if weird > 1:
            product *= k

    return product


def main():

    data = []

    with open('input') as in_f:

        image = None

        for row in in_f:
            if 'Tile' in row:
                _id = int(row.strip().split()[1][:-1])
                image = {}
                x = 0
                continue
            if len(row) < 3:
                data.append([_id, {k: v for k, v in image.items()}])
                image = None
                continue

            for y, c in enumerate(row.strip()):
                image[(x, y)] = c

            x += 1
        else:
            data.append([_id, {k: v for k, v in image.items()}])

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
