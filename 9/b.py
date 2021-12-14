from linereader import read_file

d = [[int(y) for y in list(x)] for x in read_file('9.in.txt')]

basins = []
visited = []

height = len(d)
width = len(d[0])


def get_lowest_points(data):
    potential = []

    for i, row in enumerate(data):
        positions = sorted(range(len(row)), key=lambda x: row[x])
        reserved = []
        for pos in positions:
            if pos + 1 in reserved or pos - 1 in reserved:
                continue

            cond1 = row[pos - 1] > row[pos] if pos - 1 >= 0 else True
            cond2 = row[pos + 1] > row[pos] if pos + 1 < len(row) else True
            if cond1 and cond2:
                reserved.append(pos)
                potential.append((i, pos))

    coords = []
    for x, y in potential:
        value = data[x][y]
        cond1 = data[x - 1][y] > value if x - 1 >= 0 else True
        cond2 = data[x + 1][y] > value if x + 1 < len(data) else True
        if cond1 and cond2:
            coords.append((x, y))

    return coords


def flood_fill_util(data, x, y, points):
    if x < 0 or x >= width:
        return

    if y < 0 or y >= height:
        return

    if data[y][x] == 9 or ((y * width) + x) in visited:
        return

    points.append(data[y][x])

    visited.append((y * width) + x)

    flood_fill_util(data, x + 1, y, points)
    flood_fill_util(data, x - 1, y, points)
    flood_fill_util(data, x, y + 1, points)
    flood_fill_util(data, x, y - 1, points)


def flood_fill(y, x, data):
    points = []
    flood_fill_util(data, x, y, points)

    if len(points) > 0:
        basins.append(points)


lowest = get_lowest_points(d)
for point, (y, x) in enumerate(lowest):
    flood_fill(y, x, d)

basins = sorted(basins, key=len, reverse=True)
a = len(basins[0])
b = len(basins[1])
c = len(basins[2])

print(a * b * c)
