def read_file(file_name):
    f = open(file_name, "r")

    arr = []
    for line in f:
        arr.append(line.replace('\n', ''))

    return arr


def read_lines(file_name, token):
    f = open(file_name, 'r')

    arr = []

    for line in f:
        arr.append(line.replace('\n', '').split(token))

    return arr


def read_line(file_name, token):
    return open(file_name, 'r').readline().split(token)


def read_parts(file_name, delim, split_instructions):
    arr = read_file(file_name)

    part = []
    parts = dict().fromkeys(split_instructions)
    i = 0
    for idx, item in enumerate(arr):
        if item != delim:
            part.append(item)

        if item == delim or idx == len(arr) - 1:
            parts[split_instructions[i]] = part
            part = []
            i += 1

    return parts
