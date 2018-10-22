# 1.8
class Solution:
    def __init__(self):
        # for testing purposes
        pass

    # O(MN) runtime
    # O(1) space
    def zeroMatrix(self, m):
        zeroIndex = set()

        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] == 0:
                    zeroIndex.add((i, j))

        for index in zeroIndex:
            for i in range(len(m)):
                m[i][index[1]] = 0
            for j in range(len(m[0])):
                m[index[0]][j] = 0

        return m

assert Solution().zeroMatrix([[1, 0, 3, 4], [5, 6, 7, 0], [9, 10, 11, 12]]) == [[0, 0, 0, 0], [0, 0, 0, 0], [9, 0, 11, 0]]
