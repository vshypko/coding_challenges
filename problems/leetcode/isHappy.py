# 202
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        seen = set()

        while n != 1:
            temp = 0
            while n:
                temp += (n - n // 10 * 10) ** 2
                n //= 10
            n = temp
            if n in seen:
                return False
            seen.add(n)

        return True
