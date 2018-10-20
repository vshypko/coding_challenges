# 1.2
class Solution:
    def __init__(self):
        # for testing purposes
        pass

    # O(N) runtime
    # O(N) space
    def isPermutation(self, s1, s2):
        print(s1)
        print(s2)
        if len(s1) != len(s2):
            return False
        hashmap1 = {}
        hashmap2 = {}
        firstCounter = 0
        secondCounter = 0

        for c in s1:
            if c not in hashmap1.keys():
                hashmap1[c] = 1
            else:
                hashmap1[c] += 1

        for c in s2:
            if c not in hashmap2.keys():
                hashmap2[c] = 1
            else:
                hashmap2[c] += 1

        for key, value in hashmap1.items():
            if key in hashmap2.keys():
                if hashmap1[key] >= hashmap2[key]:
                    firstCounter += 1

        for key, value in hashmap2.items():
            if key in hashmap1.keys():
                if hashmap2[key] >= hashmap1[key]:
                    secondCounter += 1

        return firstCounter == len(s2) or secondCounter == len(s1)


assert (Solution().isPermutation("abcd", "bc") is True)
assert (Solution().isPermutation("fada", "zx") is False)
