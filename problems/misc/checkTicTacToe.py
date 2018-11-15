def checkTicTacToe(board):
    if not board:
        return

    n = len(board)
    emptySpace = 0

    # check horizontal and count empty spaces
    for row in board:
        emptySpace += row.count(0)
        rowSum = sum(row)
        if rowSum == n:
            return 1
        elif rowSum == -n:
            return -1

    # check vertical
    for i in range(n):
        counter = 0
        for j in range(n):
            counter += board[j][i]
        if counter == n:
            return 1
        elif counter == -n:
            return -1

    # check diagonal
    diagonal1 = 0
    diagonal2 = 0
    for i in range(n):
        diagonal1 += board[i][i]
        diagonal2 += board[i][n-1-i]
    if diagonal1 == n or diagonal2 == n:
        return 1
    elif diagonal1 == -n or diagonal2 == -n:
        return -1

    return 2 if emptySpace < 1 else 0


board = [[1,   -1,   -1],
         [1,    0,   0],
         [1,   -1,   -1]]

print(checkTicTacToe(board))
