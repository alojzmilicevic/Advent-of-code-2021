from linereader import read_file

y = 0
x = 0
aim = 0

data = read_file('2.input.txt')

for line in data:
    direction, delta = line.split(" ")
    delta = int(delta)

    if direction == 'up':
        aim -= delta
    elif direction == 'down':
        aim += delta
    elif direction == 'forward':
        x += delta
        y += (aim * delta)

print(x * y)
