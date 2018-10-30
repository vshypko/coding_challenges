# 11
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        resultArea = 0

        while i < j:
            resultArea = max(resultArea, (j - i) * min(height[i], height[j]))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return resultArea
