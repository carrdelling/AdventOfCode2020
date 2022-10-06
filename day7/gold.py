

def solve(data):

    # parse recipes
    recipes = {}
    for row in data:

        pre, post = row.strip().split(' bags contain ')

        if 'no other bags' in post:
            continue

        cpost = post.replace('.', '').replace(' bags', '').replace(' bag', '')
        clauses = [(int(x[0]), x[2:])for x in cpost.split(', ')]

        recipes[pre] = {v: k for k, v in clauses}

    bags = 0

    targets = [('shiny gold', 1)]

    while len(targets) > 0:

        new_targets = []

        for t, m in targets:
            if t not in recipes:
                continue

            req = recipes[t]

            for n, a in req.items():

                bags += (a * m)
                new_targets.append((n, a * m))

        targets = list(new_targets)

    solution = bags

    return solution


def main():

    with open('input') as in_f:
        data = [row.strip() for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
