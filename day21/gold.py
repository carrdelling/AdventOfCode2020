

def solve(data):

    mapping = {}
    change = True

    while change:
        change = False

        common = {}

        for food, alerg in data:
            for a in alerg:
                if a in mapping.values():
                    continue
                if a in common:
                    common[a] &= food
                else:
                    common[a] = {x for x in food}

        for d, v in common.items():
            if len(v) == 1:
                mapping[list(v)[0]] = d
                change = True

        new_data = []
        for food, alerg in data:
            new_r = [
                {x for x in food if x not in mapping},
                {x for x in alerg if x not in mapping.values()},
            ]
            new_data.append(new_r)

        data = new_data

    canonical = ','.join(x[0] for x in sorted(mapping.items(), key=lambda x: x[1]))

    return canonical


def main():

    data = []

    with open('input') as in_f:
        for row in in_f:
            food, alerg = row.strip().replace(')', '').split(' (contains ')
            recipe = ({x.strip() for x in food.split()}, {x.strip() for x in alerg.split(', ')})
            data.append(recipe)

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()