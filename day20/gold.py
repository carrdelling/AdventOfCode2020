import math
from collections import defaultdict


MONSTER = '''
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
'''


def parse_monster():
    monster_dots = []
    max_x, max_y = 0, 0

    for y, line in enumerate(MONSTER.splitlines()):
        for x, char in enumerate(line):
            if char == "#":
                monster_dots.append((x, y))
                max_x = max(x, max_x)
                max_y = max(y, max_y)

    return monster_dots, max_x, max_y


def find_monsters(grid, monster_dots, max_x, max_y):

    monsters = set()

    for y in range(len(grid)):
        if y + max_y >= len(grid):
            break
        for x in range(len(grid[y])):
            if x + max_x >= len(grid[y]):
                break

            is_monster = True
            for xx, yy in monster_dots:
                if grid[y + yy][x + xx] != "#":
                    is_monster = False
                    break

            if is_monster:
                for dx, dy in monster_dots:
                    monsters.add((x + dx, y + dy))

    if len(monsters) == 0:
        return None

    all_filled = set()
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == '#':
                all_filled.add((x, y))
    return len(all_filled - monsters)


def clean_borders(options, tileset):

    output = []
    for row in tileset:
        tiles = [[_l[1:-1] for _l in options[num][_id][1:-1]] for num, _id in row]

        for y in range(len(tiles[0][0])):
            new_row = [tiles[_id][x][y] for _id in range(len(tiles)) for x in range(len(tiles[_id]))]
            output.append(new_row)

    return output


def get_borders(tile):
    up = tile[0]
    down = tile[-1]
    left = [_l[0] for _l in tile]
    right = [_l[-1] for _l in tile]

    return up, right, down, left


def flip_tile(tile):

    by_col = [_l[::-1] for _l in tile]

    four_flips = tuple([tile, tile[::-1],
                        by_col, by_col[::-1]])

    return four_flips


def get_rotations(tile):

    rotations = [tile]
    last = tile
    for _ in range(3):
        tile = [_l[:] for _l in tile]
        for x in range(len(tile)):
            for y in range(len(tile[x])):
                tile[x][y] = last[len(tile[x]) - y - 1][x]
        last = tile
        rotations.append(tile)
    return tuple(rotations)


def transform(tile):
    possible = []
    for flip in flip_tile(tile):
        a = get_rotations(flip)
        if a not in possible:
            possible += a

    output = []
    for pos in possible:
        if pos not in output:
            output.append(pos)

    return output


def compute_tile_transformations(tiles):

    tile_options = {_id: transform(tile) for _id, tile in tiles.items()}

    return tile_options


def build_tile(tiled, tile_options, dimension, x=0, y=0, seen=None):

    if y == dimension:
        return tiled

    next_x = x + 1
    next_y = y

    if next_x == dimension:
        next_x = 0
        next_y += 1

    seen = seen or set()
    for _id, tiles in tile_options.items():

        if _id in seen:
            continue
        seen.add(_id)

        for trans_id, border in tiles.items():
            top, _, _, left = border

            if x > 0:
                n_id, n_trans = tiled[x - 1][y]
                _, right_n, _, _ = tile_options[n_id][n_trans]
                if right_n != left:
                    continue
            if y > 0:
                n_id, n_trans = tiled[x][y - 1]
                _, _, down_n, _ = tile_options[n_id][n_trans]
                if down_n != top:
                    continue

            tiled[x][y] = (_id, trans_id)
            output = build_tile(tiled, tile_options, dimension, x=next_x, y=next_y, seen=seen)

            if output is None:
                continue

            return output
        seen.remove(_id)

    tiled[x][y] = None

    return None


def create_tiles(tile_options):

    tile_border_options = defaultdict(dict)

    for _id, tiles in tile_options.items():
        for idx, tile in enumerate(tiles):
            tile_border_options[_id][idx] = get_borders(tile)
    dimension = math.isqrt(len(tile_options))
    tiled = [[None] * dimension for _ in range(dimension)]

    complete = build_tile(tiled, tile_border_options, dimension)

    return complete


def solve(data):

    tile_options = compute_tile_transformations(data)
    tiled = create_tiles(tile_options)

    grid = clean_borders(tile_options, tiled)

    grid_options = transform(grid)

    monster_dots, max_x, max_y = parse_monster()
    monsters = [find_monsters(option, monster_dots, max_x, max_y) for option in grid_options]
    solution = max(m for m in monsters if m is not None)

    return solution


def main():

    data = {}

    with open('input') as in_f:
        for rawTile in in_f.read().split("\n\n"):
            name, *lines = rawTile.splitlines()
            num = int(name[5:-1])
            lines = [list(l) for l in lines]
            data[num] = lines

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
