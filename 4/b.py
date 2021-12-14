file = open('4.input.txt', 'r')

data = [int(x) for x in file.readline().split(',')]

boards = []
curBoard = []

boardMap = []
curBoardMap = []
i = 0
for line in file:
    if line != '\n':
        nums = [int(s) for s in line.split() if s.isdigit()]
        curBoard.append(nums)

        curBoardMap.append([False, False, False, False, False])

        if i % 5 == 0:
            boards.append(curBoard)
            curBoard = []

            boardMap.append(curBoardMap)
            curBoardMap = []

            i = -1

    i += 1


def has_bingo(grid, row, col):
    col_has_bingo = True
    for i in range(0, 5):
        if not grid[i][col]:
            col_has_bingo = False

    return sum(grid[row]) == 5 or col_has_bingo


total_rounds = []
current_board = 0


def check_board():
    numbers_drawn = 0

    for current_drawn in data:
        for row in range(0, len(board)):
            for col in range(0, 5):
                if board[row][col] == current_drawn:
                    boardMap[current_board][row][col] = True

                    if has_bingo(boardMap[current_board], row, col):
                        return numbers_drawn, current_drawn

        numbers_drawn += 1


current = -1
for board in boards:
    num_drawn, current = check_board()
    print(current)
    total_rounds.append([num_drawn, current])
    current_board += 1

max_value = max(total_rounds)

max_index = total_rounds.index(max_value)

print(max_index)

s = 0
for r in range(0, len(boards[max_index])):
    for k in range(0, len(boards[max_index][r])):
        if not boardMap[max_index][r][k]:
            s += boards[max_index][r][k]

print(s * total_rounds[max_index][1])
