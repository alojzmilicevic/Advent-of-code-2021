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


def checkCol(arr, col):
    print(arr)
    for k in range(0, 5):
        if not arr[k][col]:
            return False

    return True


def do():
    for number_drawn in data:
        for i in range(0, len(boards)):
            table = boards[i]
            mappsy = boardMap[i]
            for row in range(0, len(table)):
                for col in range(0, len(table[row])):
                    if table[row][col] == number_drawn:
                        mappsy[row][col] = True
                        rowTruthValue = sum(mappsy[row])
                        if rowTruthValue == 5 or checkCol(mappsy, col):
                            print("OVER", number_drawn)
                            return i, number_drawn


correct_index, act = do()

s = 0
for r in range(0, len(boards[correct_index])):
    for k in range(0, len(boards[correct_index][r])):
        if not boardMap[correct_index][r][k]:
            s += boards[correct_index][r][k]

print("sum:", s * act)
# print("SUM AFTER: ", number_drawn, "Is drawn", rowSum)
# if rowSum < 0:
# print("ENDING AFTER", number_drawn, "was drawn")
# break
