# 1.1
class Solution:
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

    assert isUnique("abcd")
