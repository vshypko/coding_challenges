# 121
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0

        if prices:
            largest = prices[len(prices) - 1]
            smallest = prices[len(prices) - 1]
            for item in prices[::-1]:
                if item > largest:
                    largest = item
                    smallest = float('inf')
                if item < smallest:
                    smallest = item
                if (largest - smallest) > max_profit:
                    max_profit = largest - smallest

        return max_profit
