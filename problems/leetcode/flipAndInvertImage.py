# 832
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(A[0])
        for row in A:
            for i in range(n // 2):
                row[i], row[~i] = abs(row[~i] - 1), abs(row[i] - 1)
            if n % 2 == 1:
                row[n // 2] = abs(row[n // 2] - 1)

        return A
