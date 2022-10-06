

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

    seek = set()

    targets = ['shiny gold']

    while len(targets) > 0:
        new_targets = []
        for k, v in recipes.items():

            valid = False
            for t in targets:
                if t in v:
                    valid = True
                    break

            if valid:
                if k not in seek:
                    seek.add(k)
                    new_targets.append(k)

        targets = list(new_targets)

    solution = len(seek)

    return solution


def main():

    with open('input') as in_f:
        data = [row.strip() for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
