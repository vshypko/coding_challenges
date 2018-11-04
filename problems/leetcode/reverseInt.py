# 7
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = 1
        reversedInt = 0

        if x < 0:
            negative = -1
            x *= -1

        while x > 0:
            reversedInt = (x % 10) + (10 * reversedInt)
            x //= 10

        if reversedInt > (2 ** 31) - 1:
            return 0

        return int(reversedInt * negative)
