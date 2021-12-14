import queue
from pprint import pprint

from linereader import read_file

d = [[int(y) for y in list(x)] for x in read_file('in.11.txt')]

d = [
    [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
    [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
    [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
    [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
    [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
    [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
    [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
    [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
    [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
    [5, 2, 8, 3, 7, 5, 1, 5, 2, 6]]
q = queue.Queue()


def get_neighbours(row, col):
    arr = [
        (row - 1, col - 1),
        (row - 1, col),
        (row - 1, col + 1),
        (row, col - 1),
        (row, col + 1),
        (row + 1, col - 1),
        (row + 1, col),
        (row + 1, col + 1)
    ]

    return list(filter(lambda coords: (0 <= coords[0] < 10) and 0 <= coords[1] < 10, arr))


flashes = 0


def sim():
    f = 0

    def first_pass():
        fl = 0
        for row in range(0, len(d)):
            for col in range(0, len(d[row])):
                d[row][col] += 1

                if d[row][col] > 9:
                    q.put((row, col))
                    d[row][col] = 0
                    fl += 1

        return fl

    f += first_pass()

    while not q.empty():
        current = q.get()
        neighbours = get_neighbours(current[0], current[1])

        for neighbour, (y, x) in enumerate(neighbours):
            if d[y][x] != 0:
                d[y][x] += 1

            if d[y][x] > 9:
                q.put((y, x))
                d[y][x] = 0
                f += 1
    return f


for i in range(0, 308):
    flashes += sim()
    if sum(sum(d, [])) == 0:
        print("NOW", i)
print(flashes)
