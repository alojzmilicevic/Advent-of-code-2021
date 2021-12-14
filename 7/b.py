from linereader import read_line

data = [int(x) for x in read_line('7.input.txt', ',')]


def get_cost(a, b):
    n = abs(a - b)
    return (n * (n + 1)) // 2


def calc(arr):
    d = {}
    for i in range(min(arr), max(arr)):
        min_sum = sum(map(lambda y: abs(y - i), filter(lambda x: x < i, arr)))
        max_sum = sum(map(lambda y: abs(y - i), filter(lambda x: x > i, arr)))

        d.setdefault(i, abs(min_sum - max_sum))

    pos = min(d, key=d.get)
    print(pos)

    total_distance = 0
    for item in arr:
        total_distance += get_cost(item, pos)

    return total_distance


res = calc(data)

print(res)

costs = []
for pos in range(min(data), max(data)):
    costs.append(sum(get_cost(i, pos) for i in data))
print(min(costs))
