# 692
import collections
import heapq

class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        hashmap = collections.Counter(words)
        resultArray = list()
        heap = list()

        for word, freq in hashmap.items():
            heap.append((-freq, word))
        heapq.heapify(heap)

        for i in range(k):
            resultArray.append(heapq.heappop(heap)[1])

        return resultArray
