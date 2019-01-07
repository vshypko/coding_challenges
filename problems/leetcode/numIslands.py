# 200

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or len(grid) <= 0 or len(grid[0]) <= 0:
            return 0

        numIslands = 0

        def dfs(grid, i, j):
            if not (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == '0'):
                grid[i][j] = '0'
                dfs(grid, i - 1, j)
                dfs(grid, i + 1, j)
                dfs(grid, i, j - 1)
                dfs(grid, i, j + 1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    numIslands += 1
        return numIslands
