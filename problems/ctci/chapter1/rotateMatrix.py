# 1.7
class Solution:
    def __init__(self):
        # for testing purposes
        pass

    # O() runtime
    # O() space
    def rotateMatrix(self, m):
        if not m:
            return m

        for row in m:
            print(row)

        return

assert (Solution().rotateMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
assert (Solution().rotateMatrix([]) == [])
