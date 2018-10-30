# 70
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dpResults = [0] * (n + 1)
        dpResults[0] = dpResults[1] = 1

        for i in range(2, n + 1):
            dpResults[i] = dpResults[i - 1] + dpResults[i - 2]

        return dpResults[n]
