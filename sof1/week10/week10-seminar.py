def find_neighbors(coord, matrix):
    get_neighbor = lambda x, y: [x, y] if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and [x, y] != coord else None
    return [
        get_neighbor(x, y) for x in range(coord[0] - 1, coord[0] + 2)
        for y in range(coord[1] - 1, coord[1] + 2)
        if get_neighbor(x, y) is not None
    ]


def explore_region(neighborhood, coords, seed):
    new_coords = []
    for coord in coords:
        # if neighborhood[coord[0]][coord[1]] == 0:
        neighborhood[coord[0]][coord[1]] = seed
        neighbors = find_neighbors(coord, neighborhood)
        new_coords += [
            neighbor for neighbor in neighbors
            if neighborhood[neighbor[0]][neighbor[1]] == 0
        ]
    return new_coords


neighborhood = [[0 for i in range(8)] for j in range(8)]
seeds = {'R': [[2, 1]], 'B': [[4, 7]], 'Y': [[7, 4]]}


def seeds_is_empty(seeds):
    for seed in seeds.values():
        if seed != []:
            return False
    return True


while not seeds_is_empty(seeds):
    for seed in seeds:
        seeds[seed] = explore_region(neighborhood, seeds[seed], seed)

for row in neighborhood:
    for cell in row:
        print(str(cell) + ' ', end='')
    print()

matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
]


def find_cell(el, count):
    matrix[el[0]][el[1]] = count
    neighbors = find_neighbors(el, matrix)
    for neighbor in neighbors:
        if matrix[neighbor[0]][neighbor[1]] == 1:
            find_cell(neighbor, count)


count = 2
for x, row in enumerate(matrix):
    for y, el in enumerate(row):
        if el == 1:
            find_cell([x, y], count)
            count += 1

print('\n')
for row in matrix:
    for cell in row:
        print(str(cell) + ' ', end='')
    print()
