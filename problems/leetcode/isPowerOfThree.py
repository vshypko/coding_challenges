# 326
import math


class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #         SOLUTION 1: (log, no loops)
        #         if n <= 0:
        #             return False
        #         logValue = math.log(n, 3)
        #         floor = math.floor(logValue)
        #         ceil = math.ceil(logValue)

        #         return 3 ** floor == n or 3 ** ceil == n

        if n <= 0:
            return False
        while n % 3 == 0:
            n = int(n / 3)
        return n == 1
