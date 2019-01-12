# 8.2

# O(rc) runtime
# O(rc) space
def robotGrid(grid):
    r = len(grid)
    c = len(grid[0])

    dp = [[]] * r
    for i in range(len(dp)):
        dp[i] = [None] * c

    dp[0][0] = [[(0, 0)]]
    for i in range(r):
        for j in range(c):
            if grid[i][j] != 0 and not (i == 0 and j == 0):
                if i > 0 and dp[i - 1][j]:
                    if not dp[i][j]:
                        dp[i][j] = list()
                    for topPath in dp[i - 1][j]:
                        dp[i][j].append(list(topPath))
                if j > 0 and dp[i][j - 1]:
                    if not dp[i][j]:
                        dp[i][j] = list()
                    for leftPath in dp[i][j - 1]:
                        dp[i][j].append(list(leftPath))
                if dp[i][j]:
                    for path in dp[i][j]:
                        path.append((i, j))
    return dp[r - 1][c - 1] or list()


grid = [
    [1, 0, 1],
    [1, 1, 1],
    [1, 1, 1],
    [0, 0, 1]
]
result = robotGrid(grid)
for path in result:
    print(path)
