# 628
class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        elif len(nums) == 4:
            return max(nums[0] * nums[1] * nums[3], nums[1] * nums[2] * nums[3])
        return max(nums[0] * nums[1] * nums[-1], nums[-3] * nums[-2] * nums[-1])
