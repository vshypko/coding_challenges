# 198
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        results = [0] * len(nums)
        results[0] = nums[0]
        results[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            results[i] = max(results[i-1], results[i-2] + nums[i])

        return results[len(nums)-1]
