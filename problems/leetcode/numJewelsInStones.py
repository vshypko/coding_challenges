# 771
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewelStones = 0
        for s in S:
            if s in J:
                jewelStones += 1
        return jewelStones
