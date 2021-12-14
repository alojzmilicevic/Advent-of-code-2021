from statistics import median
from linereader import read_line

data = [int(x) for x in read_line('7.input.txt', ',')]

med = int(median(data))

total_distance = 0
for item in data:
    total_distance += abs(item - med)

print(total_distance)
