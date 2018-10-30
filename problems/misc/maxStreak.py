class Solution:
    def __init__(self):
        # for testing purposes
        pass

    def maxStreak(self, m, data):
        allAttended = ""
        maxDays = counter = 0
        for i in range(m):
            allAttended += 'Y'

        for day in data:
            if day == allAttended:
                counter += 1
            if day != allAttended:
                counter = 0
            maxDays = max(maxDays, counter)

        return maxDays


assert Solution().maxStreak(4, ['YNYY', 'YYYY', 'YYYY', 'YYNY', 'NYYN']) == 2
assert Solution().maxStreak(3, ['YYY', 'YNN', 'YYY', 'YYY', 'YYY', 'NYN']) == 3
