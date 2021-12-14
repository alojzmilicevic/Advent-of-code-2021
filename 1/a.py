from linereader import read_file

data = [int(x) for x in read_file('1.input.txt')]

start = data[0]

total = 0
for item in data:
    if item > start:
        total += 1
    start = item

print(total)