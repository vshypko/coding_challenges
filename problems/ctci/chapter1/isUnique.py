# 1.1
class Solution:
    def __init__(self):
        # for testing purposes
        pass

    # O(N) runtime
    # O(N) space
    def isUnique(self, s):
        if not s:
            return True

        hashmap = {}
        for c in s:
            if c not in hashmap.keys():
                hashmap[c] = 1
            else:
                return False

        return True

    # O(Nlog(N)) runtime
    # O(1) space
    def isUniqueSort(self, s):
        if not s:
            return True

        sortedS = sorted(s)
        for i in range(len(sortedS) - 1):
            if sortedS[i] == sortedS[i + 1]:
                return False

        return True


assert (Solution().isUnique("abcd") is True)
assert (Solution().isUnique("dzgqmzksqod") is False)

assert (Solution().isUniqueSort("abcd") is True)
assert (Solution().isUniqueSort("dzgqmzksqod") is False)
