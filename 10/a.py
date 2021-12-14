import linereader

d = linereader.read_file("10.in.txt")

matching_pairs = {
    "{": "}",
    "[": "]",
    "(": ")",
    "<": ">",
}

points_1 = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

points_2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,

}


def run(points, part2):
    total = 0
    scores = []

    for a in d:
        stack = []
        error = False
        cur_p = 0
        for i in range(0, len(a)):
            # opening chunk
            c = a[i]
            if c == '[' or c == '(' or c == '{' or c == '<':
                stack.append((c, i))

            else:
                opening_type = stack.pop()
                if c != matching_pairs[opening_type[0]]:
                    # print("ERROR: expected", matching_pairs[opening_type[0]], "found", c, "at", i)
                    total += points[c]
                    error = True
                    break

        if not error and part2:
            for item in reversed(stack):
                cur_p = (cur_p * 5) + points[matching_pairs[item[0]]]
            scores.append(cur_p)

    return scores, total


# part 1
res = run(points_1, False)
print(res[1])

# part 2
res = run(points_2, True)
scores = res[0]
print(sorted(scores)[len(scores) // 2])
