# 1.1
class Solution:
    # O(N) runtime
    # O(N) space
    def isUnique(s):
        if not s:
            return True

        hashmap = {}
        for c in s:
            if c not in hashmap.keys():
                hashmap[c] = 1
            else:
                return False
        return True

    # O(N logN) runtime
    # O(1) space
    def isUniqueSort(s):
        if not s:
            return True

        sortedS = sorted(s)
        for i in range(len(sortedS) - 1):
            if sortedS[i] == sortedS[i + 1]:
                return False
        return True

    assert (isUnique("abcd") is True)
    assert (isUnique("dzgqmzksqod") is False)

    assert (isUniqueSort("abcd") is True)
    assert (isUniqueSort("dzgqmzksqod") is False)
