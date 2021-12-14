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