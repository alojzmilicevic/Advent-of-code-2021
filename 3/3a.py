from linereader import read_file

data = read_file('3.input.txt')

arr = []
for i in range(0, len(data)):
    if i == 0:
        for item in data[i]:
            arr.append([0, 0])

    line = data[i]

    for k in range(0, len(line)):
        arr[k][int(line[k])] += 1

gamma = ''
epsilon = ''
for item in arr:
    if item[0] > item[1]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"


print(int(gamma, 2) * int(epsilon, 2))
