# 1.7
class Solution:
    def __init__(self):
        # for testing purposes
        pass

    # O(N^2) runtime
    # O(1) space
    def rotateMatrix(self, m):
        if not m:
            return m
        if not len(m) == len(m[0]) or len(m) % 4 != 0:
            return

        currentLength = n = len(m)

        for i in range(n // 2):
            # topLeft = m[i][j]
            # topRight = m[j][n - 1 - i]
            # bottomRight = m[n - 1 - i][n - 1 - j]
            # bottomLeft = m[n - 1 - j][i]
            currentLength -= 1

            for j in range(i, currentLength):
                temp = m[i][j]
                m[i][j] = m[j][n - 1 - i]
                m[j][n - 1 - i] = m[n - 1 - i][n - 1 - j]
                m[n - 1 - i][n - 1 - j] = m[n - 1 - j][i]
                m[n - 1 - j][i] = temp
        return m


assert (Solution().rotateMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
        == [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]])
assert (Solution().rotateMatrix([[1, 2, 3, 4, 5, 6, 7, 8],
                                 [9, 10, 11, 12, 13, 14, 15, 16],
                                 [17, 18, 19, 20, 21, 22, 23, 24],
                                 [25, 26, 27, 28, 29, 30, 31, 32],
                                 [33, 34, 35, 36, 37, 38, 39, 40],
                                 [41, 42, 43, 44, 45, 46, 47, 48],
                                 [49, 50, 51, 52, 53, 54, 55, 56],
                                 [57, 58, 59, 60, 61, 62, 63, 64]])
                                == [[8, 16, 24, 32, 40, 48, 56, 64],
                                    [7, 15, 23, 31, 39, 47, 55, 63],
                                    [6, 14, 22, 30, 38, 46, 54, 62],
                                    [5, 13, 21, 29, 37, 45, 53, 61],
                                    [4, 12, 20, 28, 36, 44, 52, 60],
                                    [3, 11, 19, 27, 35, 43, 51, 59],
                                    [2, 10, 18, 26, 34, 42, 50, 58],
                                    [1, 9, 17, 25, 33, 41, 49, 57]])
assert (Solution().rotateMatrix([]) == [])
