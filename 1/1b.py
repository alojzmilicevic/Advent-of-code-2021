from linereader import read_file

data = [int(x) for x in read_file('1.input.txt')]

start = data[0] + data[1] + data[2]

total = 0
for i in range(1, len(data) - 2):
    cur = data[i] + data[i + 1] + data[i + 2]
    if cur > start:
        total += 1
    start = cur

print(total)
