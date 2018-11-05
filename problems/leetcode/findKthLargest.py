import heapq

# 215
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # O(N logN)
        # return sorted(nums)[-k]

        # O(N)
        #         heap = list()
        #         for num in nums:
        #             heapq.heappush(heap, num)
        #             if len(heap) > k:
        #                 heapq.heappop(heap)

        #         return heapq.heappop(heap)
        return heapq.nlargest(k, nums)[-1]
