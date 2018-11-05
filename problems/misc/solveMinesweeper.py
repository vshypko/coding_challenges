def solveMinesweeper(puzzleArray):
    n = len(puzzleArray)
    scoreArray = [0] * n
    for i in range(n):
        scoreArray[i] = [0] * n

    for i in range(n):
        for j in range(n):
            if i > 0:
                if puzzleArray[i - 1][j] == 'm':
                    scoreArray[i][j] += 1
            if j > 0:
                if puzzleArray[i][j - 1] == 'm':
                    scoreArray[i][j] += 1
            if i > 0 and j > 0:
                if puzzleArray[i - 1][j - 1] == 'm':
                    scoreArray[i][j] += 1
            if i < n - 1:
                if puzzleArray[i + 1][j] == 'm':
                    scoreArray[i][j] += 1
            if j < n - 1:
                if puzzleArray[i][j + 1] == 'm':
                    scoreArray[i][j] += 1
            if i < n - 1 and j < n - 1:
                if puzzleArray[i + 1][j + 1] == 'm':
                    scoreArray[i][j] += 1
            if i > 0 and j < n - 1:
                if puzzleArray[i - 1][j + 1] == 'm':
                    scoreArray[i][j] += 1
            if j > 0 and i < n - 1:
                if puzzleArray[i + 1][j - 1] == 'm':
                    scoreArray[i][j] += 1

    for i in range(n):
        for j in range(n):
            if i > 0:
                if puzzleArray[i - 1][j] == 'm':  # below
                    scoreArray[i][j] = 2

    for i in range(n):
        for j in range(n):
            if j > 0:
                if puzzleArray[i][j - 1] == 'm':  # to the right
                    scoreArray[i][j] = 0

    for i in range(n):
        if i % 2 == 1 and 'm' in puzzleArray[i]:
            for j in range(n):
                scoreArray[i][j] *= 3

    indexSet = set()
    for i in range(n):
        for j in range(n):
            if i > 0 and j > 0:
                if puzzleArray[i - 1][j - 1] == 'm' and (i, j) not in indexSet:
                    scoreArray[i][j] *= 2
                    indexSet.add((i, j))
            if i < n - 1 and j < n - 1:
                if puzzleArray[i + 1][j + 1] == 'm' and (i, j) not in indexSet:
                    scoreArray[i][j] *= 2
                    indexSet.add((i, j))
            if i > 0 and j < n - 1:
                if puzzleArray[i - 1][j + 1] == 'm' and (i, j) not in indexSet:
                    scoreArray[i][j] *= 2
                    indexSet.add((i, j))
            if j > 0 and i < n - 1:
                if puzzleArray[i + 1][j - 1] == 'm' and (i, j) not in indexSet:
                    scoreArray[i][j] *= 2
                    indexSet.add((i, j))

    for i in range(n):
        for j in range(n):
            if puzzleArray[i][j] == 'm':
                scoreArray[i][j] = -1

    return scoreArray
