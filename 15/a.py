import sys
from timeit import default_timer as timer
from datetime import timedelta
from linereader import read_file
import heapq

d = [[int(y) for y in list(x)] for x in read_file('15.in.txt')]


def is_valid(x, y, height, width):
    return 0 <= x < width and 0 <= y < height


def get_manhattan_distance(row, col, g):
    sz = len(g) - 1
    return abs(sz - row) + abs(sz - col)


def dijkstra(grid):
    pq = [(0, (0, 0))]  # start at 0,0 at a distance of 0
    ROWS = len(grid)
    COLS = len(grid[0])

    distances = [[sys.maxsize for col in line] for line in grid]

    # Left, Above, Right, below
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    distances[0][0] = grid[0][0]
    while pq:
        dist, (i, j) = heapq.heappop(pq)

        if i == ROWS - 1 and j == COLS - 1:
            return dist

        for k in range(4):
            x = j + dx[k]
            y = i + dy[k]

            if is_valid(x, y, ROWS, COLS):
                if distances[y][x] > grid[i][j] + distances[i][j]:
                    heapq.heappush(pq, (dist + grid[y][x], (y, x)))
                    distances[y][x] = distances[i][j] + grid[y][x]


def a_star():
    pass


# Part 1
start = timer()
print("Part 1: ", dijkstra(d))
end = timer()
print("Total runtime: ", timedelta(seconds=end - start))

new_map = [line * 5 for line in d * 5]

size = len(d)
for i in range(size * 5):
    for j in range(size * 5):
        new_map[i][j] = (new_map[i][j] + i // size + j // size - 1) % 9 + 1

# Part 2
start = timer()
print("Part 1: ", dijkstra(new_map))
end = timer()
print("Total runtime: ", timedelta(seconds=end - start))
