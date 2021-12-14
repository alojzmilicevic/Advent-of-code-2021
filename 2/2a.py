from linereader import read_file

y = 0
x = 0

data = read_file('2.input.txt')

for line in data:
    direction, delta = line.split(" ")
    delta = int(delta)

    if direction == 'up':
        y -= delta
    elif direction == 'down':
        y += delta
    elif direction == 'forward':
        x += delta

print(x * y)
