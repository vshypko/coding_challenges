# 136
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictionary = {}

        for item in nums:
            if item in dictionary.keys():
                dictionary[item] += 1
            else:
                dictionary[item] = 1

        for k, v in dictionary.items():
            if v == 1:
                return k
