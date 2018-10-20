# 1.4
class Solution:
    def __init__(self):
        # for testing purposes
        pass

    # O(N) runtime
    # O(N) space
    def isPalindromePermutation(self, s):
        if len(s) == 0:
            return True

        lowerS = s.replace(" ", "").lower()

        hashmap = {}
        for c in lowerS:
            if c not in hashmap.keys():
                hashmap[c] = 1
            else:
                hashmap[c] += 1

        oneCounter = 0
        for key in hashmap.keys():
            if hashmap[key] % 2 != 0:
                oneCounter += 1

        return oneCounter == 0 or oneCounter == 1


assert (Solution().isPalindromePermutation("Tact Coa") is True)
assert (Solution().isPalindromePermutation("Tact Cloa") is False)
assert (Solution().isPalindromePermutation("") is True)
