# 54
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        left = top = 0
        bottom = len(matrix)
        right = len(matrix[0])
        rA = list()
        lenMatrix = right * bottom

        while left < right or top < bottom:
            # ->
            if left < right and len(rA) < lenMatrix:
                for i in range(left, right):
                    rA.append(matrix[top][i])
                top += 1

            # down
            if top < bottom and len(rA) < lenMatrix:
                for i in range(top, bottom):
                    rA.append(matrix[i][right - 1])
                right -= 1

            # <-
            if left < right and len(rA) < lenMatrix:
                for i in range(right - 1, left - 1, -1):
                    rA.append(matrix[bottom - 1][i])
                bottom -= 1

            # ^
            if top < bottom and len(rA) < lenMatrix:
                for i in range(bottom - 1, top - 1, -1):
                    rA.append(matrix[i][left])
                left += 1

            if len(rA) >= lenMatrix:
                break

        return rA
