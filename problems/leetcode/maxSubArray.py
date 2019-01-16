# 53
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentSum = maxSum = float('-inf')

        for num in nums:
            currentSum = max(currentSum + num, num)
            maxSum = max(maxSum, currentSum)

        return maxSum
