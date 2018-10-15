# 46
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        result = list()
        if n <= 1:
            return [nums]
        for i in range(n):
            for j in self.permute(nums[:i] + nums[i+1:]):
                result.append([nums[i]] + j)
        return result
