from linereader import read_parts

d = read_parts('13.in.txt', '', split_instructions=['points', 'instructions'])


def print_arr(arr):
    x = 0
    y = 0

    for p in arr:
        if p[0] > x:
            x = p[0]
        if p[1] > y:
            y = p[1]

    mat = []
    for row in range(0, y + 1):
        vec = []
        for col in range(0, x + 1):
            vec.append('    ')

        mat.append(vec)

    for p in arr:
        mat[p[1]][p[0]] = '|-| '

    for row in mat:
        for col in row:
            print(col, end='')
        print()


instructions = [(y[0], int(y[2:])) for y in [x.split('fold along ')[1] for x in d['instructions']]]
points = [[int(p[0]), int(p[1])] for p in [x.split(',') for x in d['points']]]


def remove_duplicates(lst):
    return [[t[0], t[1]] for t in (set(tuple(i) for i in lst))]


# 602, 683 ----- along 655
for fold in instructions:
    plane, position = fold

    if plane == 'y':
        for i, point in enumerate(points):
            if point[1] > position:
                points[i][1] = position - abs(position - point[1])
    else:
        for i, point in enumerate(points):
            if point[0] > position:
                points[i][0] = position - abs(position - point[0])

    points = remove_duplicates(points)

print_arr(points)