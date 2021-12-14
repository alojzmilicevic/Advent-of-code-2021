import sys

from linereader import read_file

height = 100
width = 100


d = [[int(y) for y in list(x)] for x in read_file('a.in.txt')]


def is_local_min(row, col, arr):
    north = sys.maxsize
    south = sys.maxsize
    east = sys.maxsize
    west = sys.maxsize

    cur = arr[row][col]

    if row > 0:
        north = arr[row - 1][col]

    if row < (height - 1):
        south = arr[row + 1][col]

    if col > 0:
        west = arr[row][col - 1]

    if col < (width - 1):
        east = arr[row][col + 1]

    return cur < north and cur < south and cur < east and cur < west


risk_level = 0
for i in range(0, len(d)):
    for j in range(0, len(d[i])):
        if is_local_min(i, j, d):
            risk_level += d[i][j] + 1

print(risk_level)