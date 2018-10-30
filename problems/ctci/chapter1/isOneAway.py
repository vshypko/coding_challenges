# 1.5
class Solution:
    def __init__(self):
        # for testing purposes
        pass

    # O(N) runtime
    # O(1) space
    def isOneAway(self, s1, s2):
        if abs(len(s1) - len(s2)) > 1:
            return False

        diffCounter = 0
        longerString = s1
        shorterString = s2

        if len(s1) <= len(s2):
            longerString = s2
            shorterString = s1

        j = 0
        for i in range(len(longerString)):
            if j >= len(shorterString) or longerString[i] != shorterString[j]:
                diffCounter += 1
                if len(shorterString) < len(longerString):
                    continue
            j += 1

        return diffCounter == 0 or diffCounter == 1


assert (Solution().isOneAway("pale", "pe") is False)
assert (Solution().isOneAway("pale", "ple") is True)
assert (Solution().isOneAway("pales", "pale") is True)
assert (Solution().isOneAway("pale", "bale") is True)
assert (Solution().isOneAway("pale", "bake") is False)
