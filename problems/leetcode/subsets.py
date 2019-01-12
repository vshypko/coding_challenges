class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]

        for num in nums:
            n = len(result)
            for j in range(n):
                newSubset = list(result[j])
                newSubset.append(num)
                result.append(newSubset)

        return result
